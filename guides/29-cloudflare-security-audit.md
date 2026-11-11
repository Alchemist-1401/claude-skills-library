# Cloudflare Security Audit

## When to use
MIT-licensed skill for a six-phase security review: reconnaissance, coverage-led hunting, validation, structured findings, independent verification and reporting. Requires a coding agent with parallel workers, Node.js and an OS-enforced sandbox for running target-controlled code. No mandatory paid API or MCP. Existing model usage still applies.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Only audit code you own or are authorized to test. Without required isolation, keep execution-dependent findings unresolved. Never treat a clean AI audit as proof of security. Same repository identified in your earlier FORTRESS reel, now listed once.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit
```

## What is included here
Status: snapshot-and-guide. 20 upstream files in the scoped snapshot. Authored source is beside this guide when available. A snapshot is not a claim that local dependencies are installed.



## Source and attribution
Source: https://github.com/cloudflare/security-audit-skill
Repository: cloudflare/security-audit-skill
Pinned source commit: c1c8a8c1471069fb0e188eeaff69b8e8db6564a8
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
