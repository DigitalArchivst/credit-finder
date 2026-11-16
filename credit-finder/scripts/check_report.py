#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Read-only structural check for Credit Finder v1.3.2 reports, Python 3.10+.

This checks a limited Markdown report contract, not truth, evidence quality,
copyright permission, license validity, or fairness. Warnings need human context
review. It never edits reports. Exit codes: 0 pass, 1 structural errors, 2 usage
or I/O failure. Markdown parsing is intentionally limited to this report format.
Exactly one '- Web access: yes' or '- Web access: no' entry is required inside
'How this was done'; ordinary emphasis and punctuation-led explanations are accepted.
Narrative references to offline work do not replace this declaration.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys


def _skill_version() -> str | None:
    """Read metadata.version from the SKILL.md beside this script, if present."""
    skill_md = Path(__file__).resolve().parents[1] / "SKILL.md"
    try:
        text = skill_md.read_text(encoding="utf-8")
    except OSError:
        return None
    match = re.search(r'^\s+version:\s*"?(\d+\.\d+(?:\.\d+)?)"?\s*$', text, re.M)
    return match.group(1) if match else None


SKILL_VERSION = _skill_version()


HEADERS = ["Finding", "Point and locator", "Creator and work", "Group",
           "Strength", "Verification", "Confidence", "Evidence"]
SECTIONS = ["Summary", "How this was done", "Findings", "Unsettled items",
            "Ready-to-paste credit wording", "Rights and reuse",
            "License and disclaimer"]
GROUPS = {"Direct influence", "Historical predecessor", "Technical dependency",
          "Independent discoverer", "Ordinary citation"}
PLACEHOLDER = re.compile(r"<[^>\n]+>|\b(?:TODO|TBD|PLACEHOLDER)\b|\{\{.*?\}\}", re.I)
FINDING_ID = re.compile(r"\bF\d{2,}\b")


def has_placeholder(value: str) -> bool:
    # Markdown autolinks are evidence, not template fields.
    value = re.sub(r"<https?://[^>]+>", "", value)
    return bool(PLACEHOLDER.search(value))


def without_emphasis(value: str) -> str:
    """Normalize ordinary Markdown emphasis for metadata and zero-count text."""
    return re.sub(r"[*_`]+", "", value)


def table_cells(line: str) -> list[str]:
    """Split pipe cells, preserving escaped pipes and inline code spans."""
    cells: list[str] = []
    buf: list[str] = []
    code_ticks = 0
    index = 0
    text = line.strip()
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text):
            buf.extend(text[index:index + 2])
            index += 2
            continue
        if char == "`":
            end = index
            while end < len(text) and text[end] == "`":
                end += 1
            count = end - index
            if not code_ticks:
                code_ticks = count
            elif count == code_ticks:
                code_ticks = 0
            buf.append(text[index:end])
            index = end
            continue
        if char == "|" and not code_ticks:
            cells.append("".join(buf).strip())
            buf = []
        else:
            buf.append(char)
        index += 1
    cells.append("".join(buf).strip())
    if text.startswith("|") and cells and cells[0] == "":
        cells.pop(0)
    if text.endswith("|") and cells and cells[-1] == "":
        cells.pop()
    return cells


def visible_lines(text: str) -> list[str]:
    """Ignore fenced examples when checking real report structure."""
    result = []
    fence_char = ""
    fence_size = 0
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if match:
            marker = match.group(1)
            if not fence_char:
                fence_char, fence_size = marker[0], len(marker)
            elif marker[0] == fence_char and len(marker) >= fence_size:
                fence_char = ""
            continue
        if not fence_char:
            result.append(line)
    return result


def has_locator(evidence: str) -> bool:
    if re.search(r"https?://[^\s<>]+|\[[^\]]+\]\([^\s)]+\)", evidence):
        return True
    # A backticked filename/path plus a line/section anchor is a local locator.
    for value in re.findall(r"`([^`]+)`", evidence):
        if (re.search(r"(?:[\w.-]+/)*[\w.-]+\.[A-Za-z0-9]+", value)
                and (re.search(r"(?:[:#]L?\d+|\blines?\s+\d+|#\w)", value, re.I)
                     or re.search(r"\b(?:lines?|section|paragraph|page)\s+\S+", evidence, re.I))):
            return True
    return False


