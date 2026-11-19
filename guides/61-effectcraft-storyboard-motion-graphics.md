# EffectCraft storyboard motion graphics

## When to use
Turn a one-line animation idea plus brand assets (logo, colors, product shots) into a finished motion graphic through a two-gate workflow: Claude first returns a numbered storyboard, and builds only after you approve it. The build and render run in EffectCraft (free, open-source, local) instead of a code renderer or a paid video model. No credits, no upload.

## How to use
Read `authored/effectcraft-storyboard-motion-graphics/SKILL.md`, then give the idea and assets, for example:

> Use effectcraft-storyboard-motion-graphics: a 10-second vertical logo sting for Konsiar, logo file attached, editorial style. Storyboard first; wait for my go.

Gate 1 returns the numbered storyboard (beats, exact on-screen text, timing, frame size) and stops. Your "go" (or edits) triggers gate 2: build in EffectCraft, render locally (4K when the machine allows), report the output path. The storyboard gate is the point; the skill never skips from brief to render.

## Setup and local intake
A normal Markdown file in `authored/effectcraft-storyboard-motion-graphics/SKILL.md`. EffectCraft itself is a separate free app (see entries 13 and 45 for its MCP setup); the skill checks for it and stops rather than falling back to another pipeline if it is missing. No paid service, API key, video model or credits anywhere in the flow. The standard `prepare_library.py` intake copies this guide and the authored skill with checksum verification; it does not install EffectCraft or activate anything.

## Source and scope
Authored for this library from the user-shared reel by @mr.pynk: https://www.instagram.com/reel/Df2q9FtuPc1/ ("This Claude skill creates premium motion graphics... numbered storyboard... say go... rendered in 4K right on your machine. No video model, no credit costs."). The creator's own skill sat behind a comment gate and was not obtained; this is an original implementation of the publicly described workflow, redirected to EffectCraft per the library owner's standing instruction ("give it an effect craft twist", 19 November 2026). No license over the creator's content is asserted.

Checked: 19 November 2026.
