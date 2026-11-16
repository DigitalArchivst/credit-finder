#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Meaningful structural contract tests. Run with Python 3.10+ directly."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


CHECKER = Path(__file__).resolve().parent / "check_report.py"
SPEC = importlib.util.spec_from_file_location("check_report", CHECKER)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

ROW = "| F01 | Formula (`app.py:3`) | Example author, Method | Historical predecessor | Moderate | Verified | High | [Paper](https://example.org/paper), p. 3 |"
REPORT = """# CREDIT report: Example

Prepared with Credit Finder v1.3.2. Experimental.

## Summary

One earlier method found. This does not claim anyone copied anyone.

## How this was done

- Web access: yes
- Mode: standard

## Findings

| Finding | Point and locator | Creator and work | Group | Strength | Verification | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
ROW

## Unsettled items

None found.

## Ready-to-paste credit wording

- F01: Example author described this method.

## Rights and reuse

No source material is reproduced.

## License and disclaimer

The Credit Finder skill is MIT licensed. This report makes no new license grant.
Provided “AS IS” without warranty.
""".replace("ROW", ROW)


class ReportCheckerTests(unittest.TestCase):
    def check(self, report=REPORT):
        return MODULE.check_report(report)

    def test_compliant_and_read_only_cli(self):
        self.assertEqual(self.check()[0], [])
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "report.md"
            path.write_text(REPORT)
            before = path.read_bytes()
            result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(path.read_bytes(), before)
            path.write_text(REPORT.replace("Experimental", "Omitted"))
            invalid_before = path.read_bytes()
            invalid = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True)
            self.assertEqual(invalid.returncode, 1, invalid.stderr)
            self.assertEqual(path.read_bytes(), invalid_before)

    def test_each_required_notice(self):
        for phrase in ("Credit Finder v1.3.2", "Experimental", "AS IS", "MIT", "no new license"):
            with self.subTest(phrase=phrase):
                self.assertTrue(self.check(REPORT.replace(phrase, "omitted"))[0])

    def test_offline_requires_unverified(self):
        offline = REPORT.replace("Web access: yes", "Web access: no")
        self.assertTrue(any("offline" in error for error in self.check(offline)[0]))
        offline = offline.replace("| Moderate | Verified |", "| Moderate (provisional) | (unverified) |")
        offline = offline.replace("- F01: Example author described this method.", "- None verified.")
        self.assertEqual(self.check(offline)[0], [])

    def test_bold_offline_metadata_and_narrative_isolation(self):
        for declaration in ("- **Web access:** no", "- Web access: **no**",
                            "- **Web access:** **no**", "- Web access: no.",
                            "- Web access: no; network access was disabled."):
            with self.subTest(declaration=declaration):
                report = REPORT.replace("- Web access: yes", declaration)
                self.assertTrue(any("offline" in error for error in self.check(report)[0]))
        prose = REPORT.replace("One earlier method found.", "No web searches were needed for a hypothetical offline fallback. One earlier method found.")
        prose = prose.replace("## Rights and reuse", "- **Web access:** no\n\n## Rights and reuse")
        self.assertEqual(self.check(prose)[0], [])

    def test_web_access_metadata_required_and_unambiguous(self):
        variants = (REPORT.replace("- Web access: yes", "No web searches were performed."),
                    REPORT.replace("- Web access: yes", "- Web access: yes\n- Web access: no"),
                    REPORT.replace("- Web access: yes", "- Web access: yes\n- **Web access:** yes"),
                    REPORT.replace("- Web access: yes", "- Web access: unknown"))
        for report in variants:
            with self.subTest(report=report):
                self.assertTrue(any("Web access metadata" in error for error in self.check(report)[0]))
        for declaration in ("- Web access: yes.",
                            "- Web access: yes, through search and page opens."):
            with self.subTest(declaration=declaration):
                self.assertEqual(self.check(REPORT.replace("- Web access: yes", declaration))[0], [])

    def test_uncertain_paste_and_provisional(self):
        for state in ("(unverified)", "Disputed"):
            report = REPORT.replace("| Verified |", f"| {state} |")
            errors = self.check(report)[0]
            self.assertTrue(any("provisional" in error for error in errors))
            self.assertTrue(any("uncertain finding" in error for error in errors))

    def test_duplicate_and_malformed_rows(self):
        self.assertTrue(any("Duplicate finding" in error for error in self.check(REPORT.replace(ROW, ROW + "\n" + ROW))[0]))
        self.assertTrue(any("expected 8" in error for error in self.check(REPORT.replace(ROW, ROW.replace("| High ", "")))[0]))

    def test_disclaimer_word_is_warning_only(self):
        errors, warnings = self.check()
        self.assertEqual(errors, [])
        self.assertTrue(any("copied" in warning and "context" in warning for warning in warnings))

    def test_unknown_ready_id(self):
        report = REPORT.replace("- F01:", "- F99:")
        self.assertTrue(any("unknown finding F99" in error for error in self.check(report)[0]))

    def test_no_findings(self):
        report = REPORT.replace(ROW, "No findings.").replace("- F01: Example author described this method.", "- None.")
        self.assertEqual(self.check(report)[0], [])
        self.assertTrue(any("contradicts" in error for error in self.check(REPORT.replace(ROW, ROW + "\n\nNo findings."))[0]))

    def test_real_zero_findings_regression(self):
        actual = Path(__file__).resolve().parents[1] / "evals/fixtures/offline/offline-report-raw-v1.2.md"
        report = actual.read_text(encoding="utf-8")
        self.assertTrue(any("Missing canonical Web access metadata" in error for error in self.check(report)[0]))
        amended = report.replace("## How this was done", "## How this was done\n\n- Web access: no", 1)
        self.assertEqual(self.check(amended)[0], [])
        for statement in ("No accepted findings.", "There are **zero accepted attribution findings**.",
                          "0 attribution findings."):
            with self.subTest(statement=statement):
                report = REPORT.replace(ROW, statement).replace("- F01: Example author described this method.", "- None.")
                self.assertEqual(self.check(report)[0], [])
                populated = REPORT.replace(ROW, ROW + "\n\n" + statement)
                self.assertTrue(any("contradicts" in error for error in self.check(populated)[0]))

    def test_quick_short_notice_and_full_notice_rule(self):
        short = ("Experimental output from Credit Finder v1.3.2 (MIT License). Provided AS IS, without warranty. "
                 "This is research help, not a finding about legal rights, originality, or misconduct. "
                 "No license is granted over this report, the reviewed work, or third-party material.")
        head, _ = REPORT.split("## License and disclaimer")
        quick = (head + "## License and disclaimer\n\n" + short + "\n").replace("- Mode: standard", "- Mode: quick")
        errors, warnings = self.check(quick)
        self.assertEqual(errors, [])
        self.assertFalse(any("short notice" in w for w in warnings))
        standard = quick.replace("- Mode: quick", "- Mode: standard")
        self.assertTrue(any("short notice" in w for w in self.check(standard)[1]))

    def test_escaped_and_code_pipes(self):
        report = REPORT.replace("Formula (`app.py:3`)", r"A \| B and `x|y` (`app.py:3`)")
        self.assertEqual(self.check(report)[0], [])
        report = report.replace("| ---", "| :--").replace("[Paper](https://example.org/paper)", "<https://example.org/paper>")
        self.assertEqual(self.check(report)[0], [])

    def test_io_and_argument_failure(self):
        with tempfile.TemporaryDirectory() as folder:
            for args in ([str(Path(folder) / "missing.md")], []):
                result = subprocess.run([sys.executable, str(CHECKER), *args], capture_output=True)
                self.assertEqual(result.returncode, 2)

    def test_evidence_and_placeholders(self):
        report = REPORT.replace("[Paper](https://example.org/paper), p. 3", "source not located")
        self.assertTrue(any("verified evidence" in error for error in self.check(report)[0]))
        local = REPORT.replace("[Paper](https://example.org/paper), p. 3", "`source.md:12`")
        self.assertEqual(self.check(local)[0], [])
        self.assertTrue(self.check(REPORT.replace("Example author, Method", "<creator>"))[0])

    def test_wrong_headers_and_fenced_fake_report(self):
        self.assertTrue(self.check(REPORT.replace("| Finding | Point", "| ID | Point"))[0])
        self.assertTrue(self.check("```markdown\n" + REPORT + "\n```\n")[0])


if __name__ == "__main__":
    unittest.main()
