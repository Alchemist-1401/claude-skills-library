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
