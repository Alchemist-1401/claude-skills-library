# Find Skills (Vercel Labs)

## When to use
Find an existing agent skill for a specific task instead of searching repositories by hand. This is the discovery skill described in the Nate Herk reel shared on 11 November 2026: a Vercel skill that searches the skills.sh ecosystem and can propose installation. It is not a bundle that automatically supplies every skill in that directory.

## How to use
Give Claude a concrete task, for example:

> Find a skill for reviewing a React app's accessibility. Compare suitable options, read their actual source and license, check dependencies and costs, and show me your recommendation. Do not install anything yet.

Read this guide and the pinned `skills/find-skills/SKILL.md` first. The workflow checks the skills.sh leaderboard, searches by keywords, and presents candidates. Install counts and stars can help triage, but do not prove safety, quality, free use or suitability. Review each candidate's full instructions, scripts, dependencies and license before use. Directory results are not automatically approved additions to this library.

## Setup in the intended project
No setup was run on your device. If you later choose to install it for Claude Code, the official project-scoped command is:

```bash
npx skills add vercel-labs/skills --skill find-skills -a claude-code
```

This is a reference command, not executed during library preparation. It runs the Skills CLI and retrieves a skill, so inspect the source and choose the intended project first. The current CLI README requires Node.js 22.20 or later and internet access. Do not add `-g` (global scope) or `-y` (skip confirmation) by default. The upstream skill's optional global-install example does not change your existing permissions or project boundaries. The public directory at https://skills.sh/ can also be browsed without installing a skill.

## What is included
Pinned-source intake retrieves only `skills/find-skills/SKILL.md`, `README.md` and `LICENSE` from `vercel-labs/skills` into `library/entries/40-vercel-find-skills/upstream/`. The original files are fetched by `prepare_library.py`, not hosted as loose files in this repository. Preparation does not run the CLI, search the directory, install dependencies or activate any skill.

## Free scope and limits
The skill and CLI source are MIT licensed. The reviewed discovery path has no required paid API key or subscription. Claude access/allowance is separate. Skills found through the directory may require paid services, API keys, subscriptions or credits; they are not covered by this entry's free scope. The library's existing free-only checks still apply. The CLI README documents anonymous telemetry and security-audit requests; `DISABLE_TELEMETRY=1` or `DO_NOT_TRACK=1` disables both. No telemetry setting was changed here.

The reel's directory size and install totals are promotional figures, not verified requirements or guarantees. Finding this skill does not give Claude new permissions or make a private repository readable from a link alone.

## Source and provenance
- Original skill: https://github.com/vercel-labs/skills/blob/main/skills/find-skills/SKILL.md
- Repository and MIT license: https://github.com/vercel-labs/skills/
- Official Vercel documentation: https://vercel.com/docs/agent-resources/skills
- Directory: https://skills.sh/
- User-shared reel: https://www.instagram.com/reel/Dfm3zUdHNBs/
- Reviewed commit: `e781cb4d07433dfe1d19e924ed45cc61738c55ec`
- Checked: 11 November 2026. This is a new entry, not a duplicate of the existing design or marketing skills.
