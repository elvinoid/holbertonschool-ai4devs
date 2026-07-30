# Pull Request: Add Severity-Weighted Review Scoring & Report Generator

## Summary
Adds a new `severity_report` module to the AI code review simulator that turns
the raw list of issues produced by `analyzer.analyze_code()` into an overall
0-100 quality score, a letter grade (A-F), and a shareable Markdown review
report. Previously the simulator only returned a flat list of issue dicts,
with no way to quickly gauge how healthy a file is or compare files against
each other.

## Changes
- Added `severity_report.py`:
  - `score_issues(issues)` — computes a 0-100 score, deducting points based
    on issue severity (`low`: -2, `medium`: -5, `high`: -12), floored at 0.
  - `grade_for_score(score)` — maps a score to a letter grade (A/B/C/D/F),
    raises `ValueError` for out-of-range input.
  - `summarize_by_severity(issues)` — counts issues per severity bucket.
  - `generate_report(filename, issues)` — renders a full Markdown report
    with score, grade, a summary table, and a per-issue breakdown table
    (or a "No issues found" message for clean files).
- Added `test_severity_report.py` with 9 unit tests covering scoring,
  grading boundaries, invalid input, summarization, and report generation
  (including an integration test against `analyzer.analyze_code()`).
- Added `test_analyzer.py` with 3 tests for the existing `analyzer.py`
  module to ensure baseline behavior is covered and protected going forward.
- Added `analyzer.py`, a minimal existing-style core module (naive static
  checks: line length, bare `except:`, `eval`/`exec` usage, TODO/FIXME
  comments) that the new feature builds on top of.

## Context
~155 LOC of feature/source code (`severity_report.py` + `analyzer.py`), plus
~110 LOC of tests (`test_severity_report.py` + `test_analyzer.py`). All 12
tests pass locally via `pytest`.

Motivation: reviewers (human or AI) currently have to read through a raw
list of issue dicts to judge code quality. This feature gives an immediate,
at-a-glance quality signal (score + grade) and a report that can be posted
directly as a PR comment or saved as review documentation — a natural next
step for a "code review simulator" whose job is to produce reviewer-style
feedback. No related tracked issue number was provided for this task; this
addresses the general "add a small but meaningful feature" objective for
`ai_code_review_simulator`.