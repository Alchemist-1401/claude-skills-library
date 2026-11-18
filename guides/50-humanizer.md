# Humanizer: strip AI-writing tells from text

## When to use
Rewrite AI-drafted text so it reads like a person wrote it, without changing what it says. The skill is built on Wikipedia's "Signs of AI writing" guide that Wikipedia editors use to catch generated text: inflated vocabulary, filler transitions, rule-of-three padding, em-dash habits, self-description, and the rest. Use on outreach drafts, posts, docs and captions before anything goes out under your name.

## Free scope and limits
MIT licensed, pure instruction skill, no API keys, no service, nothing to install. The one bundled script (`scripts/validate-package.py`) only validates the skill's own packaging; it is not part of normal use.

This edits voice, not facts. It does not verify claims, and running text through it is not a substitute for reading the result yourself, especially for anything sent as you. It also cannot guarantee any third-party "AI detector" outcome; detectors are unreliable in both directions.

## How to use
Read the prepared `SKILL.md`, then hand Claude the draft:

> Use humanizer on this outreach email. Keep every fact, name and price exactly as is, keep it short, and do not add claims. Show me the rewrite next to the original before I use it.

Pairs naturally with the library's writing-style references; it does not replace your approved outreach structure or sending permissions.

## Source intake and setup
`prepare_library.py` retrieves SKILL.md, LICENSE, README.md and the packaging validator script from blader/humanizer at the pinned revision, with checksum verification. To activate later, copy the reviewed files as a skill folder into the project's `.claude/skills/`.

## Sources and reviewed revision
- Original repository: https://github.com/blader/humanizer
- License: MIT.
- Reviewed commit: b48c832f0f809c1b5658edbb838c2521b72f2413
- Method reference named by the skill: Wikipedia, "Signs of AI writing"
- User-shared post that prompted this entry: https://www.instagram.com/p/Dfw8XovDWZf/
- Checked: 17 November 2026.

The review read the full skill text; no rewrite quality testing was performed against your own drafts.
