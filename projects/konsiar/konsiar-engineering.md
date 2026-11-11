# Konsiar: website verification and improvement

## How to use
Open only for a task in Konsiar. Supply current files/facts and use the reference for the requested draft or review. This is not an installable skill. Historical settings and prices are not current verified facts. Existing owner decisions and authority remain unchanged.

## Reference
PROJECT REFERENCE, NOT AUTHORITY TO ACT
Use only in the named project when requested. Importing this document does not authorize installs, account access, sends, timers, spending, publication or production changes. Inspect current files first. Dated observations and placeholders are not proof of current implementation. Latest owner instructions and confirmed settings win. Continue independent draft work while a consequential decision is pending. Use existing tools and free local/public resources only, never trials or paid APIs/MCPs. Keep secrets and live prospect/customer data outside this library.

You are working in what should be the Konsiar codebase. Follow these rules throughout:
- Verify everything in the repo before treating it as true. Nothing in this prompt is proof of implementation: not the stack, hosting, billing, integrations, or features. Where the repo disagrees with this prompt, the repo wins; report the difference.
- Some changes are approval-gated. Never do these without asking me first, with a rollback plan: rotating or changing secrets, DNS or mail-authentication (SPF/DKIM/DMARC) changes, removing noindex or making any route publicly indexable, moving or renaming live routes, enabling billing or paid signups, installing third-party skills or packages, adding analytics or third-party embeds, changing the design language, and any production deploy. Propose; wait for my answer.
- Legal and business wording is never invented. Where a decision is missing, keep the existing placeholder and list the decision you need. Missing answers never block unrelated engineering work.
- Finish with three lists: what you changed, what you could not verify, and what is waiting on my decisions.

0. VERIFY FIRST
Inspect the repo and report: actual framework and hosting, auth approach, whether Stripe or any billing is really wired, which Meta integrations actually exist and work, all routes and which are public, and what the privacy/terms pages promise versus what the code does. Do not implement anything in this section; just report.

1. LEGAL PAGES
The privacy policy and terms contain [FILL IN] placeholders. Replace each one only with a decision I have given you; until then, leave the placeholder and add the decision to your waiting list. Needed decisions include: data retention periods, contact email, postal address, plan names, prices, currency, trial and refund terms, deletion timelines after account closure, liability limits, indemnities, and governing law and venue. Separately, determine which markets and jurisdictions the service is actually offered in and what each one requires (for example disclosures, response times, or a grievance officer where the local rules call for one); flag those items for qualified legal review rather than drafting them yourself. Add last-updated dates once the pages are final. Keep the existing guard that paid signups stay closed until the billing section is complete. Check copyright and licensing on all images and assets used on the site.

2. SECURITY PASS
The Nov 5 review reported a homepage with a strict CSP (default-src 'self'), X-Frame-Options DENY, frame-ancestors 'none', nosniff, Referrer-Policy no-referrer, a restrictive Permissions-Policy, COOP/CORP and HSTS; confirm these headers go out on every route, not just the homepage. Then check: no API keys or secrets in the repo or git history (list any found for rotation, but do not rotate without my approval); all secrets in environment variables; admin routes protected; real authentication; per-workspace authorization so users can only access their own data; input sanitization; XSS protection; CSRF protection on every state-changing form and endpoint; secure, httpOnly, sameSite cookies; session expiry; rate limiting on sign-in, signup, reset and API endpoints; locked-down CORS; debug mode off; dependencies updated with vulnerability scan results triaged; no exposed files (.env, .git, backups, source maps); database access restricted and encrypted; passwords hashed with a modern algorithm and checked against known-breached lists; Instagram and WhatsApp tokens encrypted at rest; 2FA for workspace users if the stack supports it; /.well-known/security.txt with a security contact. For every inbound webhook (Meta, Stripe, anything else): verify the provider signature, protect against replay, and make processing idempotent. Report checks run, results, unresolved risks and untested areas; never imply complete security.

