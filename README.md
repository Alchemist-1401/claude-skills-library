# Your Claude skills library

One private home for 39 curated skill entries and eight separate project references. Some entries contain several skills. Free scopes and exclusions are preserved. Adding a skill here does not install or run it on your device.

## Start with Claude

Give Claude this repository link and say:

> Read README.md, CLAUDE.md and CATALOG.md. Prepare the library in one local folder if needed. For my task, select only the relevant reviewed skill and its usage guide. Keep Konsiar, Velocitas, outreach and personal work separate.

Claude must have authenticated access to this private repository. A link alone does not grant it access. Use Claude's connected GitHub access where supported, or an authenticated local clone with Claude Code. Do not make the repository public or paste credentials into a prompt.

## Organized intake, not automatic installation

1. Clone or download this repository into one dedicated folder, such as `~/Claude-Library`.
2. Read `CATALOG.md`. Each numbered entry has its own usage guide and scoped source package.
3. For a local copy, `python3 prepare_library.py` verifies and expands the packages into `library/` inside this folder. It does not install dependencies, enable skills, edit other projects or run upstream code.
4. Read the chosen entry's README, then use or set up that skill only in the intended project. Do not copy this whole library into `.claude/skills`.

The package is split into numbered archive parts in packages/. Keep all parts together; the script handles them and verifies hashes.

The preparation script refuses to overwrite an existing `library/`. For an update, keep your existing working copy and compare it with a new prepared copy; do not delete a modified library blindly.

## Layout

- `CATALOG.md` - all 39 entries with full individual usage guides.
- `CATALOG.md` sections - usage, dependencies, free scope, source and pinned revision per entry.
- `library/guides/` - individual guide files after local preparation.
- `packages/` - scoped source snapshots, licenses, authored skills and separate project references, packaged to keep intake together.
- `manifest.json` - package hashes and file counts.
- `prepare_library.py` - local-only, standard-library extraction into one folder.
- `library/` - created locally after preparation; not a global skills install.

## Honest limits

- Lisaan's exact skill text is recovered, but the original dictionary/corpus/reference ZIP is missing. Its entry is incomplete, not ready to activate.
- MotionSites example/media collections are not redistributed. Its permitted skill code is included; retrieve permitted assets from the original source as needed.
- Remotion, Remy's Content Principles and Real SFX keep source-linked setup where redistribution permission was not established. They still have individual usage instructions. Remotion runtime free use depends on organization size.
- The hosted Motion MCP skill, paid API/trial paths, screenshot-to-code app, paid service directories, private prospect data and superseded duplicate skills are not added as active skills.
- Upstream snapshots can describe optional services outside the reviewed scope. The usage guide defines what was selected; no bulk installer or optional paid/cloud route is enabled by importing this library.

## Ongoing additions

New skills shared by the owner belong in this same private repository after review: deduplicate by source and skill name, add a usage guide, preserve source/license and dependencies, and update the catalog and manifest. A new source is not permission to run its installer or change unrelated projects.

Snapshot date: 11 November 2026. Existing Claude access/allowance is separate from free skill licensing. No claim that everything is currently installed, that a free dependency never changes terms, or that one link automatically activates every skill.
