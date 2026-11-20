---
name: saved-reels-to-skills
description: Turn a backlog of saved short-form videos (Instagram reels, TikToks, Shorts) into individual Claude skills. Use when the user hands over an export or list of saved reels and wants them mined for repeatable workflows, tools and step-by-step processes, with the keepers written out as skills Claude can actually run. One pass per reel, then a pattern pass across all of them, then one SKILL.md per keeper. Never uses comment gates or DMs to obtain gated files; builds an original implementation from what is publicly shown and labels it as such.
---

# Saved reels to skills

Mine a saved-reels backlog and convert what is genuinely reusable into executable skills. Inspired by the "Doomscroller" reel by @seymourofdevin (source at the end). The promise of that reel: export your save list, review every reel, pull out the repeatable workflows, the tools people mention and the step-by-step processes buried in the content, and write the keepers as individual skills. This skill implements that pipeline as an original work.

## Inputs

Accept any of:

- A list of reel/post URLs (pasted, or from an Instagram data export's saved-media file).
- A folder of downloaded video files.
- A mixed backlog with notes.

If the user has not exported anything, say how: Instagram app, Your activity, Download your information, then the saved-media list. Never ask for their password and never log in as them.

## Pass 1: one reel at a time

For every item, capture a `Source` record:

1. The reel's own facts: creator handle, post URL, caption, on-screen text, and the spoken or demonstrated steps. Use the caption and the video itself; do not trust third-party summaries.
2. Extract, in the reel's own terms: the workflow (what goes in, what comes out, the ordered steps), every tool or app named, and any claims that would need checking (prices, limits, "free", performance numbers).
3. Mark gaps honestly: steps the reel skips, files locked behind a comment gate or DM, steps that only exist in the creator's head. A gap is recorded, never filled with a guess.

## Pass 2: patterns across the backlog

Cluster the per-reel records:

- The same tool or app named in several reels (a real signal it is worth one good skill, not five copies).
- The same workflow shown by different creators (dedupe to one skill; note the variants).
- Recurring themes that suggest one broader skill instead of many thin ones.

## Pass 3: keepers only

A reel becomes a skill only when all of these hold:

- It describes a repeatable process, not a one-off opinion or promo.
- The process is actionable from what is publicly shown, or the missing pieces are small and clearly marked.
- Its factual claims check out, or the skill carries the unchecked items as explicit caveats.
- Nothing requires a paid tool the reel hid; if a paid dependency exists, the skill names it and its free scope up front.

Everything else goes on a skipped list with a one-line reason (promo, duplicate, unverifiable, gated beyond recovery).

## Writing each keeper

One folder per keeper with a `SKILL.md` containing:

- Frontmatter `name` and a `description` that says what it does and when to use it, in trigger terms the user would actually say.
- The workflow as ordered steps with gates where the reel showed a human approval point.
- A rules section: free scope, verification duties, and the hard rule below about gates.
- An attribution section naming the source reel URL and creator, and stating this is an original implementation of publicly shown material, not the creator's file.

Present the keeper list back to the user before writing dozens of files: which reels became skills, which were skipped and why.

## Rules

- Never comment, DM, like or follow to unlock a gated file. If the real file is not publicly available, build an original implementation of the publicly described workflow and label it exactly that way.
- Do not transcribe or republish the creator's video, audio or caption beyond a short quoted reference. Skills encode the process, not the content.
- Claims from reels are leads, not facts. Verify load-bearing ones (costs, capabilities, limits) at the owning source before writing them into a skill.
- Adding a skill to a library is not installing or running it. Nothing here installs tools, creates accounts or posts anything.

## Attribution and scope

Workflow inspired by the Instagram reel about the "Doomscroller" skill by @seymourofdevin: https://www.instagram.com/reel/Df7epBulaN6/ (November 2026). The creator's own skill sat behind a comment gate and was not obtained; this is an original implementation of the publicly described pipeline (export saves, per-reel pass, pattern extraction, individual skills). No license is asserted over the creator's video or their skill; only this original text is included here.
