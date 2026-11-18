# last30days: what people actually said this month

## When to use
Research what real people are saying about a topic across Reddit, Hacker News, YouTube, Polymarket, GitHub and the web over the last 30 days, with citations and engagement. Good for demand signals, content topics, and checking what a niche actually complains about before building for it.

## Free scope and limits (read this part)
MIT licensed. The engine runs locally (Python 3 and Node required) and has a keyless free floor: Hacker News (Algolia), Polymarket, Wikidata, Reddit's cookie-free path, and YouTube via a local yt-dlp install all work with no API key. The deeper sources are NOT free: TikTok/Instagram search and Reddit backfill go through the paid ScrapeCreators API (`SCRAPECREATORS_API_KEY`, spends credits), and X/Twitter needs its own access. The skill's onboarding may offer to set that key up; the free answer is to skip it and stay on the keyless floor. Do not buy or enter any API key without the owner's explicit approval.

The 14 MB demo media folder (`assets/`) is not mirrored in intake; the engine, references and docs are. Tool installs the skill asks for (yt-dlp, optionally others) are ordinary free installs to approve case by case; nothing is installed by adding this entry.

## How to use
Read the prepared `skills/last30days/SKILL.md`, then ask for one bounded question:

> Use last30days for "AI headshot tools complaints" on the free keyless sources only. No paid API keys, no X login. Give me the top recurring complaints with links to the actual threads, and mark which sources were unavailable without a key.

The skill has a doctor/health-check command to report which sources currently work; run that before trusting an absence of results.

## Source intake and setup
`prepare_library.py` retrieves `skills/last30days/` (SKILL.md, engine scripts, references) except the demo media folder, plus LICENSE and README, from mvanhorn/last30days-skill at the pinned revision, with checksum verification. The engine scripts are hash-pinned as published upstream; they were read for scope and dependency review, not line-by-line audited, and not executed here. To activate later, copy the reviewed skill folder into the project's `.claude/skills/`.

## Sources and reviewed revision
- Original repository: https://github.com/mvanhorn/last30days-skill
- License: MIT.
- Reviewed commit: a854f3bcb2c4344d7498426d653378510f8b253a
- User-shared post that prompted this entry: https://www.instagram.com/p/Dfw8XovDWZf/
- Checked: 17 November 2026.

The engine was not run during review; source availability changes over time, so treat the doctor output, not this guide, as the current truth at use time.
