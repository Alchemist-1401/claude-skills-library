# Skill catalog and usage guides

41 entries. For local source intake, use README.md and prepare_library.py. Individual usage files are also readable in guides/.


---

# Taste Skill

## When to use
Current skill: design-taste-frontend. Builds company websites with a consistent design system, real product UI, licensed photographs, copy checks and a browser finish gate. Local checks cover 1440, 1024, 820, 768 and 390 pixels. Requires Node 22+ and Chrome, Edge or Chromium; ffmpeg is optional. MIT licensed, no API keys. Sponsorships and optional paid services in the README are not required.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

You previously said Taste Skill was downloaded. Current installation is not checked. The old eqnxinv link is obsolete; use this repository. Start with: "Audit the existing Konsiar project, apply design-taste-frontend, and propose improvements without deploying."

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add https://github.com/Leonxlnx/taste-skill --skill design-taste-frontend
```

## What is included here
Pinned-source intake: 1482 selected upstream files are fetched by prepare_library.py into library/entries/01-taste-skill/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Leonxlnx/taste-skill
Repository: Leonxlnx/taste-skill
Pinned source commit: f6b76575f949707b4e3c37cd86cb44b0b98643e8
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# MotionSites Web Builder

## When to use
Builds cinematic landing pages: 40 reference designs, 50+ hero videos, 3D cutouts, 55+ motion recipes, and a screenshot-and-fix quality loop. License: MIT for the skill itself; its example prompts and media are (c) MotionSites - fine for building sites, including client work, not for reselling as a collection. A paid Unlimited tier exists but is not needed.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Already in the Nov 6 brief; the Nov 9 reel is a duplicate. Ask: "Audit this landing page, use the free bundled MotionSites material, then screenshot and fix the local preview. No paid library, MCP, account signup or deployment." Python/Playwright/Chromium can support local visual QA; no paid service is needed.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add Motionsites-AI/claude-skill
/plugin install motionsites-web-builder@motionsites
```

## What is included here
Pinned-source intake: 17 selected upstream files are fetched by prepare_library.py into library/entries/02-motionsites-web-builder/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Motionsites-AI/claude-skill
Repository: Motionsites-AI/claude-skill
Pinned source commit: faa30d512e3973e58675c72101a7ef42ed37ae83
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

Not mirrored (inspect source if required):
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/sheet-6.jpg
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/sheet-4.jpg
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/sheet-2.jpg
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/sheet-3.jpg
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/sheet-1.jpg
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/MEDIA.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/media/sheet-5.jpg
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/asme-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/3d-character-studio.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/INDEX.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/3d-collectible-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/modern-agency.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/mindloop-landing.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/neo-museum.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/prosthetics-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/portfolio-cosmic-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/intelligent-operations.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/email-landing-page.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/halo-usd-landing.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/retro-futurist.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/digital-epoch-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/equilibrium.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/creative-studio.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/stillmind.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/bloom-ai-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/velorah-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/neon-logic.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/digital-experiences.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/immersive-ocean.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/tech-forward.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/agent-wave.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/3d-jack-portfolio-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/mostar-guide.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/aethera-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/prisma-landing.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/intelligence-layer.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/vex-ventures-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/portal-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/aetheris-voyage-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/securify-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/bold-studio.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/interactive-discovery.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/ai-runtime.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/network-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/prompt-hero.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/contact-cybernetic.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/innovation-landing.md
- plugins/motionsites-web-builder/skills/motionsites-web-builder/examples/ai-workflow.md

---

# UI UX Pro Max

## When to use
The free, MIT-licensed repository provides UI styles, typography, color palettes, stack guidance and local design-system search. Python 3 is required; its search scripts use the standard library and make no network calls. A separate Premium product exists and is excluded. Use the open-source Basic version only.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Previously downloaded per your Nov 1 message; current installation is unverified. Run setup inside the intended project. Ask: "Use UI UX Pro Max to audit this dashboard and propose a design system, preserving all working behavior."

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx ui-ux-pro-max-cli init --ai claude
```

## What is included here
Pinned-source intake: 49 selected upstream files are fetched by prepare_library.py into library/entries/03-ui-ux-pro-max/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
Repository: nextlevelbuilder/ui-ux-pro-max-skill
Pinned source commit: 6ae86f61f520d6ca229d2f40e070410638c908c5
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Marketing skills pack (5 skills)

## When to use
The five reel skills are cold-email, sales-enablement, lead-magnets, prospecting and emails (formerly email-sequence). The pack is MIT licensed. Use them for writing, planning and reviewing material you supply: emails and follow-ups, sales collateral, lead magnets, prospect qualification and nurture sequences. Sending infrastructure, paid data providers and integrations mentioned upstream are not included or required for this draft-only route.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

From the Nov 8 cold-email reel. Start with: "Use cold-email to draft only, using these verified prospect facts and this offer. Do not send, buy data, create accounts or connect tools." No Instagram-DM adaptation has been built.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add coreyhaines31/marketingskills --skill cold-email sales-enablement lead-magnets prospecting emails -a claude-code
```