def check_report(text: str) -> tuple[list[str], list[str]]:
    """Return structural errors and advisory warnings without changing input."""
    errors: list[str] = []
    warnings: list[str] = []
    lines = visible_lines(text)
    visible = "\n".join(lines)
    titles = [line for line in lines if re.match(r"^#\s+CREDIT report:\s*", line, re.I)]
    if not titles or not re.match(r"^#\s+CREDIT report:\s*\S", titles[0], re.I):
        errors.append("Missing nonempty '# CREDIT report:' title.")
    elif has_placeholder(titles[0]):
        errors.append("Title contains a placeholder.")
    version_match = re.search(r"Credit Finder v(\d+\.\d+(?:\.\d+)?)", visible)
    if not version_match:
        errors.append("Missing 'Credit Finder vX.Y' version marker.")
    elif SKILL_VERSION and version_match.group(1) != SKILL_VERSION:
        warnings.append(
            f"Report names Credit Finder v{version_match.group(1)}, but this skill folder is v{SKILL_VERSION}."
        )
    if not re.search(r"\bExperimental\b", visible, re.I):
        errors.append("Missing Experimental notice.")
    if not re.search(r"\bAS\s+IS\b", visible, re.I):
        errors.append("Missing AS IS notice.")

    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in lines:
        match = re.match(r"^##\s+(.+?)\s*#*\s*$", line)
        if match:
            current = match.group(1).strip()
            if current in sections:
                errors.append(f"Duplicate H2 section: {current}.")
            sections.setdefault(current, [])
        elif current is not None:
            sections[current].append(line)
    for section in SECTIONS:
        if section not in sections:
            errors.append(f"Missing H2 section: {section}.")
        elif not any(line.strip() for line in sections[section]):
            errors.append(f"Empty required section: {section}.")

    license_text = " ".join(sections.get("License and disclaimer", []))
    if not (re.search(r"\bMIT\b", license_text)
            and re.search(r"\b(?:skill|Credit Finder)\b", license_text, re.I)):
        errors.append("License and disclaimer must identify the skill's MIT license.")
    report_notice = re.search(r"\breport\b", license_text, re.I) and (
        re.search(r"\b(?:CC BY 4\.0|Creative Commons Attribution 4\.0)\b", license_text, re.I)
        or re.search(r"\bno\s+(?:new\s+)?licen[cs]e\b|\bno\s+new\s+grant\b", license_text, re.I)
        or re.search(r"\breport licen[cs]e\s*:\s*\S", license_text, re.I))
    if not report_notice:
        errors.append("Missing report license or no-new-license statement.")
    mode_line = next((line for line in sections.get("How this was done", [])
                      if re.match(r"^\s*-\s*Mode\s*:", line, re.I)), "")
    is_quick = bool(re.search(r"\bquick\b", mode_line, re.I))
    if not is_quick and not re.search(r"\bnoninfringement\b", license_text, re.I):
        warnings.append("Non-Quick report appears to use the short notice; Standard, Deep, offline, partial, and self-test reports need the full notice.")
    for section in ("How this was done", "License and disclaimer"):
        for line in sections.get(section, []):
            if has_placeholder(line):
                errors.append(f"Placeholder in required metadata: {section}.")
                break

    access_entries = []
    for line in sections.get("How this was done", []):
        match = re.match(r"^\s*-\s*Web access:\s*(.*?)\s*$", without_emphasis(line), re.I)
        if match:
            value = match.group(1).lower()
            declared = re.fullmatch(r"(yes|no)(?:\s*[.,;:].*)?", value)
            access_entries.append(declared.group(1) if declared else value)
    if not access_entries:
        errors.append("Missing canonical Web access metadata: use '- Web access: yes' or '- Web access: no'.")
    elif len(access_entries) != 1:
        errors.append("Web access metadata must have exactly one entry; duplicate or contradictory entries are invalid.")
    if any(value not in {"yes", "no"} for value in access_entries):
        errors.append("Web access metadata must start with yes or no; explanations need punctuation.")
    offline = "no" in access_entries
    finding_lines = sections.get("Findings", [])
    findings: dict[str, str] = {}
    tables = 0
    row_count = 0
    index = 0
    while index < len(finding_lines):
        line = finding_lines[index]
        if "|" not in line or table_cells(line) != HEADERS:
            index += 1
            continue
        tables += 1
        index += 1
        divider = table_cells(finding_lines[index]) if index < len(finding_lines) else []
        if len(divider) != 8 or not all(re.fullmatch(r":?-+:?", cell) for cell in divider):
            errors.append("Findings table must have an eight-cell Markdown separator row.")
        else:
            index += 1
        while index < len(finding_lines) and "|" in finding_lines[index]:
            row_count += 1
            cells = table_cells(finding_lines[index])
            index += 1
            if len(cells) != 8:
                errors.append(f"Findings row {row_count} has {len(cells)} cells; expected 8.")
                continue
            fid, point, creator, group, strength, verification, confidence, evidence = cells
            if any(not cell or has_placeholder(cell) for cell in cells):
                errors.append(f"Finding {fid or row_count} has empty or placeholder cells.")
            if not re.fullmatch(r"F\d{2,}", fid):
                errors.append(f"Invalid finding ID: {fid!r}.")
            if fid in findings:
                errors.append(f"Duplicate finding ID: {fid}.")
            findings[fid] = verification
            if group not in GROUPS:
                errors.append(f"{fid}: invalid group {group!r}.")
            if not re.fullmatch(r"(?:Strong|Moderate|Courtesy)(?: \(provisional\))?", strength):
                errors.append(f"{fid}: invalid strength {strength!r}.")
            if verification not in {"Verified", "(unverified)", "Disputed"}:
                errors.append(f"{fid}: invalid verification {verification!r}.")
            if verification != "Verified" and not strength.endswith(" (provisional)"):
                errors.append(f"{fid}: uncertain finding needs a provisional strength.")
            if confidence not in {"High", "Medium", "Low"}:
                errors.append(f"{fid}: invalid confidence {confidence!r}.")
            if offline and verification != "(unverified)":
                errors.append(f"{fid}: offline findings must be (unverified).")
            if verification == "Verified" and not has_locator(evidence):
                errors.append(f"{fid}: verified evidence needs a URL, link, or local file locator.")
    zero_statement = re.compile(
        r"\b(?:no|zero|0)\s+(?:accepted\s+)?(?:attribution\s+)?findings\b", re.I)
    no_findings = bool(zero_statement.search(without_emphasis("\n".join(finding_lines))))
    if not tables and not no_findings:
        errors.append("Missing findings table with the exact eight headers.")
    if not row_count and not no_findings:
        errors.append("Zero finding rows require an explicit no-findings statement, such as 'No accepted findings'.")
    if no_findings and row_count:
        errors.append("The no-findings statement contradicts populated finding rows.")
    if tables > 1:
        errors.append("Use one findings table.")

    paste = sections.get("Ready-to-paste credit wording", [])
    for fid in sorted(set(FINDING_ID.findall("\n".join(paste)))):
        if fid not in findings:
            errors.append(f"Ready-to-paste wording refers to unknown finding {fid}.")
        elif findings[fid] != "Verified":
            errors.append(f"Ready-to-paste wording refers to uncertain finding {fid}.")
    for line in paste:
        if (re.match(r"^\s*(?:[-*+] |\d+\. )", line)
                and not FINDING_ID.search(line)
                and not re.match(r"^\s*(?:[-*+] |\d+\. )(?:None\b|No\b)", line, re.I)):
            warnings.append("Paste-ready bullet has no finding ID; manually check its evidence link.")
    risky = sorted(set(re.findall(r"\b(?:copied|stole|stolen|plagiari[sz](?:ed|m)|lifted|"
                                 r"ripped off|knock-off|clone)\b", visible, re.I)))
    if risky:
        warnings.append("Potential accusation words: " + ", ".join(risky)
                        + ". Manually review context; disclaimers and quotations can be legitimate.")
    return errors, warnings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                     epilog="Checks structure only; cannot verify truth or legal rights.")
    parser.add_argument("report", type=Path, help="Markdown report to inspect without editing")
    args = parser.parse_args(argv)
    try:
        content = args.report.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        print(f"I/O error: {exc}", file=sys.stderr)
        return 2
    errors, warnings = check_report(content)
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    for warning in warnings:
        print(f"WARNING: {warning}", file=sys.stderr)
    if errors:
        print(f"Structural check failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print("Structural check passed. Evidence and wording still require human review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
