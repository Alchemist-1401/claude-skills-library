# Diagram Design: editorial diagrams as self-contained HTML+SVG

## When to use
Turn a plain-words description into a clean editorial diagram: flows, architectures, timelines, comparisons, org charts, funnels and about 45 more types. Output is one self-contained HTML+SVG file per diagram, in your brand tokens, with no Mermaid default look. Good for Konsiar/Velocitas decks, docs and posts where a diagram should look designed, not generated.

## Free scope and limits
MIT licensed, no paid dependency. Diagrams render as HTML/SVG, so no diagram service or account is needed; export to PNG/PDF uses tools you already have (a browser). The skill ships with a default style (paper/ink/accent tokens) and deliberately pauses on first use to ask whether to customize from your website, an installed skill, a folder, pasted tokens, the default, or a saved profile. Answer that gate honestly per brand; Konsiar and Velocitas should get separate saved profiles, not one shared look.

The upstream repo carries 239 example/template HTML files under `assets/` (about 5 MB). Those are NOT mirrored in this library's intake: the skill core (SKILL.md, 69 reference files, 8 helper scripts) plus LICENSE and README are pinned. If a workflow needs the example gallery or the terminal-chrome template, fetch it from the pinned upstream revision under the same MIT license.

## How to use
Read the prepared `skills/diagram-design/SKILL.md`, then ask for one diagram at a time:

> Use diagram-design for a 5-step onboarding flow diagram for Konsiar, vertical, for a slide. Load the Konsiar brand profile (or ask me for tokens if none exists). Give me the HTML file and a rendered screenshot to check. One diagram; do not batch a whole deck.

Check the rendered output visually before shipping: text overflow and cramped nodes are the common failure, and the skill's own QA references cover fixes.

## Source intake and setup
`prepare_library.py` retrieves `skills/diagram-design/` minus the bulky `assets/` gallery, plus LICENSE and README, from cathrynlavery/diagram-design at the pinned revision, with checksum verification. To activate later, copy the reviewed skill folder into the project's `.claude/skills/`. The repo also advertises plugin manifests for several agents (Codex, Copilot, Cursor and others); those are reference options, not installed by intake.

## Sources and reviewed revision
- Original repository: https://github.com/cathrynlavery/diagram-design
- License: MIT.
- Reviewed commit: f6db0decea96de66b901331a0f79a8d4b147ebae
- User-shared post that prompted this entry: https://www.instagram.com/p/Dfw8XovDWZf/
- Checked: 17 November 2026.

The review read the skill and reference structure; it did not render every diagram type. Diagram quality claims (45+ types, no-shadow style) are the upstream design, verified only for the reviewed samples.