## What is included here
Pinned-source intake: 46 selected upstream files are fetched by prepare_library.py into library/entries/04-marketing-skills-pack-5-skills/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/coreyhaines31/marketingskills
Repository: coreyhaines31/marketingskills
Pinned source commit: 3e729622e3de0c82abdb906190d91f9018045872
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Instagram agent skill (13 skills)

## When to use
Thirteen skills that draft and quality-check Instagram content: reels written off 26 scored hook formulas, viral research that ranks what is working in your niche, a caption linter, a profile scorer, a week planner, and a humanizer that strips AI tells. Nothing gets posted until you say yes.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Run inside Velocitas only, never Konsiar or your personal account. Python supports the local tools; the source says no signup or API key is needed. Start with /ig-reel and supply a verified F1 topic and voice examples. This pack drafts and checks; it does not publish. Rights to F1 footage are not supplied.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
git clone https://github.com/Jakeschincariol/instagram-agent-skill.git
mkdir -p .claude/skills
cp -r instagram-agent-skill/skills/ig-* .claude/skills/
```

## What is included here
Pinned-source intake: 24 selected upstream files are fetched by prepare_library.py into library/entries/05-instagram-agent-skill-13-skills/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Jakeschincariol/instagram-agent-skill
Repository: Jakeschincariol/instagram-agent-skill
Pinned source commit: d03c56bb598be770c60b201f94237e5d1a4268a6
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Logo Design Skill

## When to use
Logo discovery, concepts, SVG construction, testing and a brand kit after you choose a direction. MIT skill; its Python tools use the standard library. The reference logos remain other people's trademarks, not assets to copy.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from your Oct 22 report, pick 1. No image-generation API is required. This does not mean any proposed Velocitas logo or palette has been approved.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add kaankiziltug/logo-design-skill
/plugin install logo-design@logo-design-skill
```

## What is included here
Pinned-source intake: 1464 selected upstream files are fetched by prepare_library.py into library/entries/06-logo-design-skill/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/kaankiziltug/logo-design-skill
Repository: kaankiziltug/logo-design-skill
Pinned source commit: bbf31e521d765eb6d53242549bbee7c2e5bbd6bc
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Ponytail

## When to use
A coding skill that favors existing components, small changes and necessary code, without dropping tests, error handling or accessibility. MIT; the core works in your existing coding assistant without another paid service.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from your Oct 22 report, pick 5. Treat the report's savings percentage as a test claim, not a promise for your projects. Current optional local dashboard features have their own host/version requirements.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add DietrichGebert/ponytail
/plugin install ponytail@ponytail
```

## What is included here
Pinned-source intake: 3 selected upstream files are fetched by prepare_library.py into library/entries/07-ponytail/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/DietrichGebert/ponytail
Repository: DietrichGebert/ponytail
Pinned source commit: 96608e078b2d5ea607c5c3b8b5a54d1c1fba6846
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# I Have ADHD

## When to use
Changes answer structure: action first, numbered steps and detail below. It is an output-format skill, not a medical tool. MIT; no separate service or API key is needed.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the full Oct 22 report. You did not select it in the original five picks; it is included now because this is the full qualifying library, not just that shortlist.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Install the i-have-adhd skill/plugin from https://github.com/ayghri/i-have-adhd, referring to the repository's AGENTS.md for the current installation instructions.
```

## What is included here
Pinned-source intake: 5 selected upstream files are fetched by prepare_library.py into library/entries/08-i-have-adhd/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/ayghri/i-have-adhd
Repository: ayghri/i-have-adhd
Pinned source commit: 1ecea1993b7fce257ffbd686c070948b5e07eda6
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Founder: Pricing Strategy

## When to use
Works through pricing models, tiers, unit economics and competitor prices. MIT skill in the Founder plugin. Planning from your supplied facts and publicly available research does not require a paid data service.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from your Oct 22 report, pick 12. The old commands/pricing-strategy.md link moved; the current plugin is the maintained route. Installing the plugin also exposes other founder skills. Estimates and competitor claims still need sources.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add emotixco/claude-skills-founder
/plugin install founder@emotix

Then use /founder:pricing-strategy
```

## What is included here
Pinned-source intake: 3 selected upstream files are fetched by prepare_library.py into library/entries/09-founder-pricing-strategy/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/emotixco/claude-skills-founder
Repository: emotixco/claude-skills-founder
Pinned source commit: ea6864c05c2f4a3666b9d6c14c550b20f35a04c9
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Caveman: the instruction-only skill

## When to use
Shortens replies while preserving technical facts, exact commands and negations. The standalone skills/caveman/SKILL.md is a free Apache-2.0 instruction file. It does not need the larger Caveman CLI, routing account or cloud service.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report. This is an existing upstream module, not a rewritten free substitute. The full current CLI has telemetry and optional cloud routing; those are outside this entry. No token-saving percentage is promised.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the upstream skills/caveman folder into .claude/skills/caveman in the intended project. Keep its SKILL.md unchanged. Use /caveman; use normal mode to turn it off.
```

## What is included here
Pinned-source intake: 6 selected upstream files are fetched by prepare_library.py into library/entries/10-caveman-the-instruction-only-skill/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md
Repository: JuliusBrussee/caveman
Pinned source commit: 3dc497a7f858c774d6e15b25e8c6120ef3a0eda8
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Apple Design

