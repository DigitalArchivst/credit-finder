# CREDIT report: Credit Finder v1.3.2

Prepared with Credit Finder v1.3 on 2026-11-16 and carried forward to Credit Finder v1.3.2. Report revision: 1.2.
Submitted work: the v1.3.2 release, including its optional checker. v1.3.1 changed only the Quick-mode notice and v1.3.2 only public-release wording, so no credits changed.
Status: Experimental. Complete within the bounded scope below.

## Summary

This report credits the people, projects, and earlier work behind Credit Finder. It keeps the 15 findings of the v1.2 self-review (F01 to F15) and adds 12 more (F16 to F27). Eleven of the new findings restore earlier work that the v1.0 self-test had traced and v1.2 set aside as unchecked leads; their sources were reopened for v1.3. The twelfth credits Claude's authorship by name.

The central documented contributors are Steve Little, who specified and directed the skill; the Feature Attribution Finder, its method source; Claude, which wrote v1.0 and the v1.3 integration; and ChatGPT, which revised v1.2. The skill follows the Agent Skills specification and guidance from Anthropic and OpenAI. Earlier work on independent discovery, adversarial review, weighing evidence, and contributor credit is listed as related work.

This report shows who came earlier or worked on the same ideas. It does not claim that anyone copied anyone, or that any of them endorsed this skill.

## How this was done

- Mode: Standard. v1.2's two tracer clusters and lead reconciliation (F01 to F15), plus a v1.3 lead audit (F16 to F27). No separate challenger team.
- Web access: yes.
- Retrievals: v1.2 self-review 35. v1.3 audit 13 source opens.
- Review checks: every F16 to F26 source was opened in this run; F01 to F15 keep v1.2's review record.
- Scope: as v1.2, plus the earlier-work leads named in the v1.0 credits. Other v1.0 leads (Carroll and Carrithers, Nielsen, Contract Net, MapReduce, Popper, red teaming, Ranke, Griesbach, Eusebius, Hunt and McIlroy, FORCE11, Simon) stay in Unsettled items.
- Full evidence: the v1.0 self-test team files and the v1.2 review package are kept in the project archive beside this skill.

## Findings

