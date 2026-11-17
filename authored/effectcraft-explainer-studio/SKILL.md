---
name: effectcraft-explainer-studio
description: Turn a topic into a researched, narrated, editorial explainer video (16:9 for YouTube and 9:16 for Reels/Shorts) rendered entirely in EffectCraft. Use when the user asks for an explainer, "explain how X works" video, a data story, a map or chart animation, or a faceless motion-graphics reel, and wants it free and made with EffectCraft.
---

# EffectCraft Explainer Studio

An original workflow. You write one beat sheet (JSON). `scripts/ecx.py` turns it into an EffectCraft project
and renders 16:9 and 9:16 videos from it. No paid tools, no API keys, Python standard library only.

Inspired by the public behavior of "explain how X works" reel skills. It shares no code, text or art with any
paid product.

## The twist: Receipts + One Script, Two Cuts

1. **Receipts.** Every beat that shows a fact (stat, bars, line, map, compare, timeline) must carry a `source`.
   Any beat of any type whose text contains numbers or dates also needs one. `ecx.py check` refuses to build
   otherwise. The source shows as a small tag on screen, and the outro lists every source. A `sources.md` is
   written next to the video. `check` only verifies that a source is PRESENT, not that it is true: open each
   source and confirm the claim yourself. `"source":"none"` is only for questions, transitions and pure
   explanation with no checkable claim. Never move an unsourced fact into a kinetic, quote or hook beat or
   mark it `none` to get past the check: source it or cut it.
2. **One script, two cuts.** The same beats render as 16:9 and 9:16. Layout reflows (vertical lists, bigger
   type, captions in the safe zone). `--beats id1,id2` cuts a short from a long script.
3. **Chapter wipes.** Each beat starts with a color wipe and a big faint chapter number. It reads as editorial,
   not as a slideshow.

## Setup (you, the AI agent, do this; the user does not)

1. Run `python3 scripts/ecx.py doctor` yourself. If the EffectCraft CLI is found and "runs headless: yes", go on.
2. If it is missing, tell the user once, in plain words, what you will download and install (EffectCraft is
   free, https://getartcraft.com/apps/effectcraft ; the CLI zip `effectcraft-cli-<version>-macos-universal.zip` is
   on https://github.com/storytold/effectcraft/releases ) and where. Ask one yes/no. After a yes, download,
   unzip, set `EFFECTCRAFT_CLI`, and rerun `doctor`. Do not hand the user a list of steps.
3. Voice: on macOS prefer the built-in `say` (no install). Otherwise ask once before installing Piper
   (`pip install piper-tts` plus a free voice model) and set `ECX_PIPER_MODEL`. Or use the user's own recordings
   as `vo/<beat id>.wav`. Details and licence cautions: `references/voice.md`.
4. Install or download nothing else, and spend nothing.

## Workflow (do these in order)

1. **Brief.** Ask only what is missing: topic, audience, length (default 45-75s short, 3-6 min long), format
   (default both), look (`paper` light editorial, `ink` dark, `signal` navy and yellow).
2. **Research for receipts.** Find every number from a primary or named source. Write the source label and URL
   down as you go. Never invent a statistic. If you cannot source it, make it a `kinetic` or `quote` beat with
   `"source":"none"` and phrase it as opinion, or cut it.
3. **Write the story first.** Read `references/storytelling.md`. One idea per beat. Hook in the first 2 seconds.
   Narration is `vo`, written to be heard (short sentences, no parentheses, numbers spelled the way you say them).
4. **Write the beat sheet.** Copy `templates/starter.spec.json` (or `python3 scripts/ecx.py new myvideo`). Field
   reference is in `references/spec.md`. Beat types: hook, kinetic, stat, bars, line, map, steps, timeline,
   compare, quote, outro, touchgrid, raw.
5. **Check.** `python3 scripts/ecx.py check spec.json`. Fix every ERROR and read every warning.
6. **Voice.** `python3 scripts/ecx.py voice spec.json`. Listen to at least the hook. Timing is measured from
   the real audio, so beats stretch to fit the voice.
7. **Preview.** `python3 scripts/ecx.py build spec.json` makes the projects and two stills per beat in
   `out/stills_wide` and `out/stills_tall`. LOOK at them (open each image). Use the QA list in
   `references/qa.md`. Fix text that collides, wraps badly or is too small, then rebuild. A build takes seconds.
8. **Render.** `python3 scripts/ecx.py build spec.json --render` writes `out/<name>_wide.mp4` and
   `out/<name>_tall.mp4` with narration. Render one format at a time with `--format wide` / `--format tall` for
   long videos so a tool timeout cannot cut a render off. Speed depends on the machine: one 49 s video took about
   75 s per format on the author's Linux test box; measure your own.
9. **Deliver** the mp4s, `sources.md`, and a 2-line honest note on anything you could not check.

You can also open `out/*.ecproj` in the EffectCraft app and polish by hand. Rebuilding overwrites those files,
so copy them first.

## Rules that keep it professional

- Max one idea and about 35 words of narration per beat. Split long beats.
- Never put more than 4 bars, 8 line points, 5 steps or 6 timeline events in one beat.
- Accent color marks the one thing to look at. Use `*asterisks*` around the key words in headlines.
- Do not ask the user for API keys. Do not use paid fonts, stock footage or music. Bundled fonts are Inter,
  Noto Serif, JetBrains Mono. For music use only files the user owns or that are public domain / CC0, and say where from.
- Never claim sync you did not verify. Captions here are evenly spread across each beat's narration, not
  word-aligned. Say so if the user asks.

## What this can and cannot do (be honest with the user)

It makes clean editorial explainers: animated type, charts that draw on, maps with pins and routes, step and
timeline diagrams, a built-in animated mechanism diagram (`touchgrid`: sensor grid, finger, signal change, located
point), narration, captions and chapter wipes. It is NOT a cinematic character or 3D scene generator. A new
mechanism (for example a battery or a speaker) needs a `raw` beat written in EffectCraft script, which is real
work, or a new beat type added to `ecx.py`. Do not claim parity with any paid explainer product. Captions are
evenly timed, not word-synced. Maps are generalized.

## When a beat needs something custom

Use `type":"raw"` with a `jsx_file`. It runs EffectCraft script with `T0`, `T1`, `W`, `H` defined. Command names
and parameters: run `effectcraft-cli commands --filter <word>` and read `references/effectcraft-notes.md` first.

## Tested vs untested

See `references/qa.md`, section "What was verified". Read it before promising anything about macOS voices,
Windows paths, or very long videos.