## When to use
Design and interaction guidance covering motion, typography, feedback, hierarchy and reduced-motion behavior. MIT, instruction-based; no Apple subscription, paid API or special hardware is required to use the guidance.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report and the later motion research. This is a community skill based on Apple's design ideas, not an Apple certification or a guarantee of a premium result.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add emilkowalski/skills --skill apple-design
```

## What is included here
Pinned-source intake: 3 selected upstream files are fetched by prepare_library.py into library/entries/11-apple-design/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/emilkowalski/skills/blob/main/skills/apple-design/SKILL.md
Repository: emilkowalski/skills
Pinned source commit: 715c1807e08c497cfd1dc4feb450a2a3300ef2a9
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# LottieFiles Motion Design

## When to use
Motion direction before implementation: timing, easing, choreography, emotional intent, UI patterns and quality checks. MIT, implementation-agnostic instructions; it does not require a paid LottieFiles account.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from your Oct 25 search for motion taste. Mainly written for UI animation. Its principles can guide EffectCraft work, but this is not an EffectCraft controller or a complete reel-production pipeline.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add LottieFiles/motion-design-skill
```

## What is included here
Pinned-source intake: 19 selected upstream files are fetched by prepare_library.py into library/entries/12-lottiefiles-motion-design/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/lottiefiles/motion-design-skill/
Repository: lottiefiles/motion-design-skill
Pinned source commit: f9a8a041b85185ee4881b3471d3415e939aac772
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# ArtCraft controls: EffectCraft, PhotoCraft, DesignCraft

## When to use
Three actual MIT SKILL.md folders teach Claude to operate the free, open-source creative apps you named: motion graphics, image editing and page layout. Each documents local CLI/control surfaces as well as optional local MCP access. No paid hosted MCP or AI-generation API is needed for these local editing workflows.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from Oct 25 and Nov 8. This preserves your PhotoCraft/DesignCraft choices; it does not replace them with browser rendering. The apps are alpha and can fail or lose format fidelity. Confirm the installed app/CLI version and test a small export first. Generative assets are not supplied by these editors.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Clone https://github.com/midasmatterhorn/artcraft-skills. Copy the complete effectcraft, photocraft and designcraft folders into the intended project's .claude/skills directory, preserving their references. Install the matching free ArtCraft apps separately if missing.
```

## What is included here
Pinned-source intake: 17 selected upstream files are fetched by prepare_library.py into library/entries/13-artcraft-controls-effectcraft-photocraft-designcraft/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/midasmatterhorn/artcraft-skills
Repository: midasmatterhorn/artcraft-skills
Pinned source commit: 27567a0df89f5260aadfa7b16aa2e8d14c16dfd5
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Bang Motion

## When to use
A real MIT skill for browser-based motion graphics, explainers and SaaS demos. Its native browser workflow is free; local MP4 export uses Node, Puppeteer and ffmpeg. No paid generator is mandatory.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

From your Nov 5 SaaS-demo reel and Nov 6 follow-up. Keep one copy only: plugin or manual folder. Optional After Effects/image/video MCP routes are not included in the free workflow. Asset and music rights remain your responsibility.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add bangtutorial/bang-motion
/plugin install bang-motion@bang-motion
```

## What is included here
Pinned-source intake: 31 selected upstream files are fetched by prepare_library.py into library/entries/14-bang-motion/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/bangtutorial/bang-motion
Repository: bangtutorial/bang-motion
Pinned source commit: c1aa65e921c970d858705fcb4a53a8294d1a4131
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Charlie Hills motion-graphics skills

## When to use
Native skills for brand intake, launch videos, reels, animated charts, loops, explainers and motion briefs. MIT; the source states no API key is needed. Local exports use HyperFrames or Chrome plus ffmpeg. This produces animation as code, not through EffectCraft.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from Oct 25 motion research. The current repo has 15 skills; model-showdown is outside this entry's free scope because it depends on access to other models. Its recommendation of a particular Claude model still uses your existing allowance, not free extra Claude capacity.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add charlie947/motion-graphics-skills

Select the workflows you need. Leave model-showdown unselected unless you already have every model account it needs.
```

## What is included here
Pinned-source intake: 18 selected upstream files are fetched by prepare_library.py into library/entries/15-charlie-hills-motion-graphics-skills/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/charlie947/motion-graphics-skills
Repository: charlie947/motion-graphics-skills
Pinned source commit: 229022ebca76972e119e36ada23a1648d51665ab
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Claude Motion: motion-design

## When to use
Concrete motion-design guidance for typography, pacing, easing, transitions and reading holds. The upstream .claude/skills/motion-design folder is an actual MIT skill, not just an animation library.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from Oct 25. Written for Remotion, not EffectCraft; do not pretend its code is interchangeable. Rendering is free for individual/small-team Remotion users under the eligibility rule in entry 18. No paid rendering cloud is included.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Clone https://github.com/whaleyxbt/claude-motion. Copy its complete .claude/skills/motion-design folder to the intended project's .claude/skills/motion-design, keeping any referenced files.
```

