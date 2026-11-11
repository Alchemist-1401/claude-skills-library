# REA: reverse-engineer-anything

## When to use
The repository includes a real MIT reverse-engineer-anything skill and a local analysis toolkit. Static JavaScript analysis needs no native analysis engine; Ghidra is an available free native-analysis path. Neither route requires a paid model API or a paid hosted MCP service beyond your existing assistant.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report. Not a skill-only install: its documented setup registers a local MCP server. Paid analysis engines are optional, not part of this entry. Use it only on software you are authorized to inspect; MIT licensing does not grant rights over someone else's app.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx rea-agents setup

Review the local server and skill configuration changes before approving. Use static JavaScript analysis, or a separately verified free Ghidra setup; never choose a Hopper/IDA trial or paid license as a hidden dependency.
```

## What is included here
Status: snapshot-and-guide. 9 upstream files in the scoped snapshot. Authored source is beside this guide when available. A snapshot is not a claim that local dependencies are installed.



## Source and attribution
Source: https://github.com/morluto/rea
Repository: morluto/rea
Pinned source commit: dcdae135435eb9c3c56e5e50116ab5da812a5409
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
