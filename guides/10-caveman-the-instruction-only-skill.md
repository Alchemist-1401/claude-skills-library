# Caveman: the instruction-only skill

## When to use
Shortens replies while preserving technical facts, exact commands and negations. The standalone skills/caveman/SKILL.md is a free Apache-2.0 instruction file. It does not need the larger Caveman CLI, routing account or cloud service.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report. This is an existing upstream module, not a rewritten free substitute. The full current CLI has telemetry and optional cloud routing; those are outside this entry. No token-saving percentage is promised.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the upstream skills/caveman folder into .claude/skills/caveman in the intended project. Keep its SKILL.md unchanged. Use /caveman; use normal mode to turn it off.
```

## What is included here
Pinned-source intake: 6 selected upstream files are fetched by prepare_library.py into library/entries/10-caveman-the-instruction-only-skill/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md
Repository: JuliusBrussee/caveman
Pinned source commit: 3dc497a7f858c774d6e15b25e8c6120ef3a0eda8
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
