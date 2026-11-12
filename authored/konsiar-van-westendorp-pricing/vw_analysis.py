#!/usr/bin/env python3
"""
vw_analysis.py - Van Westendorp Price Sensitivity Meter analysis (stdlib only).

Reads a CSV of survey responses, one row per respondent, with four price
columns (too_cheap, cheap, expensive, too_expensive), validates them, builds
the cumulative-frequency curves exactly (as step functions over the observed
prices - no grid, no interpolation, so no outlier can compress the resolution
and no crossing is missed), and finds the intersections.

Threshold/tie convention (documented, applied uniformly):
  increasing ("cum") curves count thresholds <= p;
  decreasing ("inv") curves count thresholds strictly > p.
A respondent whose threshold is exactly p therefore counts toward the
expensive-side curve and not toward the cheap-side curve at p. This makes
  not_cheap(p)     == 1 - cheap_inv(p)        exactly, and
  not_expensive(p) == 1 - expensive_cum(p)    exactly,
i.e. the reversed curves are literal complements, as van Westendorp's
"reverse the graphs" step requires - including at tied prices.

Convention for range endpoints (two exist in the wild - they differ):

  "original" (default): van Westendorp's own 1976 definitions.
    PMC = "too cheap" x "not cheap"         (not cheap = cum of cheap)
    PME = "too expensive" x "not expensive" (not expensive = inv of expensive)
    IDP = "cheap" x "expensive"
    OPP = "too cheap" x "too expensive"
    Source: van Westendorp (1976), ESOMAR Congress paper; also the default
    (acceptable_range = "original") in the R pricesensitivitymeter package.

  "narrower" (--range-method narrower): used by some modern tools
  (Conjointly, Quantilope, Milieu):
    PMC = "too cheap" x "expensive"
    PME = "cheap" x "too expensive"
    IDP and OPP are the same in both.

Curves are step functions that only change at observed prices, so crossings
are found exactly at observed prices. When curves coincide over a stretch
(discrete data does this), the equality region is reported as an interval
[a, b): from the first observed price where they meet up to (excluding) the
next observed price, or "a and above" if they never separate again. Nothing
is collapsed to a midpoint and separate crossings are reported separately.

Usage:
  python3 vw_analysis.py responses.csv
  python3 vw_analysis.py responses.csv --range-method narrower
  python3 vw_analysis.py responses.csv --curves-out curves.csv
  python3 vw_analysis.py responses.csv --col-too-cheap q1 --col-cheap q4 ...

Only reports what the data supports. The intersections describe stated price
perception, not demand, revenue, or profit.
"""

import argparse
import csv
import math
import sys
from bisect import bisect_left, bisect_right

REQUIRED_ORDER = ("too_cheap", "cheap", "expensive", "too_expensive")
DEFAULT_COLS = {k: k for k in REQUIRED_ORDER}


