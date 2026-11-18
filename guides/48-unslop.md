# unslop: remove the AI look from interfaces

## When to use
Turn a vibecoded, AI-looking screen into a designed interface with its own character. The skill finds the slop first (purple gradients, glows, emoji labels, shouty copy, uneven spacing), sets a direction from your product, then fixes the screen pass by pass like a designer doing a redline review. Works on dashboards, apps and landing pages in Next.js, React, Vue, Svelte, Tailwind or plain HTML/CSS, and even on a live site from a link.

Use it on a throwaway branch or copy first: it edits real UI code, and taste is subjective, so review the diff before keeping changes.

## Free scope and limits
The skill itself is instructions plus small reference scripts; no paid API or service is required. Two optional extras have their own free dependencies: the story/render scripts (`scripts/story.mjs`) need Playwright and ffmpeg installed, and working on a live site from a link needs a way to read that site. The plugin install command upstream advertises (`claude plugin install unslop --marketplace heydamir/unslop`) is a reference option, not something this library runs.

Upstream license is CC BY 4.0 (a documentation-style license, not a code license): copies and adaptations need attribution to Damir Sokolovsky (@heydamir). Preserve the LICENSE file with any copy.

## How to use
Read the prepared `skills/unslop/SKILL.md`, then point Claude at one screen or route, for example:

> Use unslop on the Konsiar dashboard home screen only. First list the slop you found and the design direction you propose. Make the changes on a new branch, keep my copy and data untouched, and show me before/after screenshots. Do not install anything without asking.

Keep it to one screen at a time; broad multi-page restyling in one pass is where quality drops.

## Source intake and setup
`prepare_library.py` retrieves the full `skills/unslop/` skill folder (SKILL.md, design-token and slop-sign references, three optional Node helper scripts) plus the upstream LICENSE and README from heydamir/unslop at the pinned revision, with checksum verification. To activate later in a project, copy only the reviewed `skills/unslop` folder into that project's `.claude/skills/`, keeping the LICENSE. Do not enable it globally across projects.

## Sources and reviewed revision
- Original repository: https://github.com/heydamir/unslop
- License: CC BY 4.0, attribution required.
- Reviewed commit: 620163eedb3529d9cd23a3994ed8d287d06f760d
- User-shared post that prompted this entry: https://www.instagram.com/p/Dfw8XovDWZf/ (pathionai carousel; the actual link sat behind a comment gate, so the repository was resolved independently)
- Checked: 17 November 2026.

The review read the skill text and references; it did not run the restyle or the story renderer on any project. The author's before/after images are illustrative, not a promise for your UI.
