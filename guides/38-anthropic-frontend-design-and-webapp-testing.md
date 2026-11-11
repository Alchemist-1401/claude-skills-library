# Anthropic: frontend design and webapp testing

## When to use
Reviewed two Apache-2.0 skills: frontend-design for deliberate visual choices and webapp-testing for local browser checks. Frontend design is instruction-only; webapp testing uses Python, Playwright and a locally installed Chromium browser, plus its bundled helper scripts. No mandatory paid API, hosted MCP or stock-asset service.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Official Anthropic repository, but its examples are educational and need testing in your own environment. This entry does not approve the entire pack, claude-api, MCP builder, paid Claude plan upgrades or any purchase. Frontend-design overlaps the design sources already here: use one lead design system and redesign only when requested.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the complete skills/frontend-design and skills/webapp-testing folders, including LICENSE.txt, scripts and examples, into .claude/skills/ in the intended project. For local browser testing install the free Python Playwright package and Chromium as upstream documents. Review scripts and run their --help before use. Do not install example-skills wholesale for this subset.
```

## What is included here
Pinned-source intake: 10 selected upstream files are fetched by prepare_library.py into library/entries/38-anthropic-frontend-design-and-webapp-testing/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/anthropics/skills
Repository: anthropics/skills
Pinned source commit: 2c5958ecac7cee2b583967a2c4981d0f4a75c579
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
