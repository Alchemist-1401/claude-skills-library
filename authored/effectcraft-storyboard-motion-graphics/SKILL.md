---
name: effectcraft-storyboard-motion-graphics
description: Produce a polished motion graphic (logo sting, promo, social animation) from a one-line idea and brand assets by first returning a numbered storyboard for approval, then building and rendering it in EffectCraft on the user's machine. Use when the user describes an animation idea and expects a storyboard before any build, or says go after reviewing one. No video-generation model and no per-render credits; rendering is local and free.
---

# EffectCraft storyboard motion graphics

A two-gate workflow for motion graphics: storyboard first, build only on approval. Inspired by a reel by @mr.pynk showing a Claude skill that turns an idea plus a logo into a numbered storyboard and then a finished animation (source at the end). The twist per the library owner's standing direction: the animation is built and rendered in **EffectCraft** (the free, open-source motion graphics app, driven through its MCP server) instead of hand-writing a code renderer. If EffectCraft is unavailable in the session, stop and say so; do not silently fall back to another pipeline.

## Gate 1: brief and storyboard

Take the user's idea and any assets (logo file, brand colors, product shots). Ask at most one round of questions, then return a **numbered storyboard** in chat:

- One numbered beat per row: what is on screen, what moves, the text (exact words), approximate seconds.
- Frame size from the destination: 1080x1920 for reels/shorts, 1920x1080 for landscape, 1080x1080 for square posts. 24 or 30 fps.
- Style direction in one line (for example: editorial texture background, bold serif type, one accent color from the logo).
- Total runtime, kept tight: 5-15 s for a logo sting, 15-45 s for a promo.

Then stop. Do not build until the user approves or edits the storyboard. "Go", "looks good", or a specific edit all count; silence does not.

## Gate 2: build and render in EffectCraft

On approval:

1. Check the `effectcraft` MCP tools are available (probe with a light call such as a document inspect). If missing, follow the setup notes in `effectcraft-motion-films` (same library, `authored/effectcraft-motion-films/SKILL.md`): install/register only within the user's authority, and report anything only they can do.
2. Create a composition at the storyboard's frame size and fps. Build each numbered beat as its own layer group or nested composition, in storyboard order, so revisions map back to beat numbers.
3. Animate with keyframes and effects; keep movement intentional (one native move at the peak, calm elsewhere). Import the user's logo and assets from disk; never regenerate or redraw a brand logo.
4. Render through EffectCraft's render queue on the user's machine. 4K (3840 px wide) when the destination and machine allow it, otherwise 1080 px. Name the output after the project and version.
5. Report the output path and what was rendered. If anything in the storyboard could not be built as approved, say which beat and why.

## Rules

- The storyboard gate is the point of this skill. Never skip from brief to render.
- Free path only: EffectCraft is free and open-source; no video-generation model, no credit-based service, no stock-site purchases. Texture and paper assets, when needed, come from free sources (see `editorial-texture-backgrounds` for the texture technique and sources).
- Everything renders locally; nothing is uploaded or published. Posting the result anywhere is the user's separate action.

## Attribution and scope

Workflow inspired by the Instagram reel "This Claude skill creates premium motion graphics" by @mr.pynk: https://www.instagram.com/reel/Df2q9FtuPc1/ (November 2026). The reel's own skill was behind a comment gate and was not obtained; this is an original implementation of the publicly described workflow (idea + logo, numbered storyboard, go, local render, no video model or credits), redirected to EffectCraft at the library owner's standing instruction. No license is asserted over the creator's video or their skill; only this original text is included here.
