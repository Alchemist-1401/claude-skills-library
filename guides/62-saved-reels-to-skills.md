# Saved reels to skills

## When to use
Turn a backlog of saved reels (or TikToks/Shorts) into individual Claude skills. Use when you hand over an export or list of saved videos and want them mined for the repeatable workflows, tools and step-by-step processes inside, with the keepers written out as skills Claude can actually run. This is the pipeline the "Doomscroller" reel describes, implemented as an original skill.

## How to use
Read `authored/saved-reels-to-skills/SKILL.md`, then hand over the backlog, for example:

> Use saved-reels-to-skills: here is my Instagram saved-media export (or this list of reel links). Review every one, pull the patterns, and write the keepers as skills. Show me the keeper and skipped lists before writing files.

Three passes: one reel at a time (caption, on-screen text, demonstrated steps, every tool named, gaps recorded honestly), then a pattern pass across the whole backlog (same tool in several reels, same workflow from different creators, dedupe), then keepers only: repeatable, actionable, fact-checked, free scope named. Each keeper becomes its own folder with a SKILL.md; skipped reels get a one-line reason.

## Setup and local intake
A normal Markdown file in `authored/saved-reels-to-skills/SKILL.md`. No installer, account, dependency, API key or paid service. Exporting your save list is your own action in the Instagram app (Your activity, Download your information); the skill never logs in as you, and it never comments, DMs, likes or follows to unlock gated files. The standard `prepare_library.py` intake copies this guide and the authored skill with checksum verification; it does not activate anything.

## Source and scope
Authored for this library from the user-shared reel by @seymourofdevin: https://www.instagram.com/reel/Df7epBulaN6/ ("Somebody built a skill that turns them into workflows Claude can actually run. It is called Doomscroller... goes through every single one... pulling patterns... written out as individual skills Claude can execute."). The creator's own skill sat behind a comment gate ("Comment REELS") and was not obtained; this is an original implementation of the publicly described pipeline. No license over the creator's content is asserted.

Checked: 19 November 2026.
