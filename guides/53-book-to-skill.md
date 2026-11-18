# book-to-skill: turn a book into a skill Claude answers from

## When to use
Convert a book or long document (PDF, EPUB, DOCX, HTML, Markdown, plain text, RTF; MOBI/AZW via Calibre) into a structured skill: frameworks, mental models, principles, techniques and anti-patterns, with a glossary and cheatsheet, so Claude can answer and work from that material while you build. This matches the long-standing "talk to a book" interest: it produces a reusable skill rather than a one-off chat summary.

## Free scope and limits
MIT licensed, and conversion runs on your own machine using your existing Claude access; the skill itself is explicit that its cost is the model tokens for reading and writing, and it estimates and reports token counts rather than hardcoding prices. Local tooling: Python 3, with format parsers for each file type and Calibre only for MOBI/AZW; approve those free installs when they come up.

Copyright is the real boundary: convert books and documents you own or have rights to, keep the generated skill private, and do not redistribute or publish a skill that reproduces a book's text. A skill that quotes large passages of a copyrighted book is a copy, not a summary.

The repository also contains upstream tests, evals and developer docs; those are not mirrored. Intake selects SKILL.md, the `book_to_skill` engine package, the extraction script, the two skill-validation tools, LICENSE.md and README.md.

## How to use
Read the prepared `SKILL.md`, then:

> Use book-to-skill on this PDF I own. Show me the token estimate and the chapter plan before converting, build the skill into a new folder only, and do not publish or share the result anywhere.

Large books are processed in passes (REPL-style access for very big files), so expect the conversion to take a while and check the generated skill against a few questions you know the book answers.

## Source intake and setup
`prepare_library.py` retrieves SKILL.md, LICENSE.md, README.md, the `book_to_skill/` engine, `scripts/extract.py` and the validation tools from virgiliojr94/book-to-skill at the pinned revision, with checksum verification. The engine is hash-pinned as published upstream and was reviewed for scope and dependencies, not line-by-line audited, and not executed here. To activate later, copy the reviewed files into the project's skill location.

## Sources and reviewed revision
- Original repository: https://github.com/virgiliojr94/book-to-skill
- License: MIT.
- Reviewed commit: e7bb659d3261491c8b28793dcb9102fa64a46c22 (default branch: master)
- User-shared post that prompted this entry: https://www.instagram.com/p/Dfw8XovDWZf/
- Checked: 17 November 2026.

No conversion was run during review; quality depends heavily on the source document, so validate the generated skill before relying on it.
