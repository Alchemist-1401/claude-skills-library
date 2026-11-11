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
