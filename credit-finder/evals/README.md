# Credit Finder v1.3.2 evaluations

The 22 scenarios in evals.json combine three small fixed submissions with
explicit evidence packets for manual simulations. They preserve the original
four scenario IDs and repair two unsupported expectations: no import does
not rule out a dependency, and an offline reviewer cannot invent an older
lyric passage. The essay fixture is shorter than the original 1,200-word
scenario description.

## Running a live comparison

Give a fresh reviewer only the requested fixture, user query, permitted tools,
and skill path for the skill condition. Do not expose expected_behavior,
previous outputs, diagnosis, or this README to the reviewer. Run a matching
baseline without the skill under the same model and access conditions.
Record the exact prompt, model, effort, source attempts, output, and limits.

Then grade evidence fidelity, relationship correctness, uncertainty, material
coverage, report usability, notices, and access/budget honesty. An invented
source, unsupported accusation, or unsupported influence/independence is a
critical failure. Structural checker success does not prove these dimensions.

For embedded packets, explicitly state which facts are stipulated. Record a
manual walkthrough or simulation as such; do not label it a live source check.
The trigger cases need actual host activation tests before claims about
routing reliability. Compare intended Claude and Codex/ChatGPT models only
when those models and hosts are actually available.

## Reproducibility

Run `python3 scripts/check_report.py REPORT.md` from the skill folder for each
completed report. The outer review package includes independent code and
prose runs, a SKILL.md-only offline run, one code baseline, checker unit tests,
and manually reviewed scenario results. The fixed inputs in this folder are
mirrored under review/fixtures in that package so the saved reports' local
links can resolve. The validation record compares those bytes.

These exercises are regression evidence for this release, not a claim of
statistically established accuracy, broad media perception, or platform
installation compatibility.