| Finding | Point and locator | Creator and work | Group | Strength | Verification | Confidence | Evidence |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| F01 | C01, SKILL.md, Resources and acknowledgments | Agent Skills project, specification | Direct influence | Strong | Verified | High | [Provenance record](references/provenance.md#guidance-actually-consulted) explicitly records use of the [specification](https://agentskills.io/specification). Confirmed as the revision's documented account. |
| F02 | C01, SKILL.md frontmatter and folder layout | Agent Skills project, specification | Technical dependency | Strong | Verified | High | [Specification](https://agentskills.io/specification), Directory structure and SKILL.md format; actual required fields and resource folders inspected. Confirmed format adoption; host loading not tested. |
| F03 | C02, checklist, references, and evals | Anthropic, Skill authoring best practices | Direct influence | Strong | Verified | High | [Provenance](references/provenance.md#guidance-actually-consulted) and [authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), structure and evaluation sections. Confirmed documented authoring role, not a claim of comprehensive platform testing. |
| F04 | C03, documented guidance use | OpenAI, Build skills | Direct influence | Strong | Verified | High | [Provenance](references/provenance.md#guidance-actually-consulted) and [Build skills](https://learn.chatgpt.com/docs/build-skills). Confirmed documented guidance role. |
| F05 | C03, agents/openai.yaml | OpenAI, optional skill metadata conventions | Technical dependency | Strong | Verified | High | [Build skills](https://learn.chatgpt.com/docs/build-skills), Optional metadata, compared with the local interface and policy fields. Confirmed optional configuration use; no host installation or activation claimed. |
| F06 | C04, Markdown text and pipe tables | John Gruber, with Aaron Swartz acknowledged; GitHub Flavored Markdown and its CommonMark basis | Technical dependency | Strong | Verified | High | [Markdown project](https://daringfireball.net/projects/markdown/) and [GFM specification](https://github.github.com/gfm/), Introduction and Tables. Confirmed use of formats only; no imported renderer or Gruber converter code is claimed. |
| F07 | C05, SKILL.md frontmatter; agents/openai.yaml | YAML Language Development Team; specification credits Oren Ben-Kiki, Clark Evans, and Ingy döt Net | Technical dependency | Strong | Verified | High | [YAML specification](https://yaml.org/spec/1.2.2/), title/credits and mapping syntax, compared with actual metadata. Confirmed format use; no particular YAML parser is a runtime requirement. |
| F08 | C06, scripts/check_report.py imports and calls | Python Software Foundation and Python contributors, Python standard library | Technical dependency | Strong | Verified | High | [Standard library](https://docs.python.org/3/library/index.html), [Python credits](https://docs.python.org/3/copyright.html), and inspected argparse/pathlib/re/sys calls. Confirmed optional tooling dependency. Tests ran on Python 3.12.14; 3.10+ is a declared minimum, not a tested version matrix. |
| F09 | C07, recorded owner specification | Steve Little, specification and direction | Ordinary citation | Strong | Verified | High | [Owner record](references/provenance.md#owner-decisions-and-revision-authority), backed by supplied SPECIFICATION.md. Confirmed as the supplied account of the eight decisions. Contributor credit does not imply an independent audit of the original conversation. |
| F10 | C08, method and review rules | Feature Attribution Finder, directed by Steve Little with Claude and OpenAI Codex assistance | Direct influence | Strong | Verified | High | [Method-source record](references/provenance.md#method-source), backed by supplied LESSONS-FROM-THE-FINDER.md. Confirmed explicit method-source relationship; project duration, full transcripts, and prior feature findings were not independently verified. |
| F11 | C09, LICENSE.md permission and disclaimer paragraphs | MIT License text, checked against the Open Source Initiative publication | Ordinary citation | Strong | Verified | High | [Local license](LICENSE.md) compared with the [MIT text](https://opensource.org/license/mit). Confirmed substantive text. OSI is the checked publisher, not an asserted author of the license or adjudicator of ownership. |
| F12 | C10, designated report-commentary grant | Creative Commons, Attribution 4.0 International | Ordinary citation | Moderate | Verified | High | [Scope rules](references/license-and-disclaimer.md) and [CC BY 4.0 legal code](https://creativecommons.org/licenses/by/4.0/legalcode.en), sections 2, 3, and 5. Confirmed separate grant and research disclaimer, limited to held or authorized rights. |
| F13 | C11, attribution pattern | Creative Commons, Recommended practices for attribution | Ordinary citation | Moderate | Verified | High | [CC guidance](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution), Basic components. Confirmed title/author/source/license recommendation. This is helpful practice, not the entirety of license conditions; title is optional under CC 4.0. |
| F14 | C12, delegation and review pattern | Anthropic, Building effective agents; current byline Erik S. and Barry Zhang | Historical predecessor | Moderate | Verified | Medium | [Publisher page](https://www.anthropic.com/research/building-effective-agents), Orchestrator-workers and Evaluator-optimizer, publisher-dated 2024-12-19. Confirmed related pattern on the current page. No archive checked; date is publisher-supplied, not a separately verified date for every current passage. No causal influence inferred. |
| F15 | C12, parallel research and synthesis | Anthropic, How we built our multi-agent research system | Historical predecessor | Moderate | Verified | Medium | [Publisher page](https://www.anthropic.com/research/multi-agent-research-system), Architecture overview, publisher-dated 2025-06-13. Confirmed related lead/subagent pattern. Current page and publisher date inspected; no historical snapshot or first-origin claim. |
| F16 | C14, independent discoverer group; "independent discovery is common" | William F. Ogburn and Dorothy Thomas, "Are Inventions Inevitable?", Political Science Quarterly 37 | Historical predecessor | Moderate | Verified | High | [Full text](https://archive.org/stream/jstor-2142320/2142320_djvu.txt): signed by both authors; "The appendix to this article contains a list of 148 such cases". Volume 37 is the 1922 volume (JSTOR 2142320); the year is not printed in the text opened. Confirmed. |
| F17 | C14, same | Robert K. Merton, "Singletons and Multiples in Scientific Discovery" (Proceedings of the American Philosophical Society 105, 1961) and "Priorities in Scientific Discovery" (American Sociological Review 22, 1957) | Historical predecessor | Moderate | Verified | Medium | [Merton bibliography](https://garfield.library.upenn.edu/merton/rkmpublications.html) lists both with volume and pages. Bibliography confirmed; full texts not opened. |
| F18 | C15, "earliest verified", never "first" | Stephen M. Stigler, "Stigler's Law of Eponymy" (Transactions of the New York Academy of Sciences, 1980), which credits Merton | Historical predecessor | Courtesy | Verified | Medium | [BibBase record](https://bibbase.org/network/publication/stigler-stiglerslawofeponymy-1980): volume 39, pages 147 to 157, 1980. The law's wording ("No scientific discovery is named after its original discoverer") and the credit to Merton come from [Wikipedia's quotation of the paper](https://en.wikipedia.org/wiki/Stigler%27s_law_of_eponymy); the paper itself was not opened. |
| F19 | C16, three-level loading of detail | Xerox Star team (David Canfield Smith, Charles Irby, Ralph Kimball, Bill Verplank, Eric Harslem), "Designing the Star User Interface", Byte, April 1982 | Historical predecessor | Moderate | Verified | Medium | [Reprint](https://www.guidebookgallery.org/articles/designingthestaruserinterface): "This is an example of 'progressive disclosure': hiding complexity until it is needed." Earliest use of the term found; not shown to be its coinage. Original issue not seen. |
| F20 | C17, challenger that tries to disprove findings | The promoter of the faith ("devil's advocate") in Catholic canonization | Historical predecessor | Moderate | Verified | Medium | [Catholic Encyclopedia, 1907](https://www.newadvent.org/cathen/01168b.htm): first formal mention "under Leo X (1513-21)"; "Urban VIII, in 1631, made his presence necessary". Confirmed. |
| F21 | C17, third reviewer settles disagreements | The Cochrane Collaboration, Cochrane Handbook for Systematic Reviews of Interventions | Historical predecessor | Courtesy | Verified | High | [Chapter 4, section 4.6.4](https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-04): "Use (at least) two people working independently"; "this may require arbitration by another person." Earliest edition opened in v1.0: 4.2.1 (2003). |
| F22 | C18, strengths, confidence, and source verdicts | Elizabeth Shown Mills, Evidence Explained, and her evidence analysis process map | Historical predecessor | Courtesy | Verified | Medium | [QuickLesson 17](https://www.evidenceexplained.com/content/quicklesson-17-evidence-analysis-process-map) defines sources, information, and evidence. The 2007 first-edition date rests on catalog records. |
| F23 | C18, same | Board for Certification of Genealogists, Genealogical Proof Standard | Historical predecessor | Courtesy | Verified | High | [BCG about page](https://bcgcertification.org/about): "During the late 1990s the five-part Genealogical Proof Standard (GPS) was developed." The page dates BCG's standards in book form to 2000 without naming the GPS in that sentence. |
| F24 | C18, same | GRADE Working Group, "Grading quality of evidence and strength of recommendations", BMJ 2004 | Historical predecessor | Courtesy | Verified | High | [PMC428525](https://pmc.ncbi.nlm.nih.gov/articles/PMC428525), BMJ 2004;328(7454):1490. Confirmed. |
| F25 | C19, credit wording sorted by kind of contribution | CRediT Contributor Roles Taxonomy (begun at a 2012 Wellcome Trust and Harvard workshop; now ANSI/NISO Z39.104-2022) | Historical predecessor | Courtesy | Verified | High | [NISO origins page](https://credit.niso.org/origins/): "A workshop hosted by the Wellcome Trust and Harvard University in 2012". Confirmed. |
| F26 | C20, similarity is not a finding of copying | Turnitin, "Does Turnitin detect plagiarism?" (Patti West-Smith, 2022) | Historical predecessor | Courtesy | Verified | High | [Turnitin blog](https://www.turnitin.co.uk/blog/does-turnitin-detect-plagiarism): "Similarity does not equal plagiarism." Confirmed. |
| F27 | C21, v1.0 instructions and v1.3 integration | Claude (Anthropic), in Claude Code | Ordinary citation | Strong | Verified | High | [Provenance record](references/provenance.md#v13-integration): the authoring session's record of 16 November 2026. Contributor credit only; it makes no claim about copyright in AI-assisted text. |

### No credit recommended

Ordinary headings, checkboxes, loop syntax, plain-language writing, and other routine conventions do not receive individual origin claims. Format acknowledgments are consolidated in F06 and F07.

## Corrections to existing credits

- v1.2 kept the v1.0 earlier-work credits only as unchecked leads, so the skill's credits no longer named them. v1.3 reopened their sources and restores eleven as findings (F16 to F26). This follows Steve Little's request that the skill credit those who made it possible.
- v1.2 did not credit Claude's authorship as a finding. v1.3 adds it (F27).
- The Genealogical Proof Standard's 2000 date is narrowed: BCG dates its standards in book form to 2000, and the GPS to the late 1990s (F23).
- All v1.2 corrections stand.

## Unsettled items

- Further earlier work traced in the v1.0 self-test but not reopened: John M. Carroll and Caroline Carrithers (1984) and Jakob Nielsen (2006) on progressive disclosure; Reid G. Smith's Contract Net (1980) and Jeffrey Dean and Sanjay Ghemawat's MapReduce (2004); Karl Popper (1934) and red teaming; Leopold von Ranke (1824); Johann Jakob Griesbach (1774, 1776) and Eusebius's canon tables; James W. Hunt and M. Douglas McIlroy (1976); the FORCE11 Software Citation Principles (2016); and Herbert A. Simon (1956). Reopening their sources would let them join the findings.
- Who coined "progressive disclosure" is not established.
- The two Anthropic pattern pages (F14, F15) use publisher dates; no archived first editions were checked.
- Model training-source use, native host activation, and minimum Python version remain untested.

## Ready-to-paste credit wording

### Influences documented in this work

- Credit Finder was specified and directed by Steve Little. Its method comes from the Feature Attribution Finder, a review he directed with Claude and OpenAI Codex in November 2026. (F09, F10)
- It follows the [Agent Skills specification](https://agentskills.io/specification), [Anthropic's skill authoring guidance](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices), and [OpenAI's skills guidance](https://learn.chatgpt.com/docs/build-skills). (F01, F03, F04)
- Written by Claude (Anthropic) for v1.0 and v1.3, and revised for v1.2 by ChatGPT (OpenAI). (F27; contributors section below)

### Earlier and related work

- On independent discovery: William F. Ogburn and Dorothy Thomas, "Are Inventions Inevitable?" (1922), and Robert K. Merton (1957, 1961). (F16, F17)
- On why "first" claims mislead: Stephen M. Stigler's law of eponymy (1980). (F18)
- On showing detail only when needed: the Xerox Star team (1982), the earliest use of "progressive disclosure" we found. (F19)
- On testing findings by trying to disprove them: the devil's advocate office in canonization (from the early 1500s), and the Cochrane Handbook's practice of two reviewers with a third to settle disagreements. (F20, F21)
- On weighing evidence: Elizabeth Shown Mills's evidence analysis, the Genealogical Proof Standard, and the GRADE Working Group (2004). (F22, F23, F24)
- On crediting by kind of contribution, and on similarity not being plagiarism: the CRediT taxonomy and Turnitin's guidance. (F25, F26)
- On lead agents with helpers: Anthropic's [Building effective agents](https://www.anthropic.com/research/building-effective-agents) (2024) and [multi-agent research system](https://www.anthropic.com/research/multi-agent-research-system) (2025). (F14, F15)

### Built with

- The Agent Skills folder format, with OpenAI's optional `agents/openai.yaml`. (F02, F05)
- Markdown (John Gruber, with Aaron Swartz) and GitHub Flavored Markdown tables; YAML for settings. (F06, F07)
- Python and its standard library for the optional report checker. (F08)

### Citations still needed

- Keep the full [MIT notice](LICENSE.md) with the skill, and the [CC BY 4.0 terms](https://creativecommons.org/licenses/by/4.0/legalcode.en) with this report. Creative Commons' [attribution guidance](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution) informs the credit pattern. (F11, F12, F13)

## Authorship and review contributors

Steve Little specified and directed the project. Claude (Anthropic), working in Claude Code, wrote v1.0, ran its self-test with four tracer teams, and audited and integrated v1.3. ChatGPT (OpenAI) prepared v1.2; delegated ChatGPT reviewers contributed method critique, guidance and licensing research, the report checker, task runs, and self-review. These acknowledgments make no claim that a model holds copyright.

## Rights and reuse

The skill's original instructions, scripts, templates, and associated
materials use MIT within the scope of LICENSE.md. This report's original
commentary has the separate CC BY 4.0 grant below. The full MIT text is included;
a short credit line is not a substitute for required notices.

External sources are linked and paraphrased. No third-party figure, historic
plate, audio, video, dataset, or source-code library is proposed for reproduction.
Using a format does not impose a converter's software license on the authored
report. Source-inputs retain their existing status and rights. Neither the
review nor the license choice adjudicates ownership of AI-assisted text.

## License and disclaimer

Experimental output from Credit Finder v1.3.2. The skill is licensed under the
[MIT License](https://opensource.org/license/mit). This report is provided
AS IS, without warranties of accuracy, completeness, fitness for a particular
purpose, or noninfringement. Findings are research assistance and may contain
errors. They do not determine legal rights, permission, originality,
infringement, or misconduct, and do not establish endorsement. Verify sources
and applicable terms before relying on or publishing the report. Earlier work
and similarity do not establish use or intent.

Report license: Steve Little offers this report's original commentary under
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/),
to the extent he holds or is authorized to license the relevant rights.
Attribute Steve Little, identify the report title and Credit Finder v1.3.2,
retain the license link, and indicate changes. The applicable legal code,
not this summary, governs the grant.

The reviewed work and third-party text, code, images, data, recordings, and
other material retain their existing rights and notices; neither license
grants permission to reuse them.

This review cannot establish which training sources contributed to a
particular model output. Resemblance does not establish use or non-use of a source.