## What is included here
Pinned-source intake: 3 selected upstream files are fetched by prepare_library.py into library/entries/16-claude-motion-motion-design/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/whaleyxbt/claude-motion/blob/main/.claude/skills/motion-design/SKILL.md
Repository: whaleyxbt/claude-motion
Pinned source commit: 6f80380b91858dad66524a5b34e027dad656d538
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# LobzyJay: motion direction and critique

## When to use
The native motion-design and motion-design-critique skills cover design principles, composition, easing and review. MIT and usable as guidance without a paid application. They are the taste layer from the After Effects research, not a promise that After Effects itself is free.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from Oct 25. The repository now redirects to motion-design-with-claude-and-codex. The aftereffects-motion controller and its paid application are excluded; Blender's separate controller/MCP setup is not part of this entry. The exact Instagram creator you remembered was never identified.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Clone https://github.com/LobzyJay/motion-design-with-claude-and-codex. Copy only skills/motion-design and skills/motion-design-critique into the intended project's .claude/skills directory.
```

## What is included here
Pinned-source intake: 12 selected upstream files are fetched by prepare_library.py into library/entries/17-lobzyjay-motion-direction-and-critique/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/LobzyJay/motion-design-with-claude
Repository: LobzyJay/motion-design-with-claude-and-codex
Pinned source commit: a4d48c55ccb54a3b8bc4e100e34f6dcaca3bbfea
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Remotion best practices

## When to use
The official skills repository teaches code-driven video work. Local Remotion rendering is free for an individual, or an organization/team with at most 3 people, including commercial work. No signup or paid cloud rendering is required for that eligible local route.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

From the Oct 22 report and later ad-toolkit research. This is conditional free licensing, not a universal free license: recheck the entire organization's headcount before using it after growth or inside a larger client organization. License terms: https://www.remotion.dev/docs/license/faq

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add remotion-dev/skills
```

## What is included here
Pinned-source intake: 0 selected upstream files are fetched by prepare_library.py into library/entries/18-remotion-best-practices/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.

No standalone redistribution license found in the source checkout; official setup remains source-linked.

## Source and attribution
Source: https://www.remotion.dev/docs/ai/skills
Repository: remotion-dev/skills
Pinned source commit: 1fc074b74b95cfecf7b1e419132f2cfe23dafebe
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Real SFX

## When to use
An actual Claude Code skill for placing recorded sound effects against video cues while retaining music and voice. Scripts are MIT; the bundled 78 UI sounds are CC0. Python 3.9+ and ffmpeg are local requirements. A separate paid sound library is not required to start.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

From the Nov 7 sound-design reel. This was previously left unverified; the linked source README now confirms the script and sound licenses. The small bundled pack does not supply every whoosh, hit or music track. Check licenses for any additional sound. A quiet gap is better than unlicensed audio.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Download the free real-sfx.skill package from the source page, or copy the complete real-sfx folder from the linked Clipwing repository into .claude/skills/real-sfx. Point it to your licensed sounds, or start with the bundled UI cues.
```

## What is included here
Pinned-source intake: 0 selected upstream files are fetched by prepare_library.py into library/entries/19-real-sfx/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.

Use official .skill download; sound/script redistribution terms stay with that source.

## Source and attribution
Source: https://clipwing.pro/skills/real-sfx
Repository: Not applicable
Pinned source commit: Not applicable
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# earshot: audio review and real-sound skills

## When to use
The repository includes actual earshot and real-sound SKILL.md folders, alongside its local CPU audio tools. MIT; the core CLI can measure, compare, review and make sound without a paid API. Initial open-model downloads are about 1.1 GB.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

From the Nov 7 sound-design reel. Use the documented local CLI or Python route; local MCP is optional. Do not use the optional earshot llm/Gemini upload feature. Real-sound still needs owned or free-licensed recordings and music, not a paid library.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
uv tool install "earshot[mcp] @ git+https://github.com/Leonxlnx/earshot"
earshot doctor --fetch

Also copy the repository's complete skills/earshot and skills/real-sound folders into the intended project's .claude/skills directory.
```

## What is included here
Pinned-source intake: 36 selected upstream files are fetched by prepare_library.py into library/entries/20-earshot-audio-review-and-real-sound-skills/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Leonxlnx/earshot
Repository: Leonxlnx/earshot
Pinned source commit: 4ac3d2ac2b151e1c23376f9ce7f3047a17050013
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Claude Watch: no-Whisper mode

## When to use
A real MIT /watch skill that extracts scene frames and native captions from public videos or local files. The upstream --no-whisper option disables paid transcription. yt-dlp and ffmpeg are the local requirements.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report. This is its documented free mode, not a custom rewrite. Without captions, it becomes frames-only and cannot claim to know the spoken content. It does not solve Instagram login walls. Native captions may also be wrong.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add taoufik123-collab/claude-watch
/plugin install watch@claude-watch

Use /watch with --no-whisper. Do not set Groq/OpenAI transcription keys.
```

## What is included here
Pinned-source intake: 21 selected upstream files are fetched by prepare_library.py into library/entries/21-claude-watch-no-whisper-mode/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/taoufik123-collab/claude-watch
Repository: taoufik123-collab/claude-watch
Pinned source commit: 7711231e4c47e5d4e06bcf5326c4abf5b70ab4a9
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Brag

## When to use
Turns a project into a launch video and share copy. The current MIT skill supports a local Node/ffmpeg/HyperFrames workflow; voiceover is optional and off by default. The hosted letsbrag.app service is separate and is not part of this entry.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report. That report's historical per-run cost is not the current local skill's price. The upstream now also includes brag-slim for its named Claude model. No paid image/video generation service is needed for the documented local workflow.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
/plugin marketplace add latent-spaces/brag
/plugin install brag@brag
```

