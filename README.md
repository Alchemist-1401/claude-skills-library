# Your Claude skills library

One private home for 43 curated skill entries, individual usage guides and eight separate project references. Some entries contain several skills. Adding a skill here does not install or run it on your device.

## Start with Claude

Give Claude this repository link and say:

> Read README.md, CLAUDE.md and CATALOG.md. Use the individual guides and the reviewed source manifest. For local intake, prepare the library in one new folder. For my task, select only the relevant skill. Keep Konsiar, Velocitas, outreach and personal work separate.

Claude needs authenticated access to this private repository. A link alone does not grant access. Use Claude's GitHub connection where supported, or an authenticated local clone with Claude Code. Never make the repository public or paste credentials into a prompt.

## One-folder intake

1. Clone or download this repository into one dedicated folder, such as `~/Claude-Library`.
2. Read `CATALOG.md` or the individual files in `guides/`.
3. For local source intake, run `python3 prepare_library.py`. It fetches selected files from original public GitHub repositories at pinned commits, verifies each file's hash, preserves source licenses, and puts the result in one new `library/` folder. Python 3.9+ and internet are required.
4. Read the chosen guide and its source. Use or set up only the skill needed in the intended project. Do not copy the whole library into `.claude/skills`.

Preparation downloads reference files. It does not execute upstream scripts, install dependencies, activate plugins, change global settings or touch other projects. Existing destinations are refused. On failure, only the script's own temporary staging folder is removed. `--destination PATH` selects a different new folder; its parent must already exist.

## Repository layout

- `guides/` - 43 individually readable usage files: purpose, free scope, dependencies, source, setup notes and pinned revision.
- `CATALOG.md` - the same usage material together for easy reading.
- `CLAUDE.md` - a short entry point.
- `projects/` - eight separate copy-ready project references, not installable skills.
- `references/tools/` - separate tool usage notes, including the two local MCP tools from the SEO reel. No servers are installed by intake.
- `authored/` - the recovered authored skill texts; file markers inside the Konsiar text preserve its original folder layout.
- `manifests/` - the exact selected source paths, commits, file hashes and licenses/notices to retrieve. This is the source of truth for what preparation actually downloads.
- `prepare_library.py` - local-only intake, standard library only.
- `library/` - created locally after preparation, not a global skill installation.

## Snapshot and source limits

The entry guides' "snapshot" descriptions refer to the reviewed source selection, not a promise that every upstream asset is stored in this GitHub repository. Preparation retrieves only paths named in `manifests/`. The guides' example install commands are reference instructions, not commands that run during intake.

Bulky rendered image/audio/PDF demos are not included in the intake. Some references/scripts name those optional or workflow-specific assets; get a needed asset from the pinned original source under its license rather than pretend it exists locally. Full applications, model weights, compiled engines and complete upstream plugin setups are not supplied.

- Lisaan: exact skill text recovered, original dictionary/corpus/reference ZIP missing. Incomplete and not ready to activate without that original ZIP.
- MotionSites: permitted skill code is selected; its restricted example/media collection is not redistributed. Use the official source when a workflow needs it and its license permits.
- Remotion, Remy's Content Principles and Real SFX: individual usage guides and source links remain, but source contents are not mirrored/retrieved where redistribution permission was not established. Remotion's runtime free use depends on organization size.
- The hosted Motion MCP skill, paid API/trial paths, screenshot-to-code app, paid service directories, private prospect data and superseded duplicate skills are not active library skills.
- Optional paid/cloud features described upstream are outside the reviewed free scope. No whole-pack installer, hook, service or paid integration is enabled by opening this library.

For updates, keep your existing working copy and prepare a fresh destination, then compare. Never delete modified work just to make an update run.

## New additions

New skills shared by the owner go into this same private repository after review: deduplicate by source/skill name, add usage instructions, preserve source/license/dependencies, and update the catalog and manifest. Adding is not permission to run an installer or change unrelated projects.

Checked 11 November 2026. Existing Claude access/allowance is separate from free skill licensing. Nothing here claims current installation or automatic activation from a link.
