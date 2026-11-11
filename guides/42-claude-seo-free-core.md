# Claude SEO (free core)

## When to use
Audit technical SEO, content, structured data, sitemaps and page quality for a specific website. This is `AgriciDaniel/claude-seo`, the first project shown in the user-shared reel. It overlaps with the existing marketing pack's SEO audit, but is a separate specialist project, not a duplicate copy of that skill.

## How to use
Read the pinned `skills/seo/SKILL.md` and the relevant sub-skill. Start with a single page and request evidence, not a blanket rewrite:

> Review this page for technical SEO, content and schema using Claude SEO's free core. Show observed issues, distinguish measured results from estimates, and rank a small set of fixes. Do not deploy changes or connect any service.

If separately installed and configured in Claude Code, `/seo page <url>` is the single-page entry point; `/seo audit <url>` is the broader audit. The library itself does not create these commands.

## Setup and source intake
`prepare_library.py` retrieves selected audit skill Markdown, root README/license/privacy/security notes at commit `cca7e4a267991aca880efade1fd12e8498caf2ce` into `library/entries/42-claude-seo-free-core/upstream/`. These are reference instructions, not a runnable plugin installation. Scripts, runtime, agents, media, paid extensions and some referenced supporting files are not included. Use the original source for a complete setup if later approved; do not run the whole pack just because it appears in the upstream README.

The upstream public plugin setup is `/plugin marketplace add AgriciDaniel/claude-seo`, then `/plugin install claude-seo@agricidaniel-claude-seo`. `/seo setup` is a separate dependency/browser setup action. These are reference commands, not run here. Current requirements: Claude Code 1.0.33+ and Python 3.11-3.14; browser checks need its separate Chromium runtime. Existing Claude access/allowance is separate.

## Free scope and limits
The public source is MIT licensed; the README says the core works without API keys. Only no-key core audit guidance is reviewed here. Private Pro versions, DataForSEO, Firecrawl, Ahrefs, SE Ranking, Profound, image generation and other paid/API-dependent extensions are outside this entry. Google and backlink API integrations are not enabled or included as ready-to-use paths.

Without field data, lab estimates are not real-user Core Web Vitals and page inspection does not prove indexing. A scan is not a ranking or revenue guarantee. Audited content is processed through the Claude session; consult the source privacy note before supplying private pages. An audit does not authorize account connections, publication or site changes.

## Sources
- Original repository, README and MIT license: https://github.com/AgriciDaniel/claude-seo/
- User-shared reel: https://www.instagram.com/reel/DfioPDmHCCs/
- Checked: 11 November 2026. Reel star counts, timings and claims that all four tools must be installed are not adopted as facts.
