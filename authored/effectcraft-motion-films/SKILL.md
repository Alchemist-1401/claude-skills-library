---
name: effectcraft-motion-films
description: Direct and produce a short motion-graphics film or reel (explainer, promo, launch, title sequence, social reel) by driving EffectCraft over MCP instead of writing rendering code from scratch. Use when the user asks Claude to make a video, reel, animation or motion graphic, especially vertical 9:16 social content, and EffectCraft is or can be connected. Adapted from the directing method of Lemo-Opuscar; the execution layer is EffectCraft.
---

# EffectCraft Motion Films

Make short films and reels by directing EffectCraft (the free, open-source motion graphics app) through its MCP server. You design and animate with EffectCraft's compositions, layers, keyframes, effects and render queue. You do not write a frame-by-frame renderer in code.

This skill is an adaptation of the directing method from **Lemo-Opuscar by Lemomo (LemoLab)** (https://github.com/lemomo-ai/lemo-opuscar), whose documentation is licensed CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/). Changed here: the build-everything-in-code pipeline is replaced with EffectCraft workflows, and the text is condensed, rewritten and restructured. Lemomo's additional grant covers adapting the docs to make your own films, including commercial and client films. This file is a personal, private adaptation. CC BY-NC 4.0 itself permits noncommercial sharing with attribution, but check the actual terms before redistributing this file in any form; commercial redistribution or embedding needs Lemomo's permission per the upstream LICENSE (lemomo.studio@gmail.com).

Verification status: the EffectCraft workflow below is verified against current documentation (sources at the end), not exercised end-to-end on a live render. EffectCraft is in alpha (about 91% of its tracked features per its README), so treat any single command as subject to confirmation with `command_list` before relying on it.

---

## 1. Check the setup, then fix what's routine

First check whether the `effectcraft` MCP tools are available in this session (`doc_inspect` is a good probe). If they are, go to section 2.

If not, inspect before asking:

- Is the EffectCraft app installed? Is `effectcraft-cli` present on PATH or in a known install folder? (On macOS the CLI is a separate download, `effectcraft-cli-...-macos-universal.zip`, from the EffectCraft releases page.)
- Is an MCP server named `effectcraft` already registered with Claude Code (`claude mcp list`)?

Handle routine setup yourself within the user's authority: registering the CLI as an MCP server is a normal config step, documented as:

```sh
claude mcp add effectcraft -- /full/path/to/effectcraft-cli mcp
```

Optional, for tighter file safety, confine the agent's file access to a working folder:

```sh
claude mcp add effectcraft -- /full/path/to/effectcraft-cli mcp \
  --automation-read-root ~/Documents/Claude/effectcraft-projects \
  --automation-write-root ~/Documents/Claude/effectcraft-projects
```

Note: while confined this way, EffectCraft refuses to run scripts.

Two ways to run, both documented:

- **Standalone (headless):** `effectcraft-cli mcp` runs its own copy of EffectCraft with no window. Simplest; use it by default.
- **Bridge (watch it live):** start the app with `effectcraft --control 9877`, then connect with `effectcraft-cli mcp --bridge 9877`. The assistant's edits appear in the app window, and it can take screenshots and use menus.

Never install software or change configuration silently. If something is genuinely missing (app not installed, CLI download needed, a permission only the user can grant), tell the user exactly what is needed and let them decide. If the tools stay unavailable, stop and say so; do not fall back to writing a code renderer.

## 2. Take the brief

The user gives a topic, sometimes a style reference, length, format, brand rules or must-have shots. Ask at most one round of questions, then decide the rest. Defaults:

- Length follows the platform: roughly 15-45 s for a reel, 30-60 s for an explainer. Shorter and tight beats padded. Past 2 minutes, warn about time and token cost.
- Frame size from the destination: 1080x1920 (9:16) for Instagram reels, 1920x1080 for landscape. Set it on the composition, not at export.
- 24 or 30 fps unless the user says otherwise.
- On-screen text in the user's language, held long enough to read (section 7).
- Loudness target about -14 LUFS when there is sound.

## 3. Benchmark, then shape the story

For anything beyond a trivial clip, pick one or two reference works (ads, title sequences, reels) that set the bar for this topic. Note what to learn (composition, pacing, colour logic, transitions) and what never to copy (characters, designs, melodies, logos, fonts, specific shots).

Story guidance, scaled to the brief:

- One subject, one goal, one change. A character, product or idea wants something; something changes; it ends differently from how it began. On a very short reel this can be a single clear beat.
- Hook early: inside the first second for reels, the first few seconds for longer pieces. No slow logo reveal.
- End with an echo of the opening when the length allows it: bookend, scale reveal, or the second attempt done right.
- One native move, a transition or transformation only motion graphics can do, at the emotional peak. Skip it rather than force it on a tiny clip.
- Cut extras. One gag the viewer reads at thumbnail size beats three they cannot.

## 4. Plan before building

Scale the planning to the job. A 10-second text animation needs a few lines of intent; a 45-second reel earns a short `TREATMENT.md` in the project folder:

1. Candidate structures, a line each (single journey, before/after, countdown, list that turns), then the pick and why. Two candidates is fine for short work; the first idea for a topic is usually its cliche.
2. Logline and arc: one sentence, then setup, turn, ending.
3. Benchmark: learn / do not learn.
4. Shot list: each shot with framing, movement (push, pull, pan, track, zoom, parallax), duration, and why.
5. Beat sheet, second by second.
6. Cue map if there is sound: tempo and where each cut, key action and text lands.
7. Text design: fonts, sizes, placement, how text enters. Type is part of the look.

## 5. Build in EffectCraft

Work through the MCP tools:

- `doc_inspect` first, to see the open project and active composition.
- `command_list` (with its filter) to discover the exact commands and parameters available in the installed version before relying on any specific one. `command_run` runs one command; `command_batch` runs a sequence and stops at the first error by default; read per-step `results` when something fails.
- Build compositions from layers: solids, shapes, text, footage, nested compositions, nulls, adjustment layers. 3D cameras and lights exist for looks that want depth.
- Animate with keyframes rather than static poses: transform properties on parented nulls, easing (Easy Ease, graph editor curves) for weight, shape operators (trim paths, repeater, wiggle and friends) and text animators for kinetic type, expressions for loops and secondary motion.
- Use the built-in effects library (documented at 308 effects, including blur, colour, distortion, keying, matte, stylize and audio effects) instead of inventing visual code.
- `render_preview` early and often: check frames at key beats before animating further. For a designed look, render a few representative frames first, one of them the signature shot, and compare against the plan before committing.

Practical habits:

- Save the project (`.ecproj`, plain JSON) into the working folder early so renders have an output path.
- While a render runs, the job owns a snapshot of the project; edits land but are not in that render, and a second render is refused until the first finishes. Render again after editing.
- Headless renders can also run from the CLI (`effectcraft-cli render --comp Main --out main.mp4`), documented in the README.

## 6. Sound, when the film has it

EffectCraft has an Audio panel, audio effects, and in-sync preview with meters and waveforms; it imports audio as footage and exports sound in its video formats (plus WAV/AIFF). Voiceover and music files themselves come from whatever free source the user already uses; check the rights of any audio before including it.

Principles, applied with judgment rather than as quotas:

- Key actions read better with matching sound: clicks, whooshes, landings, page turns. Match the material.
- Think in layers: ambience, action sounds, music. Duck music under voice.
- Silence is a tool: a near-silent beat before the turn or the peak makes the next sound land. Use it where it earns its place.
- Sound can smooth transitions: bring the next scene's sound in early, or let the last scene's sound run over the cut.
- Avoid generic piano-and-strings; pick instrumentation that fits the subject.
- If the reel is silent-plus-text by design, say so in the plan and skip the rest of this section.

## 7. Rhythm and readability

- If there is sound, lock cuts and text to the cue map. Vary pace where the film is long enough to sustain it: a faster passage, a slower one, one breath. Even speed throughout a 45-second film reads flat; a 10-second reel can just be tight.
- Hold every subtitle at least 1.8 s, and never shorter than the spoken line plus 0.6 s.
- After text animates in, hold it long enough to read at a glance (roughly letters / 15 + 1.5 seconds). A full-screen title card in a longer film wants around 4 s; scale down for short reels rather than padding them.
- Make a fast reel with fewer words per screen, not by cutting before people finish reading.

## 8. Camera and motion

- Match movement variety to length: several distinct kinds of movement and real framing changes across a 45-second piece; a short reel needs only one or two moves done well. In 2D the camera is position/scale/rotation on a parent null, parallax between layers, and focus pulls with blur.
- Give the film one signature moment when it earns one: a oner, a scale reveal, or a transition made from the medium itself.
- Design transitions as one consistent grammar (shape morphs, mask wipes, type that becomes the next scene). Avoid default fades and unmotivated hard cuts. Do not stack effects for their own sake.
- At key moments the subject should read clearly: large enough in frame, with a readable silhouette.
- Meaningful moves get weight: anticipation, action, follow-through, intentional easing. Nothing slides at constant speed unless that is the joke.

## 9. The failures to check for

- Subject too small, too far away, or jammed against the frame edge.
- Text covering the subject, or unreadable type (contrast, size, hold time).
- Too dark to read, or a colour on the same colour.
- A gag or key action too fast to understand.
- Blank frames inside transitions.
- An animation that loses the subject after a camera move (parent or track it).

## 10. Review and deliver

- Review before delivery: step through key actions at 0.2 s intervals, render preview frames at final size, watch one full-speed pass with sound if there is any.
- Fix what the review finds and check again. Repeat until no material errors remain. Do not deliver with known unresolved flaws: if something cannot be fixed with what's available, tell the user what it is and let them decide before you deliver.
- Deliver through the Render Queue to the project folder: the final video at the comp's frame rate and size (documented export formats include H.264 MP4, ProRes MOV with alpha, HEVC, AV1, WebM, image sequences, GIF, WAV/AIFF), plus the plan (`TREATMENT.md` if you wrote one), and a `CREDITS` file naming every third-party asset (fonts, music, footage, images) with its source and licence.
- Tell the user where the folder and the film are, and that they are responsible for the rights to materials they handed over.

## 11. Rights

- References teach grammar only. Never copy characters, designs, melodies, shots, logos or type designs from a benchmark.
- Assets the user owns, has licensed, or is otherwise authorized to use are fine, including their own brand assets and client materials they have rights to. Ordinary descriptive references (naming a thing to describe it) are fine.
- When rights to a third-party asset are uncertain, ask the user rather than assuming either way.
- Films made with this skill are the user's, subject to the rights of whatever third-party assets (music, voice, fonts, footage) end up in them. Verify those rights; no workflow can guarantee ownership independent of the assets used.
- Every third-party asset used lands in `CREDITS` with its licence.

## 12. What this skill deliberately drops from Lemo-Opuscar

- The code rendering pipeline (canvas/WebGL frames, headless Chrome, the `core/` toolchain and its Node/ffmpeg/Python dependencies). EffectCraft replaces it, including video and audio encoding in pure Rust.
- The 99-style prompt library. Those style prompts stay in Lemo-Opuscar under CC BY-NC; browse the gallery (https://lemomo-ai.github.io/lemo-opuscar/) for a look, then rebuild the look with EffectCraft layers and effects rather than copying the prompt files.
- The built-in TTS/voice-check pipeline. Bring audio from the user's existing free tools if the film needs a voice.

## Sources (checked 2026-11-12)

- EffectCraft README (capabilities, 308 effects, alpha status, export formats, CLI render): https://github.com/storytold/effectcraft
- EffectCraft AI-agents guide (MCP setup per platform, bridge mode, folder confinement): https://craft.wiki/apps/effectcraft/ai-agents/
- EffectCraft MCP conventions (tools `command_list` / `command_run` / `command_batch` / `doc_inspect` / `render_preview`, batch error semantics, render snapshot and single-render rules, confinement refusing scripts): https://github.com/storytold/effectcraft/blob/main/docs/mcp.md
- Lemo-Opuscar (directing method adapted here, licence terms): https://github.com/lemomo-ai/lemo-opuscar
