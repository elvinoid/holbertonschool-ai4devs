"""
severity_report.py

New feature: Severity-Weighted Review Scoring & Report Generator.

Given the list of issues produced by `analyzer.analyze_code()`, this
module computes an overall quality score for the reviewed file and
renders a human-readable Markdown report summarizing the findings.

Motivation
----------
Today the simulator only returns a flat list of issues. A reviewer
(human or AI) has no quick way to gauge "how bad" a file is overall,
or to compare files against each other. This feature adds:

  1. `score_issues()` - a 0-100 quality score, weighted by severity.
  2. `grade_for_score()` - maps a score to a letter grade (A-F).
  3. `generate_report()` - builds a Markdown-formatted review report,
     including a summary table and a per-issue breakdown.

This directly supports the "code review simulator" use case: after
analyzing a file, the tool can now output a shareable, readable
report instead of just raw issue dicts.
"""

from typing import List, Dict

# How many points each severity deducts from a perfect 100 score.
SEVERITY_WEIGHTS = {
    "low": 2,
    "medium": 5,
    "high": 12,
}

# Score thresholds for letter grades, checked in order (highest first).
GRADE_THRESHOLDS = [
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
]


def score_issues(issues: List[Dict]) -> int:
    """Compute a 0-100 quality score from a list of issues.

    Each issue deducts points based on its severity. The score never
    drops below 0, even if there are many severe issues.
    """
    score = 100
    for issue in issues:
        severity = issue.get("severity", "low")
        score -= SEVERITY_WEIGHTS.get(severity, 1)

    return max(0, score)


def grade_for_score(score: int) -> str:
    """Map a 0-100 score to a letter grade (A/B/C/D/F)."""
    if not 0 <= score <= 100:
        raise ValueError("score must be between 0 and 100")

    for threshold, grade in GRADE_THRESHOLDS:
        if score >= threshold:
            return grade
    return "F"


def summarize_by_severity(issues: List[Dict]) -> Dict[str, int]:
    """Count how many issues fall into each severity bucket."""
    counts = {"low": 0, "medium": 0, "high": 0}
    for issue in issues:
        severity = issue.get("severity", "low")
        counts[severity] = counts.get(severity, 0) + 1
    return counts


def generate_report(filename: str, issues: List[Dict]) -> str:
    """Render a Markdown report summarizing the review of `filename`.

    The report includes:
      - Overall score and letter grade
      - A count of issues per severity
      - A table listing every issue with its line, severity, and rule
    """
    score = score_issues(issues)
    grade = grade_for_score(score)
    counts = summarize_by_severity(issues)

    lines = [
        f"# Code Review Report: `{filename}`",
        "",
        f"**Score:** {score}/100  ",
        f"**Grade:** {grade}",
        "",
        "## Summary",
        "",
        "| Severity | Count |",
        "|----------|-------|",
        f"| High     | {counts['high']} |",
        f"| Medium   | {counts['medium']} |",
        f"| Low      | {counts['low']} |",
        "",
    ]

    if issues:
        lines.append("## Issues")
        lines.append("")
        lines.append("| Line | Severity | Rule | Message |")
        lines.append("|------|----------|------|---------|")
        for issue in sorted(issues, key=lambda i: i["line"]):
            lines.append(
                f"| {issue['line']} | {issue['severity']} | "
                f"{issue['rule']} | {issue['message']} |"
            )
    else:
        lines.append("No issues found. Great job!")

    return "\n".join(lines) + "\n"