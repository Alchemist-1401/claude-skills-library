# Scrapling official skill: scraping that survives bot-blocks

## When to use
Extract data from websites that defeat simple fetches: anti-bot pages, JavaScript-rendered content, sessions, spiders and concurrent crawls, with adaptive parsing that keeps working when a site's markup shifts. This is the official agent skill published inside the Scrapling repository by its author.

## Free scope and limits
BSD-3-Clause licensed, and the library itself is free open source. The real dependency is a local install: `pip install "scrapling[all]"` plus its browser components, which the skill needs before anything runs. That install is a normal free setup step to approve case by case; nothing is installed by this entry. The skill's upstream zip packaged inside the repo is not mirrored; intake takes the unpacked skill folder.

Scraping carries conduct limits that matter more than cost: respect each site's terms and robots rules, do not bypass logins or access controls, do not scrape personal data at scale, and keep request rates polite. The skill's own docs include a prompt-injection defense flag (`--ai-targeted`) for command-line scraping; keep it on, since scraped page text is untrusted input, not instructions.

## How to use
Read the prepared `agent-skill/Scrapling-Skill/SKILL.md`, then give one bounded target:

> Use the Scrapling skill to pull the public pricing table from <site>. Check their robots.txt and terms first; if they disallow it, stop and tell me. One page type, no login areas, save results to a CSV.

For Konsiar prospecting or competitor monitoring, prefer official APIs where they exist and treat scraping as the fallback with consent and rate limits, not the default engine.

## Source intake and setup
`prepare_library.py` retrieves the `agent-skill/Scrapling-Skill/` folder (SKILL.md, examples, fetching/parsing/spider references, LICENSE.txt), the agent-skill README and the repository LICENSE from D4Vinci/Scrapling at the pinned revision, with checksum verification. The `pip install` of the library itself happens only if and when you approve using the skill. To activate later, copy the reviewed skill folder into the project's `.claude/skills/`.

## Sources and reviewed revision
- Original repository: https://github.com/D4Vinci/Scrapling
- Skill folder: https://github.com/D4Vinci/Scrapling/tree/main/agent-skill/Scrapling-Skill
- License: BSD-3-Clause.
- Reviewed commit: 2998c9ebba52ef6116f0a483c7d2f21908250024
- User-shared post that prompted this entry: https://www.instagram.com/p/Dfw8XovDWZf/
- Checked: 17 November 2026.

The review read the skill and reference docs; it did not install the library or scrape any site.
