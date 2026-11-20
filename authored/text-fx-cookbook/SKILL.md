---
name: text-fx-cookbook
description: Build any of 20 named text animations (Slot Roll, Mask Wipe, Caret Type, Kerning Snap, Weight Morph, Underline Draw, Word Carousel, Odometer, Stroke Draw, Split Flap, Matrix Rain, Neon Flicker, Circle Flood, 3D Tumble, Echo Trail, Gravity Drop, Slice, Glow, Stamp, Zoom Through) for a website in dependency-free CSS/JS or for a reel in the user's video pipeline. Use when the user wants moving text for a site, landing page, title card or reel and names an effect or shows a reference. Web output honors prefers-reduced-motion; video output builds in EffectCraft when present, otherwise code.
---

# Text FX cookbook

Twenty concrete text animations, originally shown as Claude-coded effects in the @smartgears.ai reel (source at the end). The user wants these available in two places: **website design** and **reels**. Ask which surface if the brief does not say. Never paste all twenty into one piece; pick one lead effect per text moment.

## Choosing the surface

- **Website**: production-ready, dependency-free CSS with a little vanilla JS when the effect needs per-character splitting or randomness. No animation libraries, no paid fonts. Respect `prefers-reduced-motion`: render the final state statically. Keep the text selectable/real text, not images, unless the effect (Stroke Draw) genuinely needs SVG.
- **Reel/video**: build in the user's motion pipeline. Use EffectCraft when it is present (see the library's EffectCraft entries); otherwise produce the effect as code the pipeline renders. Deliver a short loopable clip or the build itself, never an upload.

## The 20 effects

For each: the recipe, then web (W) and video (V) notes. Stagger per character by default (20-40 ms web, 1-2 frames video).

1. **Slot Roll** - each letter spins through a vertical strip of random glyphs and lands on the final one, slot-machine style. W: per-char span containing a glyph column, translateY keyframes to the final glyph. V: same column offset per char, ease-out.
2. **Mask Wipe** - a hard mask sweeps across and reveals the word. W: clip-path inset animation on the text block. V: linear wipe matte.
3. **Caret Type** - typewriter with a blinking block caret that disappears at the end. W: JS appends characters on a timer; caret is a border or span with blink keyframes. V: char-by-char opacity with caret layer.
4. **Kerning Snap** - letters start widely tracked and snap tight. W: letter-spacing transition with a fast ease. V: tracking animator, one snap at the peak.
5. **Weight Morph** - the word breathes between light and heavy. W: font-variation-settings 'wght' keyframes (needs a variable font; system variable fonts work). V: variable font weight animation, or subtle scale-x as a fallback.
6. **Underline Draw** - the underline draws itself left to right. W: ::after with scaleX 0 to 1, origin left. V: stroke or shape layer draw-on under the text.
7. **Word Carousel** - words rotate through one slot in a sentence. W: stacked words in an overflow-hidden slot, translateY loop. V: same stack, ease each swap.
8. **Odometer** - digits roll upward like a counter. W: digit columns of 0-9, translateY to the value. V: same, with a slight overshoot.
9. **Stroke Draw** - the outline draws itself, then the fill fades in. W: SVG text with stroke-dasharray/dashoffset, then fill opacity. V: trim paths on outlined text.
10. **Split Flap** - airport-board flips, top half folding down. W: two clipped halves, rotateX with perspective and a backface. V: same 3D flip per character.
11. **Matrix Rain** - glyph columns rain and resolve into the word. W: canvas or absolutely positioned glyph columns fading to the final letters. V: character rain particles converging on the word.
12. **Neon Flicker** - a neon glow stutters on, then holds. W: text-shadow flicker keyframes with irregular timing. V: glow/opacity flicker, 3-4 stutters max.
13. **Circle Flood** - a colored circle grows from a point and floods behind or inside the text. W: ::before circle scaling up; use background-clip: text for flood-inside. V: circular matte reveal.
14. **3D Tumble** - letters tumble in 3D space and settle. W: rotateX/rotateY with perspective, staggered. V: 3D layer rotation per char.
15. **Echo Trail** - ghost copies trail the word and catch up. W: duplicated spans with decreasing opacity and increasing delay. V: echo/ghosting effect, 2-3 trails.
16. **Gravity Drop** - letters fall from above and bounce into place. W: translateY from negative with a bounce cubic-bezier. V: drop with a single bounce ease.
17. **Slice** - the word splits into horizontal slices that slide apart, then close. W: stacked clip-path slices translating in opposite directions. V: slice displacement.
18. **Glow** - a soft glow blooms around the word. W: text-shadow growing from 0 to a soft bloom, no flicker. V: glow ramp over 6-10 frames.
19. **Stamp** - the word slams in oversized with a slight rotation and settles with a tiny shake. W: scale from ~3 and a few degrees of rotate, fast ease-out, one 1-2px shake. V: scale pop plus one-frame shake.
20. **Zoom Through** - the camera zooms into and through the word as letters part past the lens. W: scale up with expanding letter-spacing and fade. V: z-axis zoom through the text layer.

## Rules

- One lead effect per text moment; a second effect only as an entrance/exit pair.
- Readability first: the final state must sit still long enough to read.
- Exact-name matching: when the user names one of the 20, build that effect; when they show a reference, name the closest effect back before building.
- Free path only: no paid fonts, libraries, plugins, stock or render services. Web effects are dependency-free by default.
- Respect the surface: web means real accessible text and reduced-motion fallbacks; video means the user's own pipeline and no uploading or posting.

## Attribution and scope

Effect list and demonstrations from the Instagram reel "20 text animations. Claude wrote the code for every one." by @smartgears.ai: https://www.instagram.com/reel/Df8GwhGRFrF/ (November 2026). The reel shows the 20 named effects and a demo terminal; no code or skill file was published or obtained. This cookbook is an original implementation of the publicly demonstrated effects. No license is asserted over the creator's video; only this original text is included here.
