# GEO SEO Claude (audit scope)

## When to use
Review a site's AI-search readiness: crawler access, answer clarity, content structure and schema. This is `zubair-trabzada/geo-seo-claude`, the second repository shown in the user-shared reel. It is separate from Claude SEO, though their GEO and technical checks overlap; choose the smallest relevant skill rather than run both automatically.

## How to use
Read `geo/SKILL.md` and the relevant audit sub-skill, then supply an actual page or URL:

> Check this page's AI-search readiness with GEO SEO Claude. Explain crawler-access and content issues with evidence. Treat citability scores as heuristics, not proof ChatGPT, Perplexity or Google will cite it. Suggest a few fixes without deploying anything.

After a separately approved full installation, `/geo quick <url>`, `/geo crawlers <url>` and `/geo citability <url>` are focused entry points; `/geo audit <url>` is broader. The library does not register those commands.

## Setup and source intake
`prepare_library.py` fetches selected audit skill Markdown plus README, MIT license and dependency list at commit `989cae01e8ebbc42a9ec798eb9e7cb423f5ec89c` into `library/entries/43-geo-seo-claude-audit/upstream/`. This is an audit-reference subset, not a runnable installation. Scripts, agents, report templates/media, prospect CRM, proposals, monthly tracking and auto-update skills are not supplied. Some upstream instructions still refer to those omitted files; retrieve a needed dependency from the pinned original source only after deciding on setup.

The source requires Claude Code, Git and Python 3.10+; its installer creates a virtual environment under `~/.claude/skills/geo/.venv/` and adds skill/agent files. Optional screenshot/report workflows have further dependencies. Inspect the installer and intended scope first. Do not use the upstream pipe-to-shell quick-start as an automatic intake step. Nothing was installed here.

## Free scope and limits
The source is MIT licensed and describes the tool as free. The selected public-page audit guidance requires no paid API account. Claude access/allowance is separate. The creator's paid community, monetization advice, agency pricing and revenue claims are not included or verified.

A readiness score is not observed AI visibility, a scientific citation probability or a guarantee of ranking, traffic or sales. Upstream market statistics, passage-length targets and brand-correlation claims need independent evidence before being used as client-facing facts. Do not assume `llms.txt` makes a page indexed or cited. Respect site crawl limits and use only public or authorized content. Review report claims before sharing them. Site changes and outreach remain subject to the owner's existing scope.

## Sources
- Original repository, README and MIT license: https://github.com/zubair-trabzada/geo-seo-claude
- User-shared reel: https://www.instagram.com/reel/DfioPDmHCCs/
- Checked: 11 November 2026. No CRM, prospect, proposal or follow-up settings were changed.
