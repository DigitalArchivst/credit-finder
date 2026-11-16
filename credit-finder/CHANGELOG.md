# Changelog

## v1.3.2: 2026-11-16

Public release preparation, approved by Steve Little. No method, credit
finding, or license changed.

- The provenance record now says the supplied source records are held
  privately by the owner, instead of pointing to a review archive readers
  cannot see. Their SHA-256 hashes are kept as identity records.
- Contributing AI systems are credited by product and company, Claude
  (Anthropic) and ChatGPT (OpenAI), rather than by model version.
- The Feature Attribution Finder is described as a privately held review
  directed by Steve Little.
- Version markers updated to v1.3.2 across the skill, checker, tests, evals,
  and Codex settings.
- README install instructions now give the Claude Code and Codex folder
  locations directly, instead of referring to the review package.
- First live install test: in Claude Code, the skill loaded from an everyday
  request ("Who should I credit or cite in it? Keep it quick"), ran Quick mode
  with web search on a synthetic essay, and produced a report that passed the
  checker. Other hosts remain untested.

## v1.3.1: 2026-11-16

Steve Little approved a shorter notice for Quick mode, so the notice does not
outweigh a short report.

- Quick reports now use a four-sentence short form: experimental and MIT, AS IS,
  research help rather than a legal finding, and no license over the report,
  the reviewed work, or third-party material.
- Standard, Deep, offline, partial, and self-test reports keep the full notice,
  because longer reports are more likely to be relied on or published.
- The checker reads three-part version numbers and warns when a non-Quick
  report uses the short form. A new test covers both cases (16 tests pass).
- Updated SKILL.md, the report template, the licensing reference, README,
  evals, and Codex settings to v1.3.1. CREDITS.md is carried forward unchanged
  apart from its version lines.

## v1.3: 2026-11-16

Integration of the outside v1.2 revision after an audit by Claude, the v1.0
author, at Steve Little's request. The design and the owner's eight decisions
are unchanged.

- Restored the earlier-work credits from the v1.0 self-test. v1.2 had kept them
  only as unchecked leads; their sources were reopened, and eleven return as
  findings F16 to F26 in CREDITS.md. The rest stay in Unsettled items.
- Credited Claude by name as an authorship finding, which v1.2 lacked.
- Restored plain trigger words to the description (credit, cite, thank,
  influences, inspirations, predecessors, prior art) so the skill loads when a
  creator asks in everyday words.
- Scaled Standard and Deep retrieval caps with the number of points (6 and 10
  per point, with floors and ceilings). v1.2's fixed caps of 80 and 160 would
  have stopped the v1.0 self-test partway.
- Asked for plain paste-ready wording, with short hedges inside the sentence,
  and rewrote the CREDITS wording that way.
- The checker now accepts any "Credit Finder vX.Y" marker and warns when it
  differs from the skill folder's version. Its tests now ship in `scripts/`
  and use a bundled fixture, so they run inside the installed folder.
- Narrowed the Genealogical Proof Standard date (developed in the late 1990s;
  BCG's standards first in book form in 2000).

## v1.2: 2026-11-16

Experimental review release requested by Steve Little. The handoff's proposed
v2.0 number is superseded by the user's explicit v1.2 instruction.

- Added MIT licensing for the skill and CC BY 4.0 for designated original
  report commentary, with rights exclusions and a future-report default.
- Added version, report revision, experimental status, AS IS language, and
  license/disclaimer requirements to every output path.
- Required affirmative evidence of independent development and explicit
  evidence of direct influence. Distinguished bibliography mentions from influence.
- Separated recommendation strength, verification, confidence, and source verdict.
- Kept all five groups, three strengths, and the owner's narrow exact-rule
  exception. Moved no-credit dispositions outside the strength scale.
- Repaired Standard review sampling; bounded searches, teams, and challenge rounds.
- Added feature-specific dates, source-instruction boundaries, media limitations,
  version-specific rights checks, and report reproduction notes.
- Preserved per-item relationship rows and kept unverified claims out of
  factual paste-ready credits, including in offline runs.
- Added a read-only report checker, tests, fixed fixtures, and an expanded
  evaluation plan. Replaced the fragile historical example with an explicitly
  synthetic teaching example; preserved its supplied predecessor as source material.
- Updated the current credits from the v1.2 self-review and distinguished
  retained historical leads from evidence rechecked in this run.

See the outer package's HANDOFF-BACK.md, review/DIFF-SUMMARY.md, and test records
for reasoning and actual validation limits. Those review files are not needed
to use the installed skill folder.

## v1.0: supplied baseline, 2026-11-16

The uploaded package declares metadata.version 1.0. It contains the core
workflow, five references, four scenario descriptions, and its prior self-test.
No intervening v1.1 package was supplied, so none is invented here.

## Versioning convention

Keep metadata.version as the authoritative release string. Carry that string
into the README, changelog, report template, required output notice, and checker.
Increase the minor version for compatible workflow additions, and a major
version for changes to the public report contract or owner decisions. Do not
silently renumber old reports; preserve their report date and source version.
This is a prospective two-part release convention, not a claim to strict
three-part Semantic Versioning compliance. This release uses the user-requested
v1.2 despite adding report fields and finding IDs; downstream table parsers
need updating. No compatibility promise is inferred from the requested number.