## What is included here
Pinned-source intake: 26 selected upstream files are fetched by prepare_library.py into library/entries/22-brag/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/latent-spaces/brag
Repository: latent-spaces/brag
Pinned source commit: 669ab9286aa28b6c3ee30e75f181ee74319d012a
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Agent Reach: public-reading scope

## When to use
The repository contains a real agent-reach SKILL.md plus a local retrieval toolkit, under MIT. Its documented default public channels include web, GitHub, V2EX, YouTube metadata/search/captions and Bilibili public content without a paid API key.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Your Oct 22 pick 9. This is not an offline skill or a guarantee of social-site access. Optional logged-in channels can copy browser sessions and risk account restrictions; they are outside this entry's scope. YouTube speech transcription needs a provider key and is excluded. No browser/account setup has been performed.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Give Claude the official install guide from https://github.com/Panniantong/Agent-Reach and review the proposed local setup. Use only its default public-reading channels; do not add transcription keys, paid proxies or paid fallback services.
```

## What is included here
Pinned-source intake: 7 selected upstream files are fetched by prepare_library.py into library/entries/23-agent-reach-public-reading-scope/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Panniantong/agent-reach
Repository: Panniantong/agent-reach
Pinned source commit: c70ae6da5d39bc90e09ad2ae0575ccc89f31e284
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Lisaan-al-Dawat Companion

## When to use
Your supplied ZIP is a real skill bundle: SKILL.md, writing/register guides, an unofficial Qamoos, page-marked textbook text and a standard-library dictionary lookup tool. It works locally without a paid API. It is a study aid, not an official grammar or proof of fluency.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

The exact 3,568-byte SKILL.md is preserved below, unchanged. The original ZIP itself could not be recovered for rehosting here; this text alone is not the complete package. Personal study/assistant setup only. The restricted Al-Kanz font is not included or required for plain-text use. Do not redistribute the corpus or assume font rights.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Use your original lisaan-al-dawat-companion.zip from Oct 28. Unzip it and copy the complete folder to ~/.claude/skills/lisaan-al-dawat/ so SKILL.md is directly inside that folder. Keep reference, dictionary, corpus and tools beside it.
```

## What is included here
Pinned-source intake: 0 selected upstream files are fetched by prepare_library.py into library/entries/24-lisaan-al-dawat-companion/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: Original user-requested authored skill
Repository: Not applicable
Pinned source commit: Not applicable
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

Incomplete: SKILL.md alone cannot replace the unavailable dictionary, corpus, reference files and helper tools. Do not activate this incomplete copy. Use the original Lisaan ZIP.

---

# Konsiar motion-reels v2

## When to use
The original custom project skill plus its five reference files, recovered unchanged. It covers hooks, storyboard, motion, sound, real product proof and export checks. Its original tool choices are preserved; the documented local Bang Motion/EffectCraft routes are free. It is private project guidance, not a third-party plugin.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

v1 is superseded by this v2, not duplicated. The two Nov 6 screen recordings were analyzed without audio; their exact correspondence to the two Reel URLs remains unconfirmed. This is not the pending PhotoCraft/DesignCraft/Zernio autopublishing adaptation, and none of those choices has been replaced.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the original files below to their marked paths in the Konsiar project only. Start a fresh Claude Code session. Do not install the retired Velocitas version alongside its newer Instagram pack.
```

## What is included here
Pinned-source intake: 0 selected upstream files are fetched by prepare_library.py into library/entries/25-konsiar-motion-reels-v2/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: Original user-requested authored skill
Repository: Not applicable
Pinned source commit: Not applicable
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# REA: reverse-engineer-anything

## When to use
The repository includes a real MIT reverse-engineer-anything skill and a local analysis toolkit. Static JavaScript analysis needs no native analysis engine; Ghidra is an available free native-analysis path. Neither route requires a paid model API or a paid hosted MCP service beyond your existing assistant.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Recovered from the Oct 22 report. Not a skill-only install: its documented setup registers a local MCP server. Paid analysis engines are optional, not part of this entry. Use it only on software you are authorized to inspect; MIT licensing does not grant rights over someone else's app.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx rea-agents setup

Review the local server and skill configuration changes before approving. Use static JavaScript analysis, or a separately verified free Ghidra setup; never choose a Hopper/IDA trial or paid license as a hidden dependency.
```

## What is included here
Pinned-source intake: 12 selected upstream files are fetched by prepare_library.py into library/entries/26-rea-reverse-engineer-anything/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/morluto/rea
Repository: morluto/rea
Pinned source commit: dcdae135435eb9c3c56e5e50116ab5da812a5409
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Velocitas Triple Hook - original adaptation

