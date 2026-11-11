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
