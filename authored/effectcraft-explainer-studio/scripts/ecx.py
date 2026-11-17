#!/usr/bin/env python3
"""ecx - EffectCraft Explainer Studio.

Turns one JSON "beat sheet" into an explainer video built and rendered
entirely by EffectCraft (the free open-source motion graphics app).
Python standard library only. Original work, MIT licensed.

Commands
  ecx.py doctor                      find EffectCraft, fonts, voice engines
  ecx.py new NAME                    make a starter project folder
  ecx.py check SPEC                  validate the beat sheet, write sources.md
  ecx.py voice SPEC                  make narration per beat with a free voice engine
  ecx.py build SPEC [options]        build .ecproj, preview stills, optional mp4

Build options
  --format wide|tall|both            16:9 (YouTube) and/or 9:16 (Reels/Shorts). default: from spec
  --beats id1,id2                    build only these beats (cut a short from a long script)
  --render                           also render mp4 with narration audio
  --bitrate KBPS                     video bitrate for --render (smaller files)
  --out DIR                          output folder (default: ./out next to the spec)
  --no-stills                        skip preview stills
"""
import argparse, glob, json, math, os, re, shutil, subprocess, sys, wave

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "..", "assets")

# ----------------------------------------------------------------- look
PALETTES = {
    "paper": dict(bg="#f2eee4", fg="#14130f", mute="#6b675c", panel="#e3dccb",
                  accent="#d8431e", accent2="#1b5e7a", grid="#cfc8b4"),
    "ink":   dict(bg="#0e1014", fg="#f4f1ea", mute="#8b8f99", panel="#1c1f27",
                  accent="#ff6a3d", accent2="#4cc9f0", grid="#2a2e38"),
    "signal": dict(bg="#07121f", fg="#eaf4ff", mute="#7f95ad", panel="#12263d",
                   accent="#ffd23f", accent2="#3bceac", grid="#1d3753"),
}
FONTS = dict(head=("Noto Serif", "Bold"), body=("Inter", "Regular"),
             bold=("Inter", "SemiBold"), mono=("JetBrains Mono", "Regular"))


def hexrgb(h):
    h = h.lstrip("#")
    return [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]


class Ref:
    def __init__(self, s):
        self.s = s


def ser(o):
    if isinstance(o, Ref):
        return o.s
    if isinstance(o, dict):
        return "{" + ",".join(json.dumps(k) + ":" + ser(v) for k, v in o.items()) + "}"
    if isinstance(o, (list, tuple)):
        return "[" + ",".join(ser(v) for v in o) + "]"
    if isinstance(o, float):
        return repr(round(o, 3))
    return json.dumps(o)


class Fmt:
    def __init__(self, kind):
        self.kind = kind
        self.tall = kind == "tall"
        self.W, self.H = (1080, 1920) if self.tall else (1920, 1080)
        self.mx = 84 if self.tall else 130

    def s(self, wide, tall):
        return tall if self.tall else wide


# ----------------------------------------------------------------- scene writer
class Scene:
    def __init__(self, fmt, pal, fps=30, font_override=None):
        self.f, self.p, self.fps = fmt, pal, fps
        self.lines, self.n = [], 0
        self.fonts = dict(FONTS)
        if font_override:
            self.fonts.update({k: tuple(v) for k, v in font_override.items()})

    # raw
    def cmd(self, c, **p):
        self.n += 1
        v = "v%d" % self.n
        self.lines.append("var %s=app.run(%s,%s);" % (v, json.dumps(c), ser(p)))
        return Ref(v)

    def layer(self, c, **p):
        return Ref(self.cmd(c, **p).s + ".layer")

    def expr(self, L, path, e):
        self.cmd("prop.setExpression", layer=L, path=path, expression=e)

    def setv(self, L, path, v):
        self.cmd("prop.set", layer=L, path=path, value=v)

    def span(self, L, t0, t1):
        self.cmd("layer.timing", layers=[L], **{"in": t0, "out": t1})

    # motion expressions (comp time; layers always start at 0)
    @staticmethod
    def fade_expr(t0, t1, d=0.45, out=0.3):
        return "Math.min(easeOut(time,%.3f,%.3f,0,100),easeIn(time,%.3f,%.3f,100,0))" % (t0, t0 + d, t1 - out, t1)

    def appear(self, L, t0, t1, rise=0, pop=0, d=0.45, out=0.3):
        self.expr(L, "transform/opacity", self.fade_expr(t0, t1, d, out))
        if rise:
            self.expr(L, "transform/position",
                      "[value[0],easeOut(time,%.3f,%.3f,value[1]+%d,value[1])]" % (t0, t0 + d + 0.25, rise))
        if pop:
            self.expr(L, "transform/scale",
                      "var s=easeOut(time,%.3f,%.3f,%d,100);[s,s]" % (t0, t0 + d + 0.2, 100 - pop))

    # primitives
    def text(self, s, x, y, w, size, color=None, t0=0, t1=1, role="body", just="left",
             rise=24, h=None, name=None, emph=None, pop=0, caps=False, track=None):
        font, style = self.fonts[role]
        p = dict(text=s, box=[x, y, w, h or self.text_h(s, size, w)], size=size,
                 fill=color or self.p["fg"], font=font, style=style, justify=just)
        if caps:
            p["allCaps"] = True
        if track is not None:
            p["tracking"] = track
        if name:
            p["name"] = name
        L = self.layer("layer.newText", **p)
        if emph:
            for a, b in emph:
                self.cmd("layer.setText", layer=L, range=[a, b], fill=self.p["accent"])
        self.span(L, t0, t1)
        self.appear(L, t0, t1, rise=rise, pop=pop)
        return L

    @staticmethod
    def nlines(s, size, w, k=0.54):
        per = max(4, int(w / (size * k)))
        n = 0
        for para in s.split("\n"):
            cur, ln = 0, 1
            for word in para.split():
                if cur and cur + 1 + len(word) > per:
                    ln += 1
                    cur = len(word)
                else:
                    cur += (1 if cur else 0) + len(word)
            n += ln
        return n

    def text_h(self, s, size, w):
        return self.nlines(s, size, w) * size * 1.25 + 8

    def rect(self, x, y, w, h, color, t0, t1, op=100, rise=0, name=None, round_=0):
        kind = "rounded" if round_ else "rect"
        L = self.layer("layer.newShape", kind=kind, size=[w, h], fill=color, position=[x + w / 2, y + h / 2],
                       name=name or "rect")
        self.span(L, t0, t1)
        self.expr(L, "transform/opacity", "Math.min(easeOut(time,%.3f,%.3f,0,%d),easeIn(time,%.3f,%.3f,%d,0))"
                  % (t0, t0 + 0.4, op, t1 - 0.3, t1, op))
        if rise:
            self.expr(L, "transform/position", "[value[0],easeOut(time,%.3f,%.3f,value[1]+%d,value[1])]" % (t0, t0 + 0.6, rise))
        return L

    def dot(self, x, y, r, color, t0, t1, pulse=False, name=None):
        L = self.layer("layer.newShape", kind="ellipse", size=[2 * r, 2 * r], fill=color, position=[x, y],
                       name=name or "dot")
        self.span(L, t0, t1)
        self.expr(L, "transform/opacity", self.fade_expr(t0, t1, 0.2, 0.2))
        self.expr(L, "transform/scale", "var s=easeOut(time,%.3f,%.3f,0,100);[s,s]" % (t0, t0 + 0.4))
        if pulse:
            R = self.layer("layer.newShape", kind="ellipse", size=[2 * r, 2 * r], fill=color, position=[x, y],
                           name=name or "pulse", fillOpacity=35)
            self.span(R, t0 + 0.3, t1)
            self.expr(R, "transform/scale", "var p=((time-%.3f)%%1.6)/1.6;var s=100+p*260;[s,s]" % (t0 + 0.3))
            self.expr(R, "transform/opacity", "var p=((time-%.3f)%%1.6)/1.6;(1-p)*45" % (t0 + 0.3))
        return L

    def poly(self, pts, color, width, t0, t1, draw=(0, 1.0), closed=False, fill=None, name=None,
             fill_op=100, cap=1, keep=False, trim_expr=None):
        """Stroked path that draws on with trim paths (or a static filled shape when fill is given)."""
        S = self.layer("layer.newShape", kind="none", name=name or "path")
        self.cmd("shape.newPath", layer=S, vertices=[[round(a, 1), round(b, 1)] for a, b in pts], closed=closed,
                 fill=(fill if fill else False), stroke=(color if width else False), strokeWidth=width or 0, space="comp",
                 **({"fillOpacity": fill_op} if fill else {}))
        self.span(S, t0, t1)
        if width and not fill:
            self.setv(S, "contents/group/contents/stroke/cap", cap)
            self.setv(S, "contents/group/contents/stroke/join", 1)
        if trim_expr:
            self.cmd("layer.addShapeItem", layer=S, kind="trim")
            self.expr(S, "contents/trim/end", trim_expr)
        elif draw is not None and not fill:
            self.cmd("layer.addShapeItem", layer=S, kind="trim")
            a, d = t0 + draw[0], draw[1]
            self.expr(S, "contents/trim/end", "easeOut(time,%.3f,%.3f,0,100)" % (a, a + d))
        if not keep:
            self.expr(S, "transform/opacity", "easeIn(time,%.3f,%.3f,100,0)" % (t1 - 0.3, t1))
        return S