## When to use
A focused, instruction-only skill for F1 openings: immediate context, a curiosity lean and a supported contrarian snapback, followed by an actual payoff. It complements the existing reel/Instagram skills rather than replacing the production workflow. Includes original illustrative F1 examples and a carousel adaptation. No mandatory API, MCP service, trial, credits or additional software. Existing Claude access and allowance still apply.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Authored on 9 Nov at your request, after inspecting the full 2:14 Kallaway reel. This is our original adaptation, not a creator-supplied skill or his separate gated training. Rejects unsupported scientific/guaranteed-growth claims, forced reversals, fake analytics and unverified race facts. Keeps no-black-background and current project boundaries. No posting or automatic cadence authorized.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Open the complete skill disclosure below. Copy all text and save it as .claude/skills/velocitas-triple-hook/SKILL.md inside Velocitas only. All examples and source notes are inline, so no ZIP is required. Compare and back up any existing folder first; do not overwrite velocitas-reels or the Instagram pack. Nothing is installed by this page.
```

## What is included here
Pinned-source intake: 0 selected upstream files are fetched by prepare_library.py into library/entries/27-velocitas-triple-hook-original-adaptation/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://www.instagram.com/reel/De_5mQ0R8PE/
Repository: Not applicable
Pinned source commit: Not applicable
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Content Principles by Remy Gaskell

## When to use
A creator-published, instruction-only Claude skill for writing or reviewing short-form scripts, hooks and social posts. Covers one specific viewer, value versus time cost, line-by-line progression, curiosity loops, concrete detail, simple explanations, early payoff, removing fluff, objections and visual rhythm. No scripts, MCP, API keys, credits, signup or paid add-ons are required. Existing Claude access and allowance still apply.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

From your 9 Nov aiwithremy reel. The full 1:01 audio and visuals were inspected; its title, author and methods match this public repository. Distinct from entry 27: broader script reasoning, not another copy of Triple Hook. Use principles as flexible guidance, as the source itself says. The creator reports 500+ research hours, 1.8M views and 12,000 additional followers; no causal evaluation or independently verified analytics was supplied. The repository has no explicit license file at review, so link to the original rather than rehost its full text or imply redistribution rights. Public download requires no keyword comment or DM. Martin Wang companion added 9 Nov: the overlapping hook/message ideas are consolidated here, not counted as another entry. Open the original adaptation below for an experience-first message audit; the Remy source remains linked and unchanged.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Open the original repository below. Copy its content-principles folder into .claude/skills/ inside the intended project, so content-principles/SKILL.md is present. Review it first and back up any existing folder. For Velocitas, use only that project, not your personal account. Nothing is installed by this page.

Try: Use content-principles to review this verified F1 script for a beginner viewer. Improve its reasoning and payoff without forcing a template. Do not invent race facts, statistics or growth claims; do not post.

Optional Martin Wang companion: open the original message-audit disclosure, copy all text and save as .claude/skills/content-message-audit/SKILL.md inside the intended project. Review and back up an existing folder first. This is our adaptation, separate from Remy's source. Do not post or install automatically.
```

## What is included here
Pinned-source intake: 0 selected upstream files are fetched by prepare_library.py into library/entries/28-content-principles-by-remy-gaskell/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.

No redistribution license found for Remy source. The authored message-audit companion is included separately.

## Source and attribution
Source: https://github.com/aiwithremy/content-principles
Repository: aiwithremy/content-principles
Pinned source commit: 18f96703c98763b9c3bd647a46f2e031bda4a29d
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

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
Pinned-source intake: 22 selected upstream files are fetched by prepare_library.py into library/entries/29-cloudflare-security-audit/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/cloudflare/security-audit-skill
Repository: cloudflare/security-audit-skill
Pinned source commit: c1c8a8c1471069fb0e188eeaff69b8e8db6564a8
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Matt Pocock: reviewed engineering skills

## When to use
MIT-licensed instruction skills. Reviewed subset: tdd, codebase-design, grilling and its grill-me entry point. TDD tests agreed public interfaces one slice at a time; codebase-design supplies module/interface vocabulary; grilling stress-tests decisions. Uses existing project tools and coding-agent allowance, without a required external API or MCP.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

The reel names a repository, not one skill. Only this reviewed subset is included; the remaining pack is not blanket-certified free or appropriate. TDD requires agreement on test seams; grilling stops for your decisions. Preserve your existing workflow.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Download https://github.com/mattpocock/skills into a separate reference folder. Copy only skills/engineering/tdd, skills/engineering/codebase-design, skills/productivity/grilling and skills/productivity/grill-me, with their reference files, into this project’s .claude/skills/. Do not install the whole plugin as a second copy.
```

## What is included here
Pinned-source intake: 14 selected upstream files are fetched by prepare_library.py into library/entries/30-matt-pocock-reviewed-engineering-skills/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/mattpocock/skills
Repository: mattpocock/skills
Pinned source commit: 4ae2317ddb22b046e26455e4f9c9b3aaaf62212d
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Impeccable

## When to use
Apache-2.0 design skill for improving existing interfaces: critique, accessibility/responsive audits, polish and local deterministic checks. Its local engine does not require a model API key. Node is needed for the installer; the engine binary ships with the skill or downloads once. Uses your existing coding model.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Choose this for an existing interface, not as permission to redesign everything. Overlaps the design purpose of Taste Skill, Hallmark and UI UX Pro Max, but is a distinct source. Pick one lead design skill rather than issuing conflicting design systems.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx impeccable install
Choose project scope and your actual coding tool. Review the optional hook before enabling it; do not change global settings without approval.
```

