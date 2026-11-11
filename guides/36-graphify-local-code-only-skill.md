# Graphify: local code-only skill

## When to use
Apache-2.0 project with a real /graphify skill and a local Python toolkit. Builds a queryable code relationship graph using deterministic tree-sitter parsing. Python 3.10+ and uv or pipx are needed. The reviewed free route is code-only with all LLM backends disabled; no API key, cloud trial or MCP is needed.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Not an instruction-only install: it adds the local graphifyy CLI, a project skill, supporting references and assistant configuration. Review those project changes first. Graphify Cloud and its trial are excluded. Semantic docs/media extraction, API providers, automatic hooks and integrations are outside this entry. Vendor token-saving claims are not independently verified.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Documented local route, not executed:
uv tool install graphifyy
graphify install --project
GRAPHIFY_BACKEND=none graphify extract . --code-only
Query the resulting local graph with graphify query, graphify path or graphify explain. Keep the code-only and backend=none limits when asking Claude to use /graphify. Read upstream CLI help before running.
```

## What is included here
Pinned-source intake: 13 selected upstream files are fetched by prepare_library.py into library/entries/36-graphify-local-code-only-skill/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Graphify-Labs/graphify
Repository: Graphify-Labs/graphify
Pinned source commit: 35d1d2038b9e9d470f117bf8f2473d415b5f5358
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
