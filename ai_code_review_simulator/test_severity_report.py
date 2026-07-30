"""Tests for severity_report.py"""

import pytest

from severity_report import (
    score_issues,
    grade_for_score,
    summarize_by_severity,
    generate_report,
)
from analyzer import analyze_code


def test_score_issues_no_issues_is_perfect():
    assert score_issues([]) == 100


def test_score_issues_deducts_by_severity():
    issues = [
        {"line": 1, "message": "x", "severity": "low", "rule": "r"},
        {"line": 2, "message": "y", "severity": "medium", "rule": "r"},
        {"line": 3, "message": "z", "severity": "high", "rule": "r"},
    ]
    # 100 - 2 - 5 - 12 = 81
    assert score_issues(issues) == 81


def test_score_issues_never_goes_below_zero():
    issues = [
        {"line": i, "message": "bad", "severity": "high", "rule": "r"}
        for i in range(20)
    ]
    assert score_issues(issues) == 0


def test_grade_for_score_boundaries():
    assert grade_for_score(100) == "A"
    assert grade_for_score(90) == "A"
    assert grade_for_score(89) == "B"
    assert grade_for_score(80) == "B"
    assert grade_for_score(70) == "C"
    assert grade_for_score(60) == "D"
    assert grade_for_score(59) == "F"
    assert grade_for_score(0) == "F"


def test_grade_for_score_invalid_raises():
    with pytest.raises(ValueError):
        grade_for_score(101)
    with pytest.raises(ValueError):
        grade_for_score(-1)


def test_summarize_by_severity_counts_correctly():
    issues = [
        {"line": 1, "message": "a", "severity": "high", "rule": "r"},
        {"line": 2, "message": "b", "severity": "high", "rule": "r"},
        {"line": 3, "message": "c", "severity": "low", "rule": "r"},
    ]
    counts = summarize_by_severity(issues)
    assert counts == {"low": 1, "medium": 0, "high": 2}


def test_generate_report_no_issues():
    report = generate_report("clean.py", [])
    assert "Score:** 100/100" in report
    assert "Grade:** A" in report
    assert "No issues found" in report


def test_generate_report_includes_issue_table():
    issues = [
        {"line": 5, "message": "Bare except clause",
         "severity": "high", "rule": "bare-except"},
    ]
    report = generate_report("bad.py", issues)
    assert "# Code Review Report: `bad.py`" in report
    assert "| 5 | high | bare-except | Bare except clause |" in report
    assert "| High     | 1 |" in report


def test_generate_report_integrates_with_analyzer():
    code = "def f():\n    try:\n        pass\n    except:\n        pass\n"
    issues = analyze_code(code)
    report = generate_report("integration.py", issues)
    assert "bare-except" in report
    assert "Grade:**" in report