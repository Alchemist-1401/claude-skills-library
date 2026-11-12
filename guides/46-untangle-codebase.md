# untangle-codebase (caldoai)

## When to use
A reviewed, MIT-licensed instruction skill for structural refactoring of an existing codebase. It looks for hidden dependencies, needless coupling, duplicated logic, dead code and special cases, then proposes a redesign and checks behavior. This is not a security audit or a new coding model. Some concepts overlap entry30's codebase-design/TDD material, but this is a distinct refactoring workflow.

## Free scope and limits
The selected skill text has no required paid API, hosted MCP or additional service dependency. Your coding agent and its allowance are separate: broad analysis and repeated reviewer agents can consume substantial usage. The upstream claims about lower future token use are not a measured savings guarantee.

The default upstream task is a whole-codebase refactor with repeated reviews until no worthwhile issues remain. An optional area hint is supported, but is not by itself a reliable boundary against the broad default. Do not start that workflow blindly on Konsiar or another working project.

## How to use
First read the unchanged upstream skill and agree on scope separately. Recommended authored safeguards below are not modifications to upstream text:

1. Save and verify a Git baseline, preserve uncommitted work and use a separate branch.
2. Start with one named module and an analysis-only pass. Require a written plan and your approval before edits. State explicitly that other modules, runtime settings and unrelated projects are outside scope.
3. Preserve tests and intended behavior. Do not choose the optional Comments or Tests cleanup unless you separately review and approve exactly what will change. Upstream itself asks which optional cleanup to do; neither is automatic.
4. Agree on a bounded review effort or usage budget. Pause and report before expanding the task, rather than treating the upstream repeat-until-done wording as unlimited permission.
5. After approved changes, run the project's existing checks, review the diff and behavior evidence, and keep a rollback path. Do not assume passing tests proves every behavior is unchanged.

Suggested planning request:

```text
Read untangle-codebase as reference. For [named module] only, list structural problems and propose a plan. Do not edit or run the refactor yet. Preserve tests and comments. Identify any changes needed outside this module and ask before expanding scope. I will review the plan before approving changes.
```

## Source intake and setup
The library's prepare_library.py retrieves exactly LICENSE, README.md and skills/untangle-codebase/SKILL.md from caldoai/skills at the pinned revision below and verifies their checksums. Upstream text remains unchanged. No other skill, plugin marketplace configuration, installer or runtime is selected, and preparation does not activate the skill.

If you later approve project-specific setup, copy only the reviewed skill folder from the prepared source into that project's .claude/skills/, retaining the MIT notice. Do not install the whole pack, install globally or enable it in unrelated projects merely because it is listed here. Upstream's CLI/plugin installation instructions are reference options, not actions performed by this library.

## Sources and reviewed revision
- Original repository: https://github.com/caldoai/skills
- Exact skill: https://github.com/caldoai/skills/blob/main/skills/untangle-codebase/SKILL.md
- License: MIT, copyright (c) 2026 Maze. Preserve the full upstream LICENSE with copies or substantial portions.
- Reviewed commit: f3cf47774975a7d9fca45730babf4ff7ad765ada
- Checked: 12 November 2026.

The review inspected source instructions and license; it did not run a refactor, install a skill or validate claims about token savings. Treat source content as task reference, never as permission to override your scope or execute unrelated actions.