def load_rows(path, cols):
    """Return (valid, rejected) lists. Rejected rows are (line_number, reason)."""
    valid, rejected = [], []
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = [c for c in cols.values() if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit("CSV is missing expected column(s): %s\nFound: %s"
                     % (", ".join(missing), ", ".join(reader.fieldnames or [])))
        for i, row in enumerate(reader, start=2):  # row 1 = header
            try:
                r = {k: float(row[c].strip()) for k, c in cols.items()}
            except (ValueError, AttributeError, TypeError):
                rejected.append((i, "non-numeric or missing value"))
                continue
            if not all(math.isfinite(v) for v in r.values()):
                rejected.append((i, "non-finite value (inf/nan)"))
                continue
            if any(v < 0 for v in r.values()):
                rejected.append((i, "negative price"))
                continue
            if not (r["too_cheap"] <= r["cheap"] <= r["expensive"] <= r["too_expensive"]):
                rejected.append((i, "violates too_cheap <= cheap <= expensive <= too_expensive"))
                continue
            valid.append(r)
    return valid, rejected


def build_curves(rows):
    """Exact step-function curves over observed knots.

    Returns (knots, curves) where curves[name] is a dict with:
      at:     value at each knot (cum: P(t <= k); inv: P(t > k))
      before: value just below each knot (cum: P(t < k); inv: P(t >= k))
    Between consecutive knots every curve is constant at its `at` value.
    """
    n = len(rows)
    vals = {k: sorted(r[k] for r in rows) for k in REQUIRED_ORDER}
    knots = sorted(set(v for vs in vals.values() for v in vs))

    def series(key, kind):
        v = vals[key]
        at, before = [], []
        for k in knots:
            le = bisect_right(v, k) / n
            lt = bisect_left(v, k) / n
            if kind == "cum":
                at.append(le)
                before.append(lt)
            else:  # inv
                at.append(1 - le)   # P(t > k)
                before.append(1 - lt)  # P(t >= k)
        return {"at": at, "before": before}

    curves = {
        "too_cheap_inv": series("too_cheap", "inv"),
        "cheap_inv": series("cheap", "inv"),
        "not_cheap": series("cheap", "cum"),
        "expensive_cum": series("expensive", "cum"),
        "not_expensive": series("expensive", "inv"),
        "too_expensive_cum": series("too_expensive", "cum"),
    }
    return knots, curves


def find_crossings(knots, a, b):
    """All crossings/touches of two step curves, as separate events.

    Returns a list of ("point", x) or ("interval", lo, hi) events. Curves are
    constant between knots, so crossings happen at knots (a step jumps the
    difference past zero) and equality plateaus are maximal runs of knots
    where the difference is zero. Nothing is merged or averaged.
    """
    m = len(knots)
    d_at = [a["at"][i] - b["at"][i] for i in range(m)]
    d_before = [a["before"][i] - b["before"][i] for i in range(m)]
    events = []
    i = 0
    while i < m:
        if d_at[i] == 0:
            j = i
            while j + 1 < m and d_at[j + 1] == 0:
                j += 1
            # d_at[k]==0 means equality on [k, next knot): the curves are
            # constant until the next knot, so the region extends right.
            hi = knots[j + 1] if j + 1 < m else None
            events.append(("interval", knots[i], hi))
            i = j + 1
        elif d_before[i] * d_at[i] < 0:
            events.append(("point", knots[i]))
            i += 1
        else:
            i += 1
    return events


def fmt_events(events):
    """Human strings for crossing events; empty list -> [None]."""
    if not events:
        return None
    out = []
    for e in events:
        if e[0] == "point":
            out.append("%.2f" % e[1])
        elif e[2] is None:
            out.append("%.2f and above (equality from here on)" % e[1])
        else:
            out.append("%.2f .. %.2f (equality interval, upper bound exclusive)"
                       % (e[1], e[2]))
    return out


def analyze(rows, range_method):
    knots, curves = build_curves(rows)
    if range_method == "original":
        pmc = find_crossings(knots, curves["too_cheap_inv"], curves["not_cheap"])
        pme = find_crossings(knots, curves["too_expensive_cum"], curves["not_expensive"])
        pairs = {"PMC": "too cheap x not cheap", "PME": "too expensive x not expensive"}
    else:
        pmc = find_crossings(knots, curves["too_cheap_inv"], curves["expensive_cum"])
        pme = find_crossings(knots, curves["too_expensive_cum"], curves["cheap_inv"])
        pairs = {"PMC": "too cheap x expensive", "PME": "cheap x too expensive"}
    pts = {
        "PMC": pmc,
        "OPP": find_crossings(knots, curves["too_cheap_inv"], curves["too_expensive_cum"]),
        "IDP": find_crossings(knots, curves["cheap_inv"], curves["expensive_cum"]),
        "PME": pme,
    }
    return knots, curves, pts, pairs


def main():
    ap = argparse.ArgumentParser(description="Van Westendorp PSM analysis")
    ap.add_argument("csv")
    ap.add_argument("--range-method", choices=["original", "narrower"],
                    default="original",
                    help="PMC/PME definition: van Westendorp 1976 (default) "
                         "or the narrower modern-tool variant")
    ap.add_argument("--curves-out", metavar="FILE",
                    help="write all six curves (values at observed prices) to CSV")
    for k in REQUIRED_ORDER:
        ap.add_argument("--col-" + k.replace("_", "-"), default=DEFAULT_COLS[k],
                        help="CSV column for %s" % k)
    args = ap.parse_args()

    cols = {k: getattr(args, "col_" + k) for k in REQUIRED_ORDER}
    rows, rejected = load_rows(args.csv, cols)
    if len(rows) < 2:
        sys.exit("Need at least 2 valid respondents; got %d." % len(rows))

    knots, curves, pts, pairs = analyze(rows, args.range_method)

    print("Van Westendorp analysis (range method: %s)" % args.range_method)
    print("  respondents: %d valid, %d rejected" % (len(rows), len(rejected)))
    if rejected:
        for line, why in rejected[:5]:
            print("    rejected row %d: %s" % (line, why))
        if len(rejected) > 5:
            print("    ... and %d more" % (len(rejected) - 5))
    print()
    labels = [
        ("PMC", "point of marginal cheapness (%s)" % pairs["PMC"]),
        ("OPP", "optimal price point (too cheap x too expensive)"),
        ("IDP", "indifference price point (cheap x expensive)"),
        ("PME", "point of marginal expensiveness (%s)" % pairs["PME"]),
    ]
    for key, desc in labels:
        ev = fmt_events(pts[key])
        print("  %-4s %s" % (key, desc))
        if ev is None:
            print("       no crossing in data")
        else:
            for s in ev:
                print("       %s" % s)
    print()
    pmc_ev, pme_ev = fmt_events(pts["PMC"]), fmt_events(pts["PME"])
    if pmc_ev and pme_ev:
        print("  acceptable price range:")
        print("    lower bound (PMC): %s" % "; ".join(pmc_ev))
        print("    upper bound (PME): %s" % "; ".join(pme_ev))
        if len(pmc_ev) + len(pme_ev) > 2:
            print("    multiple crossings - inspect the curves before")
            print("    quoting a single range.")
    else:
        print("  acceptable price range: not determinable "
              "(no crossing for %s)" %
              " and ".join(k for k, ev in (("PMC", pmc_ev), ("PME", pme_ev)) if not ev))
    print()
    print("  n=%d. Values are exact crossings of the cumulative step" % len(rows))
    print("  functions of stated thresholds; with small n they are still")
    print("  only as informative as the sample. These are stated price")
    print("  perceptions, not demand, revenue, or a profit-optimal price")
    print("  (van Westendorp: 'optimal' means least resistance, with 'no")
    print("  relation to the optimum-theory in economy').")

    if args.curves_out:
        keys = ("too_cheap_inv", "not_cheap", "cheap_inv",
                "expensive_cum", "not_expensive", "too_expensive_cum")
        with open(args.curves_out, "w", newline="") as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["price"] + list(keys))
            for i, k in enumerate(knots):
                w.writerow(["%.4f" % k] + ["%.6f" % curves[name]["at"][i] for name in keys])
        print("  curves written to %s (values at observed prices)" % args.curves_out)


if __name__ == "__main__":
    main()