# ----------------------------------------------------------------- spec helpers
EST_WPS = 2.55  # spoken words per second when no audio exists


def words(s):
    return re.findall(r"\S+", s or "")


def clean_emph(s):
    """'a *b* c' -> ('a b c', [(2,3)])"""
    out, ranges, i = "", [], 0
    for part in re.split(r"(\*[^*]+\*)", s):
        if part.startswith("*") and part.endswith("*") and len(part) > 2:
            ranges.append((len(out), len(out) + len(part) - 2))
            out += part[1:-1]
        else:
            out += part
    return out, ranges


def audio_len(path):
    try:
        if path.lower().endswith(".wav"):
            with wave.open(path) as w:
                return w.getnframes() / float(w.getframerate())
    except Exception:
        pass
    if shutil.which("ffprobe"):
        try:
            r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                                "default=nw=1:nk=1", path], capture_output=True, text=True)
            return float(r.stdout.strip())
        except Exception:
            pass
    if shutil.which("afinfo"):
        r = subprocess.run(["afinfo", path], capture_output=True, text=True)
        m = re.search(r"estimated duration: ([\d.]+)", r.stdout)
        if m:
            return float(m.group(1))
    return None


MIN_DUR = dict(touchgrid=8, hook=4.5, kinetic=4.5, stat=4.5, bars=6, line=6, map=6.5, steps=7, timeline=7, compare=6,
               quote=5, outro=6)


class Plan:
    def __init__(self, spec, spec_dir, only=None):
        self.spec = spec
        self.dir = spec_dir
        beats = spec["beats"]
        if only:
            beats = [b for b in beats if b["id"] in only]
        self.beats = beats
        t = 0.0
        for i, b in enumerate(self.beats):
            b["_i"] = i
            vo = b.get("vo", "")
            af = b.get("vo_file") or os.path.join(spec_dir, "vo", b["id"] + ".wav")
            b["_audio"] = af if os.path.exists(af) else None
            real = audio_len(b["_audio"]) if b["_audio"] else None
            b["_vo_len"] = real if real else len(words(vo)) / EST_WPS
            d = max(b.get("dur", 0), MIN_DUR.get(b["type"], 5), (b["_vo_len"] + 1.0) if vo else 0)
            b["_t0"], b["_t1"] = t, t + d
            t += d
        self.total = t


# ----------------------------------------------------------------- beats
def cap_wrap(S, b, t0, t1, margin_y):
    """word-chunk captions spread over the voice-over time (even spread, approximate sync)."""
    vo = b.get("vo", "")
    ws = words(vo)
    if not ws:
        return
    f = S.f
    per = 3 if f.tall else 6
    chunks = [" ".join(ws[i:i + per]) for i in range(0, len(ws), per)]
    start, end = t0 + 0.35, min(t1 - 0.2, t0 + 0.35 + b["_vo_len"])
    weights = [len(c) for c in chunks]
    tot = float(sum(weights))
    cur = start
    size = f.s(44, 62)
    for c, w in zip(chunks, weights):
        dur = (end - start) * w / tot
        L = S.text(c, f.mx, margin_y, f.W - 2 * f.mx, size, S.p["fg"], cur, cur + dur, role="bold",
                   just="center", rise=0, h=size * 1.3, name="cap")
        # captions cut hard, no fade
        S.expr(L, "transform/opacity", "100")
        cur += dur


def chrome(S, b, plan):
    f, p = S.f, S.p
    t0, t1 = b["_t0"], b["_t1"]
    tag = b.get("tag") or ""
    n = "%02d" % (b["_i"] + 1)
    S.text("%s  %s" % (n, tag.upper()) if tag else n, f.mx, f.s(58, 90), f.W * 0.6, f.s(26, 30), p["accent"], t0, t1,
           role="mono", rise=0, h=40, name="chapter", track=60)
    src = b.get("source")
    if src and src != "none":
        label = src if isinstance(src, str) else src.get("label", "")
        txt = "SOURCE  " + label
        if f.tall:
            S.text(txt, f.mx, 128, f.W - 2 * f.mx, 26, p["mute"], t0 + 0.5, t1, role="mono", rise=0, h=34, name="source")
        else:
            S.text(txt, f.W - f.mx - 1000, f.s(58, 90), 1000, 24, p["mute"], t0 + 0.5, t1, role="mono", rise=0,
                   just="right", h=34, name="source")
    # progress bar
    # (one layer for the whole video is added once in build_scene)
    cap = plan.spec.get("captions", "tall")
    if b.get("vo") and (cap == "both" or (cap == "tall" and f.tall)):
        cap_wrap(S, b, t0, t1, f.H - f.s(170, 330))


def backdrop(S, b):
    f, p = S.f, S.p
    n = "%02d" % (b["_i"] + 1)
    sz = f.s(520, 640)
    L = S.text(n, f.W - f.s(760, 700) + 40, f.H - f.s(560, 980), f.s(760, 700), sz, p["grid"], b["_t0"], b["_t1"], role="head",
               just="right", rise=0, h=sz * 1.2, name="backdrop-number")
    S.expr(L, "transform/opacity", "Math.min(easeOut(time,%.3f,%.3f,0,55),easeIn(time,%.3f,%.3f,55,0))" % (b["_t0"], b["_t0"] + 0.8, b["_t1"] - 0.3, b["_t1"]))