## What is included here
Pinned-source intake: 61 selected upstream files are fetched by prepare_library.py into library/entries/31-impeccable/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/pbakaus/impeccable
Repository: pbakaus/impeccable
Pinned source commit: c1e0e5492fbb524f5df84d635ecfae7dc438ec45
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Everything Claude Code: coding-standards only

## When to use
MIT-licensed local coding-standards skill reviewed for naming, readability, error handling, TypeScript/React examples and maintainability. Use as instruction-only code review, with your existing model. Its illustrative API/database examples do not require buying those services.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Upstream is now named ECC and contains much more than skills. Only coding-standards is verified and included here. Pro/private-repo services, external API/MCP integrations, extra model providers and the rest of the pack are outside this free core. Simplicity overlaps Ponytail; no duplicate Ponytail text is copied.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Download the repository from the source link. Copy only skills/coding-standards/ into this project’s .claude/skills/coding-standards/. Read SKILL.md and use it to review supplied code. Do not run the full installer or enable hooks/MCPs.
```

## What is included here
Pinned-source intake: 3 selected upstream files are fetched by prepare_library.py into library/entries/32-everything-claude-code-coding-standards-only/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/affaan-m/everything-claude-code
Repository: affaan-m/everything-claude-code
Pinned source commit: d2ef2680594f9a17526a6e1a2e18b3d242c5d17b
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Anatomy

## When to use
MIT-licensed agent skill that builds interactive isometric explanations of machines and systems in SVG, with optional WebGL and 3D effects. Node 20.10+ and Chrome/Chromium support building and visual checks. Core kit uses Node built-ins, with no API key or npm dependency; React 18+ is needed only for React output.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Project-local install, not global. Useful for technical explainers, not a general chart library. Accurate dimensions and relationships need sources; attractive geometry is not evidence the explanation is correct.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add wheresryan22/anatomy -a claude-code
```

## What is included here
Pinned-source intake: 132 selected upstream files are fetched by prepare_library.py into library/entries/33-anatomy/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/wheresryan22/anatomy
Repository: wheresryan22/anatomy
Pinned source commit: 1482e8469b0a9e0d8cc18ea2740a01423d29ae80
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Hallmark

## When to use
MIT-licensed design skill with theme directions, original page composition and anti-generic-design checks. Node 18+ supports installation; browser checks need local puppeteer-core and Chrome. Static checks alone do not verify the finished page. No mandatory paid API or hosted MCP in this scope.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Distinct source, with overlap in design goals. Do not stack it with other design systems blindly. Use audit for review; redesign an existing site only when you request that. Use bundled/openly licensed imagery and retain required photo credits, not a paid image service.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
npx skills add nutlope/hallmark
For full local browser checks, install puppeteer-core in the intended development environment and provide Chrome. Read upstream setup before running its checker.
```

## What is included here
Pinned-source intake: 139 selected upstream files are fetched by prepare_library.py into library/entries/34-hallmark/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/Nutlope/hallmark
Repository: Nutlope/hallmark
Pinned source commit: 04977e15f3dfd6ee4b74c887dac3eb52665d6c92
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Addy Osmani: source-driven development

## When to use
MIT-licensed source-driven-development skill. Checks the project's framework versions, reads the relevant official documentation, follows current patterns and cites sources. This reviewed instruction-only scope needs no paid API or MCP. Existing web-reading access is required for fresh documentation.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Distinct source, with overlap in coding discipline. This entry is only source-driven-development, not all 25 skills, browser DevTools MCP, model-routing, deployment or the full plugin. Use it to verify choices inside the intended project; it does not authorize changing outreach or shipping anything.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy skills/source-driven-development/SKILL.md from the source repository into .claude/skills/source-driven-development/SKILL.md in the intended project. Review any referenced companion skills before adding them. Do not install the whole plugin for this subset.
```

## What is included here
Pinned-source intake: 3 selected upstream files are fetched by prepare_library.py into library/entries/35-addy-osmani-source-driven-development/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/addyosmani/agent-skills/
Repository: addyosmani/agent-skills
Pinned source commit: 301b02b12bff98e4688e6984af6556802322bbde
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

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

---

# Karpathy-inspired coding guidelines

