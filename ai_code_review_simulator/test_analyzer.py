"""Tests for analyzer.py (existing functionality)."""

from analyzer import analyze_code


def test_analyze_code_detects_bare_except():
    code = "try:\n    pass\nexcept:\n    pass\n"
    issues = analyze_code(code)
    rules = [i["rule"] for i in issues]
    assert "bare-except" in rules


def test_analyze_code_detects_long_lines():
    code = "x = " + "1" * 100
    issues = analyze_code(code)
    rules = [i["rule"] for i in issues]
    assert "line-length" in rules


def test_analyze_code_clean_code_has_no_issues():
    code = "def add(a, b):\n    return a + b\n"
    assert analyze_code(code) == []