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