## When to use
The repository includes an actual karpathy-guidelines/SKILL.md, not only CLAUDE.md. MIT, instruction-only: surface assumptions, avoid unnecessary abstractions, make surgical changes and define verifiable success criteria. No mandatory API, MCP, signup or extra software.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Community guidelines derived from Andrej Karpathy's observations, not an official Karpathy product or endorsement. Overlaps Ponytail and existing engineering skills in purpose, but is a distinct source. Choose one lead workflow instead of stacking competing rules. Never overwrite a project's existing CLAUDE.md blindly.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy skills/karpathy-guidelines/SKILL.md from the repository into .claude/skills/karpathy-guidelines/SKILL.md in the intended project. Preserve existing project instructions. No full plugin or global install is needed for this scope.
```

## What is included here
Pinned-source intake: 2 selected upstream files are fetched by prepare_library.py into library/entries/37-karpathy-inspired-coding-guidelines/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/multica-ai/andrej-karpathy-skills
Repository: multica-ai/andrej-karpathy-skills
Pinned source commit: 2c606141936f1eeef17fa3043a72095b4765b9c2
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Anthropic: frontend design and webapp testing

## When to use
Reviewed two Apache-2.0 skills: frontend-design for deliberate visual choices and webapp-testing for local browser checks. Frontend design is instruction-only; webapp testing uses Python, Playwright and a locally installed Chromium browser, plus its bundled helper scripts. No mandatory paid API, hosted MCP or stock-asset service.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Official Anthropic repository, but its examples are educational and need testing in your own environment. This entry does not approve the entire pack, claude-api, MCP builder, paid Claude plan upgrades or any purchase. Frontend-design overlaps the design sources already here: use one lead design system and redesign only when requested.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the complete skills/frontend-design and skills/webapp-testing folders, including LICENSE.txt, scripts and examples, into .claude/skills/ in the intended project. For local browser testing install the free Python Playwright package and Chromium as upstream documents. Review scripts and run their --help before use. Do not install example-skills wholesale for this subset.
```

## What is included here
Pinned-source intake: 10 selected upstream files are fetched by prepare_library.py into library/entries/38-anthropic-frontend-design-and-webapp-testing/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/anthropics/skills
Repository: anthropics/skills
Pinned source commit: 2c5958ecac7cee2b583967a2c4981d0f4a75c579
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

# Superpowers: debugging and verification

## When to use
Two reviewed MIT skills: systematic-debugging finds root causes before fixes; verification-before-completion requires fresh test/build evidence before claiming success. They are local instructions and supporting techniques, with no mandatory paid API or MCP. Tests use the project's existing language/runtime.

## How to use
Read the entry description and scope below. For a task, supply the actual project/input and ask Claude to use this skill for that task. Start with a draft or local review. Setup is separate from use.

Subset only, not the full autonomous framework. Keep the complete debugging folder and review its cross-references to test-driven-development before use. Existing Matt Pocock TDD covers a related purpose; avoid adding a second whole TDD workflow by default. No automatic implementation, commits, deployment, new accounts or spending is authorized.

## Setup in the intended project
These are the curated source's setup notes, not a script to run on import. Do not run the whole pack when this entry names a subset.

```text
Copy the complete skills/systematic-debugging and skills/verification-before-completion folders from the repository into .claude/skills/ in the intended project. Preserve the supporting debugging references and helper files. Review them before execution. Do not install the full Superpowers plugin merely to use this subset.
```

## What is included here
Pinned-source intake: 9 selected upstream files are fetched by prepare_library.py into library/entries/39-superpowers-debugging-and-verification/upstream/. They are not hosted as loose files in this repository. Authored texts, when available, are in authored/. This is not a complete plugin installation; optional rendered/media assets and dependencies may need the original source.



## Source and attribution
Source: https://github.com/obra/superpowers
Repository: obra/superpowers
Pinned source commit: 22f0b463e7a5e579904dd6211a520321035526f7
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.

---

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

---

# Seven psychology rules for selling

## When to use
A compact lens for writing or reviewing sales copy, DMs, pitches, objections and follow-ups. This is a new reel-derived authored skill, separate from the broader marketing pack, outreach project reference and content-message audit. It is not a claim that seven rules explain every buyer.

## How to use
Read `authored/seven-psychology-rules-selling/SKILL.md`, then give Claude the actual draft or task and any confirmed audience/offer facts. For example:

> Use seven-psychology-rules-selling to review this pitch. Suggest the smallest useful edit. Treat the seven ideas as hypotheses, preserve the actual offer and existing follow-up cadence, and do not invent facts or send anything.

Use it as a lens, not a rigid script. Take stated budgets, objections and refusals at face value. Proof, trials and guarantees must already be real, available and authorized. Existing sending approval scope remains unchanged.

## Setup and local intake
The complete authored skill is a normal Markdown file in `authored/seven-psychology-rules-selling/SKILL.md`. No upstream installer, account, dependency, API key or paid service is required to read or apply it. Existing Claude access/allowance is separate.

The standard `prepare_library.py` intake copies this guide and the authored skill into one new library folder with checksum verification. It does not activate skills or alter any project, outreach cadence, price or sending permission. To use it, point Claude to the file for the current task. Any later installation into a project's skill folder is a separate choice.

## Source and scope
Paraphrased from the user-shared reel "7 Psychology rules for selling anything to anyone" by @builtformoresis: https://www.instagram.com/reel/DcoEwqwRTcU/

These are one creator's rules of thumb, not established universal buyer facts. The recovered reel supplied no study citations; the creator's income claim is not used as evidence. The skill preserves attribution and does not reproduce the video, transcript or promotional income claims. No license for the original video is asserted. Only the newly authored paraphrase is included here; no external download is needed.

Checked: 11 November 2026. No manipulation, fake urgency, invented scarcity, exaggerated pain or new promises. A refusal or opt-out ends the pitch.