3. PUBLIC LANDING PAGE + SEO
The Nov 5 review reported konsiar.com opening on the sign-in form, the whole domain is noindex, and no sitemap.xml. Recheck those historical observations before deciding what remains. Propose a public landing page at / that presents Konsiar: headline, what it does, how it works, an expandable FAQ, and a sign-up call to action. Describe only features you verified in the repo; do not promise integrations or capabilities that do not exist, and do not publish pricing until I give you real plan names and prices. Sign-in moves to /login. Authenticated app routes, auth flows, password reset, and webhook endpoints must stay non-indexable. Removing noindex and going live with the new routes are approval-gated as above. Once approved: sitemap.xml referenced from robots.txt (keep the existing AI content-signal reservations), canonical tags, a unique meta title and description per public page, one H1 per page, correct heading hierarchy, alt text, Organization and SoftwareApplication schema markup, an OG image plus og:title, og:description and Twitter card tags, clean URL slugs, HTTPS everywhere, mobile responsiveness, compressed images, good Core Web Vitals, sensible internal links, and a pass over the site for broken links. Add custom 404 and error pages in the same design language. Give me the exact steps to verify the site in Google Search Console and submit the sitemap, and propose a backlink strategy as a plan only (no outreach without my approval).

4. UX ADDITIONS
Add the ones that fit Konsiar: password visibility toggle on every password field, clear form success and error states, loading states on all submits, hover states, sticky header on the landing page, skip-to-content link, mobile menu, scroll back-to-top on long pages, confirmation modals for destructive actions, copy-to-clipboard where useful (for example webhook or API URLs in the dashboard), and a print stylesheet for the legal pages. The theme toggle already exists; keep it. Skip what does not fit yet: cookie banner and UTM tracking only if analytics or cookies are actually added, floating contact button only once a contact channel exists, full site search only once there is enough content, scroll progress bars only on long-form pages.

5. ACCESSIBILITY, CONTENT AND THIRD PARTIES
Alt text on all images, color contrast to WCAG AA in both light and dark themes, every form and menu fully keyboard operable, visible focus states, clear button labels, no fake reviews or unsupported claims, real business details in the footer. Inventory all analytics tracking and third-party embeds currently on the site; report what each one loads and what data it touches, and remove or gate anything not needed (removals are approval-gated if they change behavior).

6. DESIGN TASTE
Two creator-shared skills were suggested as design inspiration: a "Taste Skill" and "MotionSites" (its "700+ designs" figure is the creator's claim, not verified). Treat them as inspiration for the visual direction only. Before installing or copying from any third-party skill, package, or design asset: inspect its source, license, copyright and dependencies, and ask me first.

7. OPERATIONS SAFEGUARDS THE REELS MISSED
Set up or propose, with paid services and production changes approval-gated:
- Automated database backups plus a tested restore procedure.
- Uptime monitoring and error tracking with alerts to me.
- Audit logging of account and settings changes per workspace.
- Transactional email deliverability for password resets and receipts: propose the SPF, DKIM and DMARC records for the sending domain (approval-gated) and test that reset mail does not land in spam.
- A staging or preview environment so changes are tested before production.
- Billing edges: dunning when a payment fails, grace-period behavior, and plan-limit enforcement that matches whatever the terms end up saying.
- Data export from the dashboard and a working account-deletion path, matching the privacy policy's promises.
- Automated tests for the critical flows: sign-in/signup/reset, webhook handling (including bad signatures and replays), authorization boundaries between workspaces, and any billing transitions. Run them and include the results as verification evidence.
- A short internal runbook: how to deploy, roll back, and rotate a leaked secret.

Security addendum (gaps not in master prompt v3, from the
checklist reel; verify stack applicability before changing code):

- Use parameterized database queries everywhere; validate all input
  explicitly and escape output by context.
- Protect against mass assignment: field allowlists on every write
  endpoint.
- Uploads: restrict types and sizes, define storage location and
  access rules.
- Minimize API responses: return only the data each screen needs.
- Add bot and abuse defense beyond basic rate limiting.
- Separate browser-safe publishable database keys from privileged
  server-only keys, and test row- and workspace-level authorization.
  "Use a public DB key" only ever means a publishable key, never a
  privileged key copied to the client.
