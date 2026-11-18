# Closer sales team skills (11 skills: leads, outreach, follow-up, call coach, contracts, pipeline)

## When to use
Eleven MIT-licensed Claude skills that together work like a small sales team: record-keeper (logs emails and calls - the simple CRM), prospector (finds leads and drafts cold outreach), follow-up (keeps following up until a call is booked, stops at the first no), sales-coach (live call coaching), contract-writer, researcher, scheduler, pipeline, proposal-writer, win-back and forecaster.

This is the pack from the nocodealex "free Claude sales team" reel. Same author as library entry 05 (instagram-agent-skill), different repo. For Konsiar-style local outreach, prospector, follow-up and record-keeper are the natural starting trio.

## Free scope and limits
MIT licensed; no paid API, no signup, no CRM seats. Python 3.8+ only, nothing to pip install. Honest caveats, matching the reel's own "catch": nothing is sent, booked or signed without your approval - Claude drafts, you approve, and sending happens from your own accounts through connectors you choose. Cold email has legal rules (consent, identification, unsubscribe; the reel mentions a 50/day cap) - you own compliance. The sales-coach works from call captions you supply; tell people when captions are on. The skills share pipeline/deals.py, so keep all eleven together if you use the Python tools.

## What is included
The complete repository mirrored at the pinned commit: all 11 skill directories plus README and LICENSE - 45 files, hash-verified on intake by prepare_library.py.

## How to use
After preparation, name the skill and give real context, for example:

> Use prospector to draft first-touch emails for these five verified local businesses. Drafts only - do not send anything, and use only the facts I supply.

## Sources and reviewed revision
- Original repository: https://github.com/Jakeschincariol/closer-skill
- License: MIT.
- Reviewed commit: 0b0107690e202010710a59eb7d0b47d331255e59
- Reel that prompted this entry: https://www.instagram.com/reel/Df1nzcEn6PQ/ (nocodealex). The repo link sat behind a comment gate and was resolved independently; the 11-skill sales-team structure, live-call coach and draft-approval rule match the reel exactly, but creator provenance is not proven by a link.
- Checked: 17 November 2026.
