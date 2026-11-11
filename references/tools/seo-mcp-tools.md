# SEO reel: local MCP tool references

These are the two tools in the user-shared reel https://www.instagram.com/reel/DfioPDmHCCs/ . They are kept separate from the skill catalog: an MCP server is software that exposes tools, not just a reusable instruction file. No server, package or account connection was installed here. Source links only; the library intake copies this reference, not the servers.

## Chrome DevTools MCP

Original: https://github.com/ChromeDevTools/chrome-devtools-mcp

Use it to inspect a live Chrome page, collect a performance trace and debug concrete browser problems. Example after a separately approved setup:

> Measure this public page's loading performance in a clean browser. Show the recorded bottleneck and distinguish lab results from field data. Do not change the site or access unrelated tabs/accounts.

The source provides an MCP configuration using `npx` and the `chrome-devtools-mcp` package. Inspect and select a version before configuration; do not blindly execute a moving `@latest` command from this library. Requirements are Node.js LTS, npm and supported Google Chrome. Source license: Apache-2.0. Reviewed source commit: `eb4b53d1621b906c1c2a323d3460f0f988d169db`.

The local server has no required paid API/subscription in this reviewed browser-debugging path; Claude access is separate. It can inspect and modify browser data. Use a dedicated browser context and do not expose sensitive sessions without a scoped decision. Usage statistics are enabled by default; `--no-usage-statistics` disables them. Performance tools may send trace URLs to Google's CrUX API; `--no-performance-crux` disables that path. Neither setting was changed here. The current repository also includes genuine companion skills; they depend on the server or CLI and are not activated by this reference.

## Search Console MCP

Exact project shown in the reel: https://github.com/saurabhsharma2u/search-console-mcp

Use it for a site's actual Google Search Console data only after selecting the right account and verified property. Example after a separately approved read-only setup:

> Compare this verified property's clicks, impressions and CTR across two comparable periods. Separate observations from possible causes. Do not submit URLs, change sitemaps, add/remove properties or request additional scopes.

The source's setup entry is `npx search-console-mcp setup`, followed by adding the server to the MCP client. That command opens Google authorization and stores credentials; it was not run here. Choose the intended Google account/property, review access scopes and keep the default read-only scope for analysis. Source license: MIT. Reviewed version: 2.1.4, commit `7de2215cc81c82c65213719b7d0ad411d8fc06a1`.

This is a local open-source tool reference, not a hosted paid MCP subscription. The reviewed Search Console path needs an authorized existing Search Console property and API access; it is not evidence that the owner has connected one. API quotas and Google's current conditions apply. Other engines, AdSense and write/indexing features are outside this reference's scope. The repository says writes require separate authorization. Do not connect accounts or expand permissions just to make an audit work.

Real clicks do not instantly validate a fix. Compare adequate time windows and account for seasonality, reporting delay and other changes; correlation does not prove cause. The project's AI-query insights are custom heuristics, not an official Google/Bing AI-citation feed. Indexing submission is not a guarantee of indexing.

## Together

Start with one relevant SEO skill or a public-page review. Add measured browser evidence when useful, and authorized Search Console data when available. All four are not prerequisites for doing any SEO. Keeping them in the library does not install them, spend money or grant access. Checked 11 November 2026.
