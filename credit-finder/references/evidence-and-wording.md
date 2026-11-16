# Evidence and wording

Use this reference for uncertain relationships, dates, and recommendations. The rules in SKILL.md remain sufficient without this file.

## Contents

- Relationship decisions
- Evidence records
- Verification and confidence
- Strength and the exact-rule exception
- Source verdicts
- Credit wording
- Difficult cases

## Relationship decisions

Start with the claim, then choose a group. Do not begin with a famous creator and work backward from resemblance.

| Question | Decision |
| :-- | :-- |
| Does the work explicitly say a source shaped a particular part? | Direct influence, described as the work's documented account |
| Does the submitted material contain or call the component? | Technical dependency, with the observed role |
| Is there a specific matching feature demonstrably earlier than the submitted feature? | Historical predecessor, with the extent of the match |
| Is similar contemporary or later work affirmatively documented as separately developed? | Independent discoverer, with that documentary basis |
| Does a quotation, datum, image, or factual claim need a source? | Ordinary citation, if a supporting source is located |
| Is there only similarity, an undated source, or no known connection? | An unsettled candidate, not a supported influence or independence finding |

A source may support more than one relationship. Keep separate finding IDs and evidence for each. A source named only in a bibliography does not establish influence. A later acknowledgment records the creator's later account; do not silently backdate it.

For the independent-discoverer group, compare the relevant feature dates. When an earlier work is also independently developed, use predecessor as the group and describe the independently supported development in a note. Evidence of absence must be specific to a record or search scope. It is not a general proof of independence.

## Evidence records

For each finding retain:

- F-ID and C-ID; exact item locator in the submission.
- Creator's public name, source title, and source URL or local file link.
- The exact feature or passage inspected. Use a short paraphrase or a permitted brief quote.
- Publication, release, feature introduction, revision, and access dates as relevant. State what each date represents.
- Source verdict for the claim tested, verification, confidence, and limits.
- Existing rights notice, if a dependency or reproduced asset is involved.

Prefer primary sources: original work, official documentation, release records, a versioned repository, or a dated original. These sources can still be wrong or incomplete. Explain when a claim rests on a reliable secondary account. Repetition across sites is not independent corroboration if the sites share one source.

An archive capture proves that the captured content was present by that time only to the extent the capture actually shows it. A current page describing an old product does not by itself date every feature to the initial release. A title page does not establish the content of a plate that was not viewed.

Use source text tools for readable text and image-capable tools for plates and figures when available. State the actual representation inspected. Do not say that a text tool can never view images; capabilities vary.

## Verification and confidence

| Verification | Meaning |
| :-- | :-- |
| Verified | Evidence inspected in this run adequately supports this particular relationship and its material dates |
| (unverified) | A source, date, match, or required access is missing; also mandatory for every finding in an offline run |
| Disputed | Inspected evidence or reviewers disagree on a material part that the run could not settle |

Local inspection can establish what a submitted file says even when outside verification is unavailable. Under the owner's offline rule, still mark the whole finding (unverified) and describe this narrower observation.

Confidence is claim-specific. **High** means the material relationship, match, identity, and dates are well supported. **Medium** means the claim is adequately qualified but some corroboration or detail is limited. **Low** means important uncertainty remains. Opening a page is never sufficient reason for High confidence. Use Low for unsupported or inaccessible external claims.

A previous report is evidence of what its author reported, not proof that the current reviewer opened its sources. Label inherited verification explicitly. Keep missing originals and historical leads in Unsettled items until rechecked.

## Strength and the exact-rule exception

Strength answers how compelling the credit recommendation is if its relationship is supported. It is not a probability or a legal conclusion.

| Strength | Usual basis |
| :-- | :-- |
| Strong | Explicit documented influence, observed dependency, exact quotation, or specific data tied to its source |
| Moderate | A close and dated predecessor, supported separate development, or a sourced general claim |
| Courtesy | Related background whose connection is limited |

An uncertain finding may carry a proposed strength, such as `Strong (provisional)`, but cannot enter factual paste-ready wording. Do not use courtesy as a substitute for missing evidence of a claimed dependency. An actual optional dependency still deserves its appropriate notice when it is used.

For the owner's exact-rule exception, require all three:

1. The submitted implementation matches the exact rule, not merely a similar layout or an eponym.
2. Authoritative evidence supports the stated attribution.
3. A bounded check addresses credible competing attributions and finds no material unresolved conflict.

Record the evidence and search limits. Describe the supported attribution; do not claim universal undisputed origin. If any part fails, use Moderate or leave the attribution unsettled. The exception changes credit strength only. It never proves direct influence.

Use a separate no-credit disposition for routine practice. "No identifiable credit found in this search" does not mean "the maker invented it."

## Source verdicts

| Verdict | Meaning for the tested claim |
| :-- | :-- |
| Confirmed | Inspected content supports the specific claim |
| Corrected | Inspected content supports a different fact; state the correction |
| Unsupported | Inspected content does not support the claimed relationship or detail |
| Unreachable | The source could not be retrieved; record the bounded attempts |
| Not viewable | The relevant content could not be perceived in the available representation |

A source may be Confirmed for a title and Unsupported for a claimed feature. Record both rather than assigning a blanket verdict to the URL. Corrections need the same evidence standard as original findings.

## Credit wording

Every factual recommendation cites its finding ID and preserves the scope of the table.

| Section | Example pattern |
| :-- | :-- |
| Influences documented in this work | `<Work>'s README identifies <source> as a guide to <specific part>. (F01)` |
| Earlier and related work | `<Specific feature> also appears in <creator>'s <work> (<verified date>), an earlier example located in this review. (F02)` |
| Earlier and related work | `<Records> document <creator>'s separate development of <specific result> in <work>. (F03)` |
| Built with | `<Component>, by <public creator>, <version and source>, under <verified license>. Retain the actual required notices. (F04)` |
| Citations still needed | `<Claim and locator>: add <located reference and precise locator>. (F05)` |

These are patterns, not statements about actual sources. If the version-specific license is unknown, say so beside the dependency and list the exact unresolved notice check. Do not substitute a current upstream license for a historical version's terms.

Creative Commons' [attribution guidance](https://wiki.creativecommons.org/wiki/Recommended_practices_for_attribution) suggests recording title, author, source, and license. That useful pattern is not a universal substitute for the actual license's notice requirements.

Avoid causal words such as "inspired by," "derived from," or "used as a guide" unless the work explicitly documents that role. Avoid "follows a form" when "a similar form appears in" is all the evidence shows. Never allege misconduct. A lexical warning is a prompt for contextual review, not a judgment.

## Difficult cases

- **Missing source:** give the candidate and uncertainty in Unsettled items. Do not invent a citation or a remembered quote.
- **Word match:** inspect both texts, locate them, state the comparison scope, and quote only what the evidence and platform rules allow. Make no claim about causation.
- **Third-party allegation:** treat it as an unverified lead. Investigate the narrow attribution question without endorsing or amplifying the allegation.
- **Unused manifest package:** report it as declared and unconfirmed, not observed use. Check source calls, build role, or other supplied evidence.
- **No imports:** inspect vendored code, assets, services, and implementation notes. Absence of an import does not establish original authorship or exclude dependencies.
- **Conflicting dates:** preserve the competing claims and the reason for preferring one, or leave the date disputed.
- **Unviewed audio or image:** limit findings to the transcript, caption, metadata, or credit record actually inspected.
- **Private people:** use published creator names only; omit private identifiers and personal records.
- **AI assistance:** identify the disclosed platform/model only when records name it. Do not infer training-source use.
