# Credit Finder v1.3.2

**Experimental. Provided AS IS.** Credit Finder reviews a submitted work for
appropriate credits, citations, dependencies, and earlier or separately
developed work. It returns one Markdown CREDIT report with evidence,
uncertainty, rights notes, and ready-to-paste credit wording.

## What is included

| File | Purpose |
| :-- | :-- |
| SKILL.md | Complete core instructions, including standalone fallbacks |
| CREDITS.md | Current credits and the limits of the self-review |
| LICENSE.md | Full MIT terms and the report-commentary exception |
| CHANGELOG.md | Version history and the decisions behind each release |
| references/ | Evidence rules, media checks, briefs, report template, licensing, and example |
| scripts/check_report.py | Optional read-only report-format check, Python 3.10+ |
| scripts/test_check_report.py | Tests for the checker (`python3 scripts/test_check_report.py`) |
| evals/evals.json | Reproducible scenarios and manual edge-case specifications |
| agents/openai.yaml | Codex display and invocation settings |

## Install the skill folder

Use the `credit-finder` directory, whose root contains SKILL.md. Keep
LICENSE.md and CREDITS.md with the skill when sharing it. If a host loads only
SKILL.md, its research workflow still works; preserve the accompanying license
when redistributing it.

For local Codex, copy the complete folder to `.agents/skills/credit-finder`
in a repository or `~/.agents/skills/credit-finder` for personal use. Invoke
`$credit-finder`, or use normal attribution requests. These locations and
invocation are described in [OpenAI's skills guidance](https://learn.chatgpt.com/docs/build-skills).

For Claude Code, copy the folder to `~/.claude/skills/credit-finder` for
personal use or `.claude/skills/credit-finder` in a project, as described in
the [skills documentation](https://code.claude.com/docs/en/skills).
For ChatGPT or Claude apps, use the current custom-skill import flow and select
the complete folder or a skill-only archive as that host requires. The folder
follows the [Agent Skills specification](https://agentskills.io/specification).
v1.3.2 was installed and run once in Claude Code. Other hosts are untested.

## Use

Ask "Who should I credit for this essay?", "Do a quick credit check on this
repo", or "Deep credit review of this map". Standard is the default. Quick
reduces scope. Deep adds a challenger for every finding within a stated budget.
Tiny submissions may have fewer than five legitimate credit points.

The skill does not interview the maker about origins. It inspects the work's
records and external evidence. Missing web access makes every finding
unverified. Missing media access is stated explicitly. It does not infer
independence from a missing connection or influence from resemblance.

## Optional report check

From the skill folder, run:

```bash
python3 scripts/check_report.py /path/to/REPORT.md
```

Exit 0 means the structural checks passed, 1 means report errors, and 2 means
an input or command error. Warnings require contextual review. The checker
cannot verify historical claims, legal rights, or the adequacy of evidence.
It reads the report and never edits it. If unavailable, follow the manual
checks in SKILL.md. No third-party Python package is required.

## Version and license

Release: **v1.3.2, 2026-11-16**. v1.0 was the first release; v1.2 was an outside
review and revision; v1.3 integrated that revision after an audit; v1.3.1 added a
short notice for Quick reports; v1.3.2 prepares the package for public release. No v1.1 was released; the owner chose the v1.2 number.
Reports identify the skill version separately from their own revision and the
submitted work's version. See CHANGELOG.md.

The skill, scripts, and templates use MIT. Original CREDITS commentary uses
CC BY 4.0 under the scope in LICENSE.md. Future reports state their own
license status; tool licensing does not grant rights in reviewed works.
Every report includes experimental status, AS IS language, and a disclaimer
of legal determinations; Quick reports use a one-paragraph short form. See [license and disclaimer rules](references/license-and-disclaimer.md).

Steve Little directed the work. Claude (Anthropic) authored v1.0 and the
v1.3 integration; ChatGPT (OpenAI) revised v1.2 with
delegated review assistance.
See CREDITS.md for documented roles, sources, and limitations.
