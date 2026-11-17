# EffectCraft Explainer Studio: original narrated explainer builder

## When to use
Turn a topic into a researched, narrated, editorial explainer video rendered entirely in EffectCraft: 16:9 for YouTube and 9:16 for Reels/Shorts from the same script. Use when you ask for an explainer, an "explain how X works" video, a data story, a map or chart animation, or a faceless motion-graphics reel, and want it free and made with EffectCraft.

This is an original skill written for this library on 16 November 2026, after you shared a reel demonstrating the paid Full Visual product (https://www.instagram.com/p/DfPQlVOgpH2/ , $99 at https://getkeyframes.com/products/full-visual). That product was not bought, downloaded or copied. This skill was built independently from its public on-screen behavior plus EffectCraft's official docs and CLI, and it shares no code, text, art or branding with it. No parity with the paid product is claimed.

## How to use
Read `authored/effectcraft-explainer-studio/SKILL.md`, then give Claude the topic, audience, length and format. For example:

> Use effectcraft-explainer-studio to make a 60-second explainer on how a touchscreen works, both 16:9 and 9:16. Research and source every fact, render through EffectCraft, and show me the preview stills before the final render. Ask me once before any install on my Mac; do not spend money.

The workflow: brief, sourced research, story, one JSON beat sheet, automated check, voice, preview stills you inspect, then render. You write one beat sheet; `scripts/ecx.py` builds an EffectCraft project and renders both formats with narration. Beat types include hook, kinetic type, counting stat, bars, line, map (bundled Natural Earth data with pins and route arcs), steps, timeline, compare, quote, chapter outro, an animated touchgrid mechanism diagram, and a raw EffectCraft-script escape hatch.

The twist, versus a plain explainer generator:
1. **Receipts.** Every beat that shows a fact must carry a source or the check refuses to build. Sources show on screen and are collected into the outro and a `sources.md`. The check verifies a source is present, not that it is true; the research step still has to open each source. Never relabel an unsourced fact as opinion or another beat type to pass: source it or cut it.
2. **One script, two cuts.** The same beats reflow for 16:9 and 9:16, and `--beats` cuts a short from a long script.
3. **Chapter wipes** with big faint chapter numbers for an editorial look. Looks: paper, ink, signal. Bundled fonts: Inter, Noto Serif, JetBrains Mono.

## What is included
The complete reviewed skill package is in `authored/effectcraft-explainer-studio/`:
- `SKILL.md`: the workflow, setup, rules and honesty limits.
- `scripts/ecx.py`: the builder (Python standard library only; `doctor`, `new`, `check`, `voice`, `build`).
- `references/`: storytelling, beat-sheet spec, EffectCraft CLI notes, voice setup, QA checklist.
- `templates/starter.spec.json` and `examples/data-demo.spec.json`: working beat sheets.
- `assets/world_110m.json`: Natural Earth 1:110m country outlines (public domain).
- `LICENSE`: MIT.

`packages/effectcraft-explainer-studio.zip` is the byte-exact reviewed package as delivered, for one-file download. `prepare_library.py` copies all of these files into one new library folder after checksum verification. No upstream repository is fetched for this entry; there is nothing to install by opening this library.

Entry 45 (EffectCraft Motion Films) is a separate directing/storytelling adaptation. This entry is an executable build-and-render pipeline; they do not depend on each other.

## Setup, cost and verification limits
Everything runs locally through the free, open-source EffectCraft CLI (https://github.com/storytold/effectcraft); the skill's `doctor` command checks for it, and the skill instructs Claude to ask you once before any download or install on your Mac. Voice uses the macOS built-in `say`, free Piper voices, or your own recordings. No paid API keys, fonts, stock footage or music. Music only from files you own or public domain/CC0, with the source stated.

Tested before publication: `check`, `build`, and real renders of both formats (1920x1080 and 1080x1920, h264+aac with narration) of a 49-second demo, using EffectCraft CLI 0.24.1 on Linux; about 75 seconds per format on that machine. Not yet tested: macOS and Windows paths and voices, long-form videos, and music. Captions are evenly timed across each beat, not word-synced. EffectCraft is alpha software; confirm installed capabilities and inspect the preview stills and rendered frames, which the workflow already requires.

This skill is not a cinematic character or 3D scene generator. A new mechanism beyond the bundled touchgrid diagram needs a raw EffectCraft-script beat or a new beat type in `ecx.py`, which is real work. Adding this entry is not permission to install anything, spend anything, or render on your device without your say.

## Attribution and rights
Original work for this library, MIT licensed (see the package LICENSE). Written from public product behavior and official EffectCraft documentation only; no paid or proprietary material was acquired or used. Map data: Natural Earth, public domain (https://www.naturalearthdata.com). EffectCraft itself is a separate project by Storytold; GitHub currently reports its license as Apache-2.0 and no separate LICENSE file was found, so recheck its repo before relying on redistribution terms. Inspired-by reference, not a source: Full Visual by Keyframes, https://getkeyframes.com/products/full-visual (paid, not acquired).

## Verified sources
- Skill package: `authored/effectcraft-explainer-studio/` in this repository (rendered proof inspected before publication).
- EffectCraft engine: https://github.com/storytold/effectcraft
- Natural Earth map data: https://www.naturalearthdata.com
- User-shared reel that prompted this skill: https://www.instagram.com/p/DfPQlVOgpH2/
- Checked: 16 November 2026.
