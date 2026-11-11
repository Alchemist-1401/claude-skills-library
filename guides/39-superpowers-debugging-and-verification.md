# Superpowers: debugging and verification

## When to use
Two reviewed MIT skills: systematic-debugging finds root causes before fixes; verification-before-completion requires fresh test/build evidence before claiming success. They are local instructions and supporting techniques, with no mandatory paid API or MCP. Tests use the project's existing language/runtime.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Subset only, not the full autonomous framework. Keep the complete debugging folder and review its cross-references to test-driven-development before use. Existing Matt Pocock TDD covers a related purpose; avoid adding a second whole TDD workflow by default. No automatic implementation, commits, deployment, new accounts or spending is authorized.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the complete skills/systematic-debugging and skills/verification-before-completion folders from the repository into .claude/skills/ in the intended project. Preserve the supporting debugging references and helper files. Review them before execution. Do not install the full Superpowers plugin merely to use this subset.
```

## What is included here
Pinned-source intake: 9 selected upstream files are fetched by prepare_library.py into library/entries/39-superpowers-debugging-and-verification/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/obra/superpowers
Repository: obra/superpowers
Pinned source commit: 22f0b463e7a5e579904dd6211a520321035526f7
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
