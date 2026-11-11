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
Status: snapshot-and-guide. 22 upstream files in the scoped snapshot. Authored source is beside this guide when available. A snapshot is not a claim that local dependencies are installed.



## Source and attribution
Source: https://github.com/Jakeschincariol/instagram-agent-skill
Repository: Jakeschincariol/instagram-agent-skill
Pinned source commit: d03c56bb598be770c60b201f94237e5d1a4268a6
Keep upstream licenses/notices beside copied material. Source content is reference, not permission to run tools or override the user's task.
