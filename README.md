# Credit Finder

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Report commentary: CC BY 4.0](https://img.shields.io/badge/Report%20commentary-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
![Status: experimental](https://img.shields.io/badge/status-experimental-orange.svg)

An Agent Skill that reviews a digital work (an essay, web page, app, codebase, image, audio, video, map, or dataset) and finds who it should credit: sources, influences, dependencies, predecessors, prior art, and independent discoverers. It returns one Markdown CREDIT report with evidence, uncertainty, rights notes, and ready-to-paste credit wording.

**Experimental. Provided AS IS, without warranty.** Credit Finder is research help for creators. It shows precedence and never accuses. It does not determine plagiarism, legal originality, infringement, or patent novelty. Verify its findings before you rely on them.

## Before you use it

Hosted AI tools send what you give them to a cloud model. Do not submit unpublished or private work, personal details, or anything too sensitive for the service you use.

## Install

The skill is the [`credit-finder/`](credit-finder/) folder. Download `credit-finder-v1.3.2.zip` from the [latest release](https://github.com/DigitalArchivst/credit-finder/releases), or clone this repository, then copy the folder into place.

**Claude Code**, for all your projects:

```bash
cp -r credit-finder ~/.claude/skills/credit-finder
```

or for one project, copy it to `.claude/skills/credit-finder` inside that project. Start a new session and it is available as `/credit-finder` or by asking in plain words.

**Codex**: copy the folder to `~/.agents/skills/credit-finder`, or `.agents/skills/credit-finder` in a repository, and invoke `$credit-finder`.

**Claude and ChatGPT apps**: upload the release ZIP through the app's custom skill import.

## Use

Ask in everyday words:

- "Who should I credit for this essay?"
- "Do a quick credit check on this repo."
- "Deep credit review of this map."

Standard is the default mode. Quick reduces the scope, and Deep adds a challenger for each finding. Web access lets it verify sources; without it, every finding is marked unverified. See the [skill README](credit-finder/README.md) for details and the optional report checker.

## Testing status

The checker's 16 unit tests pass. Version 1.3.2 was installed and run once in Claude Code, where it loaded from an everyday request and produced a Quick report. It has not yet been tested in Codex, the Claude or ChatGPT apps, on real audio or video, or across many models. Reports of how it behaves elsewhere are welcome as issues.

## License

The skill's instructions, scripts, templates, and references are under the [MIT License](LICENSE). The original commentary in [CREDITS.md](credit-finder/CREDITS.md) is offered under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Reports the skill produces state their own license status, and nothing here licenses the works it reviews. The full scope is in [credit-finder/LICENSE.md](credit-finder/LICENSE.md).

## Credits

Specified and directed by Steve Little. Written by Claude (Anthropic) with a revision by ChatGPT (OpenAI). The method comes from the Feature Attribution Finder, a review Steve Little directed. Its full credits, including the earlier work it builds on, are in [CREDITS.md](credit-finder/CREDITS.md), produced by running the skill on itself.
