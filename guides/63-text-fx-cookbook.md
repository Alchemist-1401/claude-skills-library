# Text FX cookbook

## When to use
Twenty named text animations for moving type: Slot Roll, Mask Wipe, Caret Type, Kerning Snap, Weight Morph, Underline Draw, Word Carousel, Odometer, Stroke Draw, Split Flap, Matrix Rain, Neon Flicker, Circle Flood, 3D Tumble, Echo Trail, Gravity Drop, Slice, Glow, Stamp, Zoom Through. Built for two surfaces: website design (dependency-free CSS/JS, reduced-motion safe) and reels (the user's video pipeline, EffectCraft when present). Use when a site, landing page, title card or reel needs text that moves.

## How to use
Read `authored/text-fx-cookbook/SKILL.md`, then name the effect and surface, for example:

> Use text-fx-cookbook: Kerning Snap on the word "Tight" for the Konsiar homepage hero, web. Real text, reduced-motion fallback included.

or:

> Use text-fx-cookbook: Slot Roll on "SPEED" for the next Velocitas reel, 3 seconds, loopable.

The skill asks which surface if the brief does not say, builds one lead effect (a second only as an entrance/exit pair), and keeps the final state still long enough to read. Web output is real selectable text with no libraries; reel output builds in EffectCraft when present, otherwise as renderable code.

## Setup and local intake
A normal Markdown file in `authored/text-fx-cookbook/SKILL.md`. No installer, account, dependency, API key or paid service. Web effects are dependency-free CSS/vanilla JS by default. The standard `prepare_library.py` intake copies this guide and the authored skill with checksum verification; it does not activate anything.

## Source and scope
Authored for this library from the user-shared reel by @smartgears.ai: https://www.instagram.com/reel/Df8GwhGRFrF/ ("20 text animations. Claude wrote the code for every one."), with the owner's note that he needs these "in both website design and reels" (19 November 2026). The reel publishes no code; this is an original implementation of the 20 publicly demonstrated effects. No license over the creator's content is asserted.

Checked: 19 November 2026.
