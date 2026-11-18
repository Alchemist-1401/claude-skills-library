# Anthropic official skills pack (canvas, art, artifacts, GIFs, MCP, skill creator, comms, docs)

## When to use
Nine official Anthropic skills from the anthropics/skills repository, matching the design, dev, operations and legal labels of the business-squads carousel: canvas-design (poster/visual design), algorithmic-art (generative art), web-artifacts-builder (web artifacts), slack-gif-creator (animated GIFs for Slack), mcp-builder (build MCP servers), skill-creator (author new skills), internal-comms (internal communications), xlsx (spreadsheet creation/editing) and docx (document creation/editing).

Companion to library entry 38, which already covers frontend-design and webapp-testing from the same repository; there is no overlap between the two entries.

## Free scope and limits
Each of the nine skills carries its own LICENSE.txt with the full standard Apache License 2.0 text, verified at the pinned commit - including docx and xlsx, which have historically raised license questions; no source-available or proprietary exception applies at this revision. Document skills may use Python libraries (for example openpyxl, python-docx) inside Claude's environment; those are free, preinstalled in Claude Code, and disclosed upstream. No paid API or account is required.

## What is included
250 selected upstream files: the nine complete skill directories (SKILL.md, scripts, references, examples and per-skill LICENSE.txt) plus the repository README and THIRD_PARTY_NOTICES.md, hash-verified on intake by prepare_library.py.

## How to use
After preparation, name the skill and give the actual task, for example:

> Use canvas-design to draft a launch poster concept for Konsiar: headline, layout and palette directions. Reference only, no final assets.

## Sources and reviewed revision
- Original repository: https://github.com/anthropics/skills
- License: Apache License 2.0 (per-skill LICENSE.txt in every included skill).
- Reviewed commit: e4bb5d960d87126ff3b3a8af1a104b7db67560ba
- Carousel that prompted this entry: https://www.instagram.com/p/Dfe3uGciqka/ (osama.ishtiaq.ai). The post published no links; this is a verified exact-name match to the official repo, not proof of the creator's precise source.
- Checked: 17 November 2026.