def title_at(S, b, t0, t1, y=None):
    f = S.f
    if b.get("title"):
        S.text(b["title"], f.mx, y or f.s(150, 230), f.W - 2 * f.mx, f.s(54, 66), S.p["fg"], t0 + 0.2, t1, role="head",
               h=f.s(140, 220) if f.tall else 70, name="title")
        return (y or f.s(150, 230)) + (S.nlines(b["title"], f.s(54, 66), f.W - 2 * f.mx, 0.58) * f.s(54, 66) * 1.3) + 30
    return y or f.s(150, 230)


def beat_hook(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    w = f.W - 2 * f.mx
    size = f.s(150, 128)
    head, emph = clean_emph(d.get("headline", b.get("title", "")))
    nl = S.nlines(head, size, w, 0.60)
    hh = nl * size * 1.2
    top = (f.H - hh) / 2 - f.s(30, 60)
    if d.get("kicker"):
        S.text(d["kicker"].upper(), f.mx, top - f.s(70, 80), w, f.s(32, 32), p["accent"], t0 + 0.2, t1, role="mono",
               rise=16, h=44, track=80)
    S.text(head, f.mx, top, w, size, p["fg"], t0 + 0.4, t1, role="head", rise=40, h=hh, emph=emph)
    S.poly([(f.mx, top + hh + 26), (f.mx + f.s(360, 300), top + hh + 26)], p["accent"], 10, t0 + 0.4, t1,
           draw=(1.0, 0.7))
    if d.get("sub"):
        S.text(d["sub"], f.mx, top + hh + 60, w * 0.8, f.s(38, 40), p["mute"], t0 + 1.2, t1, role="body", rise=16)


def beat_kinetic(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    lines = d.get("lines", [])
    w = f.W - 2 * f.mx
    size = f.s(104, 100)
    y = f.s(300, 480)
    gap = f.s(34, 40)
    n = max(1, len(lines))
    span = max(1.0, (t1 - t0 - 1.6))
    heights = []
    for ln in lines:
        txt, _ = clean_emph(ln)
        heights.append(S.nlines(txt, size, w, 0.58) * size * 1.2)
    total = sum(heights) + gap * (n - 1)
    y = max(f.s(190, 300), (f.H - total) / 2 - f.s(0, 40))
    for i, ln in enumerate(lines):
        txt, emph = clean_emph(ln)
        a = t0 + 0.4 + i * span / n
        S.text(txt, f.mx, y, w, size, p["fg"] if i == len(lines) - 1 or True else p["mute"], a, t1, role="head",
               rise=36, h=heights[i], emph=emph)
        y += heights[i] + gap


def count_expr(t0, v, dec, pre, suf, dur=1.6):
    fmt = "var v=easeOut(time,%.3f,%.3f,0,%s);" % (t0, t0 + dur, repr(float(v)))
    fmt += "var s=v.toFixed(%d);var p=s.split('.');p[0]=p[0].replace(/\\B(?=(\\d{3})+(?!\\d))/g,',');" % dec
    return fmt + "%s+p.join('.')+%s" % (json.dumps(pre), json.dumps(suf))


def beat_stat(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    w = f.W - 2 * f.mx
    size = f.s(300, 280)
    pre, suf = d.get("prefix", ""), d.get("suffix", "")
    val = d.get("value", 0)
    dec = int(d.get("decimals", 0))
    y = f.s(230, 420)
    L = S.text(pre + str(val) + suf, f.mx, y, w, size, p["accent"], t0 + 0.3, t1, role="head", rise=0, h=size * 1.25)
    try:
        S.expr(L, "text/sourceText", count_expr(t0 + 0.4, float(val), dec, pre, suf))
    except Exception:
        pass
    ly = y + size * 1.2 + 10
    lab = d.get("label", "")
    S.text(lab, f.mx, ly, w * (0.9 if f.tall else 0.7), f.s(56, 54), p["fg"], t0 + 1.2, t1, role="bold", rise=20)
    if d.get("context"):
        cy = ly + S.nlines(lab, f.s(56, 54), w * (0.9 if f.tall else 0.7)) * f.s(56, 54) * 1.25 + 24
        S.text(d["context"], f.mx, cy, w * 0.75, f.s(36, 38), p["mute"], t0 + 1.8, t1, role="body", rise=14)


def beat_bars(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    items = d.get("items", [])
    unit = d.get("unit", "")
    top = title_at(S, b, t0, t1)
    mx = f.mx
    areaH = f.H - top - f.s(150, 400)
    n = max(1, len(items))
    rowH = min(f.s(120, 230), areaH / n)
    labelW = f.s(430, 0)
    x0 = mx + labelW
    maxW = f.W - mx - x0 - f.s(230, 300)
    vmax = float(d.get("max") or max([i["value"] for i in items] + [1]))
    hl = d.get("highlight")
    y = top + 20
    for k, it in enumerate(items):
        a = t0 + 0.7 + k * 0.35
        is_hl = hl is None and k == 0 or hl == it["label"] or hl == k
        col = p["accent"] if is_hl else p["accent2"]
        if f.tall:
            S.text(it["label"], mx, y, f.W - 2 * mx, 46, p["fg"], a, t1, role="bold", rise=10, h=60)
            by = y + 96
        else:
            S.text(it["label"], mx, y + rowH * 0.5 - 28, labelW - 20, 46, p["fg"], a, t1, role="bold", rise=10, h=50)
            by = y + rowH * 0.5
        ln = max(8, maxW * it["value"] / vmax)
        th = rowH * (0.40 if not f.tall else 0.22)
        S.poly([(x0, by), (x0 + ln, by)], col, th, a, t1, draw=(0.0, 0.9), cap=0)
        v = it["value"]
        dec = 0 if float(v).is_integer() else 1
        L = S.text(str(v), x0 + ln + 22, by - f.s(36, 40), 260, f.s(60, 68), p["fg"], a + 0.6, t1, role="bold", rise=0, h=80)
        S.expr(L, "text/sourceText", count_expr(a + 0.1, float(v), dec, d.get("prefix", ""), unit, 0.9))
        y += rowH


def beat_line(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    pts = d.get("points", [])
    if len(pts) < 2:
        return
    top = title_at(S, b, t0, t1)
    x0, x1 = f.mx + f.s(90, 110), f.W - f.mx - f.s(60, 30)
    y0 = top + f.s(30, 40)
    y1 = f.H - f.s(210, 420)
    vals = [float(v) for _, v in pts]
    lo, hi = d.get("min", min(vals)), d.get("max", max(vals))
    if lo == hi:
        hi = lo + 1
    pad = (hi - lo) * 0.08
    lo, hi = lo - pad, hi + pad
    X = lambda i: x0 + (x1 - x0) * i / (len(pts) - 1)
    Y = lambda v: y1 - (y1 - y0) * (float(v) - lo) / (hi - lo)
    unit = d.get("unit", "")
    for g in range(4):
        gv = lo + (hi - lo) * g / 3
        gy = Y(gv)
        S.poly([(x0, gy), (x1, gy)], p["grid"], 2, t0 + 0.2, t1, draw=(0.1, 0.6), cap=0)
        S.text(("%.0f" if (hi - lo) > 8 else "%.1f") % gv + unit, f.mx - 14, gy - 40, 160, f.s(28, 34), p["mute"], t0 + 0.5, t1,
               role="mono", rise=0, just="left", h=30)
    path = [(X(i), Y(v)) for i, (_, v) in enumerate(pts)]
    S.poly(path, p["accent"], f.s(9, 10), t0 + 0.6, t1, draw=(0.0, 2.6), name="series")
    ends = [0, len(pts) - 1]
    for i in ends:
        S.text(str(pts[i][0]), X(i) - 90, y1 + 18, 180, f.s(30, 34), p["mute"], t0 + 0.6, t1, role="mono", rise=0, just="center",
               h=34)
    S.dot(X(len(pts) - 1), Y(vals[-1]), 14, p["accent"], t0 + 3.0, t1, pulse=True)
    lastlab = "%s%s" % (pts[-1][1], unit)
    S.text(lastlab, X(len(pts) - 1) - 300, Y(vals[-1]) - 100, 290, f.s(68, 80), p["fg"], t0 + 3.1, t1, role="bold", just="right",
           rise=0, h=100)
    for an in d.get("annotations", []):
        i = int(an["at"])
        frac = i / (len(pts) - 1)
        a = t0 + 0.6 + 2.6 * frac * 0.9
        S.dot(X(i), Y(vals[i]), 9, p["accent2"], a, t1)
        S.text(an["text"], min(max(X(i) - 200, f.mx), f.W - f.mx - 400), Y(vals[i]) + 30, 400, f.s(32, 38), p["fg"], a + 0.2, t1,
               role="body", just="center", rise=10)


def project(f, lon, lat, view):
    if view["mode"] == "eq":
        t = math.asin(math.sqrt(3) / 2 * math.sin(math.radians(lat)))
        lam = math.radians(lon)
        x = 2 * math.sqrt(3) * lam * math.cos(t) / (3 * (1.340264 + 3 * (-0.081106) * t ** 2 + t ** 6 * (0.000893 * 7 + 3 * 0.003796 * t ** 2)))
        y = t * (1.340264 + (-0.081106) * t ** 2 + t ** 6 * (0.000893 + 0.003796 * t ** 2))
        return x, -y
    return math.radians(lon) * view["cos"], -math.radians(lat)


def clip_poly(pts, rect):
    """Sutherland-Hodgman clip of a polygon to rect (x0,y0,x1,y1)."""
    x0, y0, x1, y1 = rect
    def clip(poly, inside, cut):
        out = []
        for i, cur in enumerate(poly):
            prev = poly[i - 1]
            if inside(cur):
                if not inside(prev):
                    out.append(cut(prev, cur))
                out.append(cur)
            elif inside(prev):
                out.append(cut(prev, cur))
        return out
    def vx(xc):
        return lambda a, b: (xc, a[1] + (b[1] - a[1]) * (xc - a[0]) / (b[0] - a[0]))
    def hy(yc):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (yc - a[1]) / (b[1] - a[1]), yc)
    poly = pts
    for ins, cut in ((lambda q: q[0] >= x0, vx(x0)), (lambda q: q[0] <= x1, vx(x1)),
                     (lambda q: q[1] >= y0, hy(y0)), (lambda q: q[1] <= y1, hy(y1))):
        if not poly:
            break
        poly = clip(poly, ins, cut)
    return poly


def beat_map(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    world = json.load(open(os.path.join(ASSETS, "world_110m.json")))
    hl = [c.upper() for c in d.get("highlight", [])]
    pins = d.get("pins", [])
    routes = d.get("routes", [])
    top = title_at(S, b, t0, t1)
    area = (f.mx, top + 10, f.W - 2 * f.mx, f.H - top - f.s(190, 440))
    pts = []
    for c in hl:
        for r in world.get(c, {}).get("r", []):
            if not r["h"]:
                pts += r["p"]
    pts += [(q["lon"], q["lat"]) for q in pins]
    for r in routes:
        pts += [tuple(r["from"]), tuple(r["to"])]
    bbox = d.get("bbox")
    if bbox:
        lon0, lat0, lon1, lat1 = bbox
    elif pts:
        lon0, lon1 = min(q[0] for q in pts), max(q[0] for q in pts)
        lat0, lat1 = min(q[1] for q in pts), max(q[1] for q in pts)
        px, py = (lon1 - lon0) * 0.25 + 4, (lat1 - lat0) * 0.25 + 3
        lon0, lon1, lat0, lat1 = lon0 - px, lon1 + px, lat0 - py, lat1 + py
    else:
        lon0, lat0, lon1, lat1 = -180, -58, 180, 85
    lon0, lon1 = max(-180, lon0), min(180, lon1)
    lat0, lat1 = max(-85, lat0), min(85, lat1)
    mode = "eq" if (lon1 - lon0) > 200 else "plate"
    view = dict(mode=mode, cos=math.cos(math.radians((lat0 + lat1) / 2)))
    corners = [project(f, lon0, lat0, view), project(f, lon1, lat1, view)]
    xs = [c[0] for c in corners]
    ys = [c[1] for c in corners]
    if mode == "eq":
        xs = [project(f, lon0, 0, view)[0], project(f, lon1, 0, view)[0]]
        ys = [project(f, 0, lat1, view)[1], project(f, 0, lat0, view)[1]]
    sx = area[2] / max(1e-6, abs(xs[1] - xs[0]))
    sy = area[3] / max(1e-6, abs(ys[1] - ys[0]))
    sc = min(sx, sy)
    cx = area[0] + area[2] / 2 - sc * (xs[0] + xs[1]) / 2
    cy = area[1] + area[3] / 2 - sc * (ys[0] + ys[1]) / 2
    P = lambda lo, la: (cx + sc * project(f, lo, la, view)[0], cy + sc * project(f, lo, la, view)[1])
    vis = lambda x, y: -200 < x < f.W + 200 and -200 < y < f.H + 200

    land = S.layer("layer.newShape", kind="none", name="land")
    hil = S.layer("layer.newShape", kind="none", name="highlight")
    nland = nhl = 0
    for iso, c in world.items():
        for r in c["r"]:
            if r["h"]:
                continue
            xy = clip_poly([P(lo, la) for lo, la in r["p"]], (area[0], area[1], area[0] + area[2], area[1] + area[3]))
            if len(xy) < 3:
                continue
            if iso.upper() in hl:
                S.cmd("shape.newPath", layer=hil, vertices=[[round(x, 1), round(y, 1)] for x, y in xy], closed=True,
                      fill=p["accent"], stroke=p["bg"], strokeWidth=1.5, space="comp")
                nhl += 1
            else:
                S.cmd("shape.newPath", layer=land, vertices=[[round(x, 1), round(y, 1)] for x, y in xy], closed=True,
                      fill=p["panel"], stroke=p["bg"], strokeWidth=1.5, space="comp")
                nland += 1
    S.span(land, t0, t1)
    S.expr(land, "transform/opacity", S.fade_expr(t0 + 0.1, t1))
    S.span(hil, t0, t1)
    S.expr(hil, "transform/opacity", "Math.min(easeOut(time,%.3f,%.3f,0,100),easeIn(time,%.3f,%.3f,100,0))" % (t0 + 0.9, t0 + 1.6, t1 - 0.3, t1))
    k = 0
    for r in routes:
        a, c = P(*r["from"]), P(*r["to"])
        mid = ((a[0] + c[0]) / 2, (a[1] + c[1]) / 2 - math.hypot(c[0] - a[0], c[1] - a[1]) * 0.25)
        arc = [((1 - u) ** 2 * a[0] + 2 * (1 - u) * u * mid[0] + u * u * c[0],
                (1 - u) ** 2 * a[1] + 2 * (1 - u) * u * mid[1] + u * u * c[1]) for u in [i / 24 for i in range(25)]]
        S.poly(arc, p["accent2"], f.s(6, 7), t0 + 1.6 + k * 0.7, t1, draw=(0, 1.2), name="route")
        k += 1
    for j, q in enumerate(pins):
        x, y = P(q["lon"], q["lat"])
        a = t0 + 1.4 + j * 0.5
        S.dot(x, y, f.s(11, 13), p["fg"], a, t1, pulse=True, name="pin")
        if q.get("label"):
            left = x > f.W * 0.62
            S.text(q["label"], x + (-290 if left else 22), y - 20, 270, f.s(30, 32), p["fg"], a + 0.2, t1, role="bold",
                   just="right" if left else "left", rise=0, h=44)
    S.lines.append("// map: %d land rings, %d highlighted rings" % (nland, nhl))


def beat_steps(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    steps = d.get("steps", [])
    n = max(1, len(steps))
    top = title_at(S, b, t0, t1)
    avail_w = f.W - 2 * f.mx
    if not f.tall:
        colw = avail_w / n
        y = f.H * 0.38
        S.poly([(f.mx + 30, y + 30), (f.W - f.mx - colw + 30, y + 30)], p["grid"], 4, t0 + 0.5, t1, draw=(0, 0.8 + n * 0.5), cap=0)
        for i, st in enumerate(steps):
            x = f.mx + i * colw
            a = t0 + 0.7 + i * (t1 - t0 - 2.2) / n
            S.dot(x + 30, y + 30, 30, p["accent"], a, t1)
            S.text(str(i + 1), x, y + 8, 60, 38, p["bg"], a + 0.1, t1, role="bold", just="center", rise=0, h=46)
            S.text(st["title"], x, y + 84, colw - 40, 58, p["fg"], a + 0.2, t1, role="head", rise=20)
            if st.get("text"):
                S.text(st["text"], x, y + 84 + S.nlines(st["title"], 58, colw - 40, 0.58) * 72 + 12, colw - 40, 38, p["mute"], a + 0.5, t1, rise=14)
    else:
        rowH = min(340, (f.H - top - 520) / n)
        y = top + 20
        for i, st in enumerate(steps):
            a = t0 + 0.7 + i * (t1 - t0 - 2.2) / n
            S.dot(y and f.mx + 34, y + 34, 34, p["accent"], a, t1)
            S.text(str(i + 1), f.mx + 4, y + 10, 60, 42, p["bg"], a + 0.1, t1, role="bold", just="center", rise=0, h=50)
            if i < n - 1:
                S.poly([(f.mx + 34, y + 76), (f.mx + 34, y + rowH + 0)], p["grid"], 4, a + 0.2, t1, draw=(0, 0.6), cap=0)
            S.text(st["title"], f.mx + 110, y + 2, avail_w - 110, 64, p["fg"], a + 0.2, t1, role="head", rise=18)
            if st.get("text"):
                S.text(st["text"], f.mx + 110, y + 90, avail_w - 110, 42, p["mute"], a + 0.5, t1, rise=12)
            y += rowH


def beat_timeline(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    ev = d.get("events", [])
    n = max(1, len(ev))
    top = title_at(S, b, t0, t1)
    if not f.tall:
        y = f.H * 0.5
        S.poly([(f.mx, y), (f.W - f.mx, y)], p["fg"], 5, t0 + 0.4, t1, draw=(0, 1.2 + n * 0.45), cap=0)
        colw = (f.W - 2 * f.mx) / n
        for i, e in enumerate(ev):
            x = f.mx + i * colw + 12
            a = t0 + 0.8 + i * (1.2 + n * 0.45) / n
            S.dot(x, y, 15, p["accent"], a, t1)
            up = i % 2 == 0
            S.text(str(e["when"]), x - 12, y - 150 if up else y + 36, colw + 60, 76, p["accent"], a + 0.1, t1, role="head", rise=14, h=80)
            S.text(e["text"], x - 12, y - 60 if up else y + 124, colw * 1.6 - 20, 34, p["fg"], a + 0.3, t1, rise=14)
    else:
        x = f.mx + 30
        y = top + 30
        step = min(360, (f.H - top - 560) / n)
        S.poly([(x, y), (x, y + step * (n - 1) + 10)], p["fg"], 5, t0 + 0.4, t1, draw=(0, 1.2 + n * 0.45), cap=0)
        for i, e in enumerate(ev):
            a = t0 + 0.8 + i * (1.2 + n * 0.45) / n
            yy = y + i * step
            S.dot(x, yy, 16, p["accent"], a, t1)
            S.text(str(e["when"]), x + 50, yy - 44, 700, 72, p["accent"], a + 0.1, t1, role="head", rise=12, h=70)
            S.text(e["text"], x + 50, yy + 44, f.W - x - 50 - f.mx, 42, p["fg"], a + 0.3, t1, rise=12)


def beat_compare(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    top = title_at(S, b, t0, t1)
    sides = [d.get("left", {}), d.get("right", {})]
    gap = 40
    if not f.tall:
        pw = (f.W - 2 * f.mx - gap) / 2
        py, ph = top + 20, f.H - top - 380
        boxes = [(f.mx + i * (pw + gap), py, pw, ph) for i in range(2)]
    else:
        pw = f.W - 2 * f.mx
        ph = (f.H - top - 760) / 2
        boxes = [(f.mx, top + 20 + i * (ph + gap), pw, ph) for i in range(2)]
    for i, (sd, (x, y, w, h)) in enumerate(zip(sides, boxes)):
        a = t0 + 0.5 + i * 0.8
        col = p["accent"] if i == 0 else p["accent2"]
        S.rect(x, y, w, h, p["panel"], a, t1, name="panel")
        S.rect(x, y, 10, h, col, a + 0.1, t1, name="edge")
        S.text(sd.get("label", ""), x + 44, y + 36, w - 80, 34, p["mute"], a + 0.2, t1, role="mono", rise=10, caps=True, h=44)
        vsize = f.s(150, 130)
        S.text(str(sd.get("value", "")), x + 44, y + 100, w - 80, vsize, col, a + 0.3, t1, role="head", rise=24, h=vsize * 1.2, pop=8)
        if sd.get("note"):
            S.text(sd["note"], x + 44, y + 100 + vsize * 1.25, w - 88, f.s(36, 40), p["fg"], a + 0.7, t1, rise=12)
    if d.get("verdict"):
        vy = boxes[-1][1] + boxes[-1][3] + f.s(36, 30)
        S.text(d["verdict"], f.mx, vy, f.W - 2 * f.mx, f.s(52, 58), p["accent"], t1 - (t1 - t0) * 0.45, t1, role="head", rise=18, h=130)


def beat_quote(S, b):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    w = f.W - 2 * f.mx
    size = f.s(92, 88)
    h = S.nlines(d.get("text", ""), size, w - 40, 0.58) * size * 1.25
    y = (f.H - h) / 2 - 40
    S.text("\u201c", f.mx - 6, y - f.s(210, 230), 300, 300, p["accent"], t0 + 0.2, t1, role="head", rise=0, h=330)
    S.text(d.get("text", ""), f.mx, y, w, size, p["fg"], t0 + 0.5, t1, role="head", rise=30, h=h)
    if d.get("who"):
        S.text("\u2014 " + d["who"], f.mx, y + h + 40, w, f.s(36, 40), p["mute"], t0 + 1.6, t1, role="mono", rise=10, h=46)


def beat_outro(S, b, plan):
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    w = f.W - 2 * f.mx
    size = f.s(96, 90)
    head, emph = clean_emph(d.get("takeaway", ""))
    h = S.nlines(head, size, w, 0.6) * size * 1.2
    y = f.s(220, 380)
    S.text(head, f.mx, y, w, size, p["fg"], t0 + 0.3, t1, role="head", rise=36, h=h, emph=emph)
    S.poly([(f.mx, y + h + 24), (f.mx + 300, y + h + 24)], p["accent"], 10, t0 + 0.4, t1, draw=(1.0, 0.7))
    yy = y + h + 80
    if d.get("cta"):
        S.text(d["cta"], f.mx, yy, w, f.s(46, 48), p["accent"], t0 + 1.4, t1, role="bold", rise=16)
        yy += f.s(100, 110)
    srcs = []
    for bb in plan.spec["beats"]:
        s = bb.get("source")
        if s and s != "none":
            lab = s if isinstance(s, str) else s.get("label", "")
            if lab not in srcs:
                srcs.append(lab)
    if srcs and d.get("show_sources", True):
        txt = "SOURCES\n" + "\n".join(srcs[:6])
        S.text(txt, f.mx, f.H - f.s(160, 470) - 30 * min(6, len(srcs)), w, f.s(22, 26), p["mute"], t0 + 2.0, t1, role="mono", rise=0,
               h=40 * (min(6, len(srcs)) + 1))


def beat_touchgrid(S, b):
    """Mechanism diagram: a sensor grid, a finger touch, signal change at each crossing, and the located point."""
    f, p = S.f, S.p
    d = b.get("data", {})
    t0, t1 = b["_t0"], b["_t1"]
    cols, rows = int(d.get("cols", 8)), int(d.get("rows", 5))
    tc, tr = d.get("touch", [cols * 0.6, rows * 0.45])
    top = title_at(S, b, t0, t1)
    cap = f.s(210, 470)
    # panel for the grid, text strip below (wide: right side)
    if f.tall:
        gx0, gx1 = f.mx + 20, f.W - f.mx - 20
        gy0, gy1 = top + 70, top + 70 + 560
    else:
        gx0, gx1 = f.mx + 20, f.W * 0.64
        gy0, gy1 = top + 70, f.H - cap - 40
    X = lambda c: gx0 + (gx1 - gx0) * c / (cols - 1)
    Y = lambda r: gy0 + (gy1 - gy0) * r / (rows - 1)
    a = t0 + 0.5
    for r in range(rows):
        S.poly([(X(0) - 30, Y(r)), (X(cols - 1) + 30, Y(r))], p["accent2"], f.s(5, 6), a + r * 0.1, t1, draw=(0, 0.9), cap=0, name="row-wire")
    for c in range(cols):
        S.poly([(X(c), Y(0) - 30), (X(c), Y(rows - 1) + 30)], p["mute"], f.s(5, 6), a + 0.6 + c * 0.08, t1, draw=(0, 0.9), cap=0, name="col-wire")
    touch_t = t0 + max(2.6, (t1 - t0) * 0.35)
    fx, fy = X(tc), Y(tr)
    spacing = (gx1 - gx0) / (cols - 1)
    best = None
    for r in range(rows):
        for c in range(cols):
            dist = math.hypot(c - tc, r - tr)
            if best is None or dist < best[0]:
                best = (dist, c, r)
            L = S.layer("layer.newShape", kind="ellipse", size=[f.s(22, 26)] * 2, fill=p["fg"], position=[X(c), Y(r)], name="node")
            S.span(L, a + 0.9, t1)
            k = math.exp(-dist / 1.3)
            S.expr(L, "transform/opacity", "easeOut(time,%.3f,%.3f,0,100)*easeIn(time,%.3f,%.3f,1,0)" % (a + 0.9, a + 1.3, t1 - 0.3, t1))
            S.expr(L, "transform/scale", "100+easeOut(time,%.3f,%.3f,0,%.1f)" % (touch_t, touch_t + 0.8, 340 * k))
            S.expr(L, "effects", "0") if False else None
    # finger: soft disc with repeating ripples
    F = S.layer("layer.newShape", kind="ellipse", size=[spacing * 2.2] * 2, fill=p["accent"], position=[fx, fy], name="finger", fillOpacity=40)
    S.span(F, touch_t, t1)
    S.expr(F, "transform/scale", "var s=easeOut(time,%.3f,%.3f,40,100);[s,s]" % (touch_t, touch_t + 0.5))
    S.expr(F, "transform/opacity", "Math.min(easeOut(time,%.3f,%.3f,0,100),easeIn(time,%.3f,%.3f,100,0))" % (touch_t, touch_t + 0.4, t1 - 0.3, t1))
    for j in range(2):
        R_ = S.layer("layer.newShape", kind="ellipse", size=[spacing * 2.2] * 2, fill=p["accent"], position=[fx, fy], name="ripple", fillOpacity=18)
        S.span(R_, touch_t + 0.3, t1)
        off = j * 0.9
        S.expr(R_, "transform/scale", "var q=((time-%.3f+%.1f)%%1.8)/1.8;var s=100+q*180;[s,s]" % (touch_t + 0.3, off))
        S.expr(R_, "transform/opacity", "var q=((time-%.3f+%.1f)%%1.8)/1.8;(1-q)*60" % (touch_t + 0.3, off))
    # found marker
    _, bc, br = best
    fa = touch_t + 1.6
    S.dot(X(bc), Y(br), f.s(34, 40), p["fg"], fa, t1, pulse=False, name="found")
    ring = S.layer("layer.newShape", kind="ellipse", size=[f.s(90, 100)] * 2, fill=p["bg"], position=[X(bc), Y(br)], name="found-ring", fillOpacity=0)
    S.cmd("shape.fillStroke", layers=[ring], fillType="none", stroke=p["fg"], strokeWidth=f.s(6, 7))
    S.span(ring, fa, t1)
    S.expr(ring, "transform/opacity", S.fade_expr(fa, t1, 0.3, 0.3))
    # step captions
    labs = d.get("labels", ["Grid holds a steady field", "Finger steals charge", "Chip finds the biggest change"])
    times = [a + 0.9, touch_t, fa]
    if f.tall:
        ly = gy1 + 90
        for i, lab in enumerate(labs[:3]):
            S.text("%d  %s" % (i + 1, lab), f.mx, ly + i * 120, f.W - 2 * f.mx, 40, p["fg"] if i == 2 else p["mute"], times[i], t1, role="bold", rise=14, h=60)
    else:
        lx = gx1 + 90
        for i, lab in enumerate(labs[:3]):
            S.text("%d" % (i + 1), lx, gy0 + 30 + i * 190, 80, 90, p["accent"], times[i], t1, role="head", rise=14, h=100)
            S.text(lab, lx + 80, gy0 + 40 + i * 190, f.W - lx - 80 - f.mx, 46, p["fg"], times[i], t1, role="bold", rise=14, h=130)


def beat_raw(S, b):
    """Escape hatch: data.jsx_file is EffectCraft script (After Effects style JS + app.run) added to the scene.
    Variables available: T0, T1 (beat start/end seconds), W, H. Keep every layer inside T0..T1."""
    d = b.get("data", {})
    path = d.get("jsx_file")
    S.lines.append("var T0=%r,T1=%r,W=%d,H=%d;" % (b["_t0"], b["_t1"], S.f.W, S.f.H))
    S.lines.append(open(os.path.join(S.base_dir, path)).read())


BEATS = dict(hook=beat_hook, kinetic=beat_kinetic, stat=beat_stat, bars=beat_bars, line=beat_line, map=beat_map,
             steps=beat_steps, timeline=beat_timeline, compare=beat_compare, quote=beat_quote, touchgrid=beat_touchgrid, raw=beat_raw)
FACT_TYPES = {"stat", "bars", "line", "map", "compare", "timeline"}


def wipe(S, t0):
    f, p = S.f, S.p
    L = S.layer("layer.newShape", kind="rect", size=[f.W * 1.2, f.H], fill=p["accent"], position=[f.W / 2, f.H / 2], name="wipe")
    S.span(L, t0 - 0.25, t0 + 0.55)
    S.expr(L, "transform/position", "[easeOut(time,%.3f,%.3f,%d,%d),value[1]]" % (t0 - 0.25, t0 + 0.55, -f.W * 0.6, f.W * 1.7))
    return L


def build_scene(plan, kind, out_dir, name):
    spec = plan.spec
    f = Fmt(kind)
    pal = dict(PALETTES.get(spec.get("style", "paper"), PALETTES["paper"]))
    pal.update(spec.get("colors", {}))
    S = Scene(f, pal, spec.get("fps", 30), spec.get("fonts"))
    S.base_dir = plan.dir
    S.lines.append("// generated by ecx.py - do not edit, change the spec instead")
    S.cmd("comp.new", name="Main", width=f.W, height=f.H, frameRate=spec.get("fps", 30), duration=round(plan.total + 0.5, 2),
          background=pal["bg"])
    for b in plan.beats:
        t0, t1 = b["_t0"], b["_t1"]
        backdrop(S, b)
        if b["type"] == "outro":
            beat_outro(S, b, plan)
        else:
            BEATS[b["type"]](S, b)
        chrome(S, b, plan)
        if b["_i"] > 0:
            wipe(S, t0)
    # progress bar
    S.poly([(0, f.H - 6), (f.W, f.H - 6)], pal["accent"], 10, 0, plan.total + 0.5, draw=None, keep=True, name="progress", cap=0,
           trim_expr="linear(time,0,%.2f,0,100)" % plan.total)
    # audio
    for b in plan.beats:
        if b["_audio"]:
            S.cmd("file.import", paths=[os.path.abspath(b["_audio"])])
            S.cmd("layer.addItem", item=os.path.basename(b["_audio"]), time=round(b["_t0"] + 0.3, 3))
    music = spec.get("music")
    if music and os.path.exists(os.path.join(plan.dir, music)):
        S.cmd("file.import", paths=[os.path.abspath(os.path.join(plan.dir, music))])
        M = S.layer("layer.addItem", item=os.path.basename(music), time=0)
        S.cmd("prop.set", layer=M, path="audio/audioLevels", value=[spec.get("music_db", -22)] * 2)
    jsx = "\n".join(S.lines) + "\n"
    path = os.path.join(out_dir, "%s_%s.jsx" % (name, kind))
    open(path, "w").write(jsx)
    return path


# ----------------------------------------------------------------- CLI plumbing
def find_cli():
    cands = [os.environ.get("EFFECTCRAFT_CLI"), shutil.which("effectcraft-cli")]
    cands += ["/Applications/EffectCraft.app/Contents/MacOS/effectcraft-cli",
              "/Applications/EffectCraft.app/Contents/Resources/effectcraft-cli",
              os.path.expanduser("~/Applications/EffectCraft.app/Contents/MacOS/effectcraft-cli"),
              os.path.expanduser("~/bin/effectcraft-cli"), "/usr/local/bin/effectcraft-cli",
              r"C:\Program Files\ArtCraft\EffectCraft\effectcraft-cli.exe",
              os.path.expandvars(r"%LOCALAPPDATA%\Programs\ArtCraft\EffectCraft\effectcraft-cli.exe")]
    for c in cands:
        if c and os.path.exists(c):
            return c
    hits = glob.glob(os.path.expanduser("~/**/effectcraft-cli"), recursive=False)
    return hits[0] if hits else None


def need_cli():
    c = find_cli()
    if not c:
        sys.exit("EffectCraft CLI not found. Install EffectCraft (free): https://getartcraft.com/apps/effectcraft , "
                 "then set EFFECTCRAFT_CLI=/full/path/to/effectcraft-cli (macOS: download the 'effectcraft-cli' zip "
                 "from the GitHub releases page and unzip it).")
    return c


def load_spec(path):
    spec = json.load(open(path))
    return spec, os.path.dirname(os.path.abspath(path))


def strings(o):
    if isinstance(o, str):
        return [o]
    if isinstance(o, dict):
        return [x for k, v in o.items() if k != "jsx_file" for x in strings(v)]
    if isinstance(o, list):
        return [x for v in o for x in strings(v)]
    return []


def problems(spec):
    errs, warns = [], []
    ids = set()
    if not spec.get("beats"):
        errs.append("spec has no beats")
    for i, b in enumerate(spec.get("beats", [])):
        bid = b.get("id", "?")
        if bid in ids:
            errs.append("duplicate beat id %s" % bid)
        ids.add(bid)
        if b.get("type") not in list(BEATS) + ["outro"]:
            errs.append("beat %s: unknown type %r (use: %s)" % (bid, b.get("type"), ", ".join(list(BEATS) + ["outro"])))
            continue
        src = b.get("source")
        if b["type"] in FACT_TYPES and not src:
            errs.append("beat %s (%s) shows facts and needs a \"source\"." % (bid, b["type"]))
        if b["type"] in FACT_TYPES - {"compare", "timeline"} and src == "none":
            errs.append("beat %s (%s) shows data, so \"source\":\"none\" is not allowed. Source it or remove it." % (bid, b["type"]))
        if (not src or src == "none"):
            blob = " ".join(strings(b.get("data", {}))) + " " + b.get("vo", "") + " " + b.get("title", "")
            if re.search(r"\d", blob):
                errs.append("beat %s has numbers or dates but no real source. Source the claim or remove it. Do not relabel a factual claim to get around this check." % bid)
            elif src == "none":
                warns.append("beat %s is marked source none: confirm it contains no factual claims (names, dates, statistics, causal claims about the world) a viewer could check" % bid)
        if b["type"] != "outro" and not b.get("vo"):
            warns.append("beat %s has no narration text (vo); it will run for its minimum length" % bid)
        n = len(words(b.get("vo", "")))
        if n > 70:
            warns.append("beat %s narration is %d words; consider splitting into two beats" % (bid, n))
    return errs, warns


def sources_md(spec):
    out = ["# Sources\n"]
    for b in spec.get("beats", []):
        s = b.get("source")
        if s and s != "none":
            lab = s if isinstance(s, str) else s.get("label", "")
            url = "" if isinstance(s, str) else s.get("url", "")
            out.append("- **%s** (%s): %s %s" % (b["id"], b["type"], lab, url))
    return "\n".join(out) + "\n"


def cmd_check(a):
    spec, d = load_spec(a.spec)
    errs, warns = problems(spec)
    plan = Plan(spec, d)
    for w in warns:
        print("warn:", w)
    for e in errs:
        print("ERROR:", e)
    print("total length about %.1fs over %d beats" % (plan.total, len(plan.beats)))
    print("NOTE: check verifies that sources are PRESENT, not that they are true. Open each source and confirm the claim.")
    open(os.path.join(d, "sources.md"), "w").write(sources_md(spec))
    return 1 if errs else 0


def cmd_doctor(a):
    c = find_cli()
    print("EffectCraft CLI:", c or "NOT FOUND (see SKILL.md, setup)")
    if c:
        r = subprocess.run([c, "info", "--json"], capture_output=True, text=True)
        print("  runs headless:", "yes" if r.returncode == 0 else "NO " + r.stderr[:200])
    print("ffprobe:", shutil.which("ffprobe") or "no (only wav narration lengths can be read)")
    for n in ("piper", "say", "espeak-ng"):
        print("voice engine %-9s:" % n, shutil.which(n) or "no")
    print("python:", sys.version.split()[0])
    return 0


def run_voice_engine(engine, text, out, voice=None):
    if engine == "say":
        cmd = ["say"] + (["-v", voice] if voice else []) + ["-o", out, "--data-format=LEI16@22050", text]
        subprocess.run(cmd, check=True)
    elif engine == "piper":
        model = voice or os.environ.get("ECX_PIPER_MODEL")
        if not model:
            sys.exit("piper needs a voice model: set ECX_PIPER_MODEL=/path/en_US-lessac-medium.onnx")
        subprocess.run(["piper", "--model", model, "--output_file", out], input=text, text=True, check=True)
    elif engine == "espeak-ng":
        subprocess.run(["espeak-ng", "-s", "160"] + (["-v", voice] if voice else []) + ["-w", out, text], check=True)
    else:
        sys.exit("unknown voice engine " + engine)


def cmd_voice(a):
    spec, d = load_spec(a.spec)
    v = spec.get("voice", {}) or {}
    eng = a.engine or v.get("engine", "auto")
    if eng == "auto":
        eng = next((e for e in ("piper", "say", "espeak-ng") if shutil.which(e)), None)
    if not eng:
        print("No free voice engine found. Options: macOS 'say' (built in), Piper (free, offline), eSpeak-NG, or record "
              "your own voice and drop per-beat WAVs into vo/<beat id>.wav. Nothing was generated.")
        return 1
    os.makedirs(os.path.join(d, "vo"), exist_ok=True)
    for b in spec["beats"]:
        if not b.get("vo"):
            continue
        out = os.path.join(d, "vo", b["id"] + ".wav")
        if os.path.exists(out) and not a.force:
            print("keep", out)
            continue
        run_voice_engine(eng, b["vo"], out, v.get("voice"))
        print("made", out, audio_len(out))
    return 0


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.stderr.write((r.stdout + r.stderr)[-1500:] + "\n")
        sys.exit("command failed: " + " ".join(cmd[:4]))
    return r


def cmd_build(a):
    cli = need_cli()
    spec, d = load_spec(a.spec)
    errs, warns = problems(spec)
    for w in warns:
        print("warn:", w)
    if errs:
        for e in errs:
            print("ERROR:", e)
        return 1
    only = a.beats.split(",") if a.beats else None
    plan = Plan(spec, d, only)
    out = a.out or os.path.join(d, "out")
    os.makedirs(out, exist_ok=True)
    name = re.sub(r"[^a-zA-Z0-9_-]+", "-", spec.get("name", "explainer")).strip("-")
    fmt = a.format or spec.get("format", "both")
    kinds = ["wide", "tall"] if fmt == "both" else [fmt]
    for kind in kinds:
        jsx = build_scene(plan, kind, out, name)
        proj = os.path.join(out, "%s_%s.ecproj" % (name, kind))
        if os.path.exists(proj):
            os.remove(proj)
        r = run([cli, "script", jsx, "--save-as", proj])
        print("built", proj)
        if not a.no_stills:
            sd = os.path.join(out, "stills_" + kind)
            os.makedirs(sd, exist_ok=True)
            for b in plan.beats:
                for lab, frac in (("a", 0.45), ("b", 0.85)):
                    t = b["_t0"] + (b["_t1"] - b["_t0"]) * frac
                    run([cli, "render-frame", proj, "--time", "%.2f" % t, "--out",
                         os.path.join(sd, "%02d_%s_%s.png" % (b["_i"] + 1, b["id"], lab)), "--max-side", "960"])
            print("stills ->", sd)
        if a.render:
            mp4 = os.path.join(out, "%s_%s.mp4" % (name, kind))
            run([cli, "render", proj, "--comp", "Main", "--out", mp4, "--format", "h264", "--audio", "on"] + (["--bitrate", str(a.bitrate)] if a.bitrate else []))
            print("rendered", mp4)
    open(os.path.join(out, "sources.md"), "w").write(sources_md(spec))
    print("total length about %.1fs. Sources list: %s" % (plan.total, os.path.join(out, "sources.md")))
    return 0


def cmd_new(a):
    dst = os.path.abspath(a.name)
    os.makedirs(dst, exist_ok=True)
    src = os.path.join(HERE, "..", "templates", "starter.spec.json")
    shutil.copy(src, os.path.join(dst, "spec.json"))
    print("created", os.path.join(dst, "spec.json"))
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="c", required=True)
    sub.add_parser("doctor").set_defaults(fn=cmd_doctor)
    s = sub.add_parser("new"); s.add_argument("name"); s.set_defaults(fn=cmd_new)
    s = sub.add_parser("check"); s.add_argument("spec"); s.set_defaults(fn=cmd_check)
    s = sub.add_parser("voice"); s.add_argument("spec"); s.add_argument("--engine"); s.add_argument("--force", action="store_true"); s.set_defaults(fn=cmd_voice)
    s = sub.add_parser("build"); s.add_argument("spec"); s.add_argument("--format", choices=["wide", "tall", "both"])
    s.add_argument("--beats"); s.add_argument("--render", action="store_true"); s.add_argument("--out"); s.add_argument("--no-stills", action="store_true"); s.add_argument("--bitrate", type=int, help="video kbps for render")
    s.set_defaults(fn=cmd_build)
    a = ap.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
