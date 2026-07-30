"""
analyzer.py

Minimal AI code review simulator core.

Scans a piece of Python source code (as text) and returns a list of
"issues" found, each represented as a dict:

    {
        "line": <int>,
        "message": <str>,
        "severity": "low" | "medium" | "high",
        "rule": <str>,
    }

This module represents the existing functionality of the simulator.
The new feature added in this PR (severity_report.py) builds on top
of the list of issues produced here.
"""

from typing import List, Dict


def analyze_code(code: str) -> List[Dict]:
    """Run a small set of naive static checks against `code`.

    This is intentionally simple: it's a simulator, not a real linter.
    """
    issues: List[Dict] = []
    lines = code.splitlines()

    for i, line in enumerate(lines, start=1):
        stripped = line.rstrip()

        if len(stripped) > 79:
            issues.append({
                "line": i,
                "message": "Line exceeds 79 characters",
                "severity": "low",
                "rule": "line-length",
            })

        if "except:" in stripped:
            issues.append({
                "line": i,
                "message": "Bare except clause",
                "severity": "high",
                "rule": "bare-except",
            })

        if "eval(" in stripped or "exec(" in stripped:
            issues.append({
                "line": i,
                "message": "Use of eval()/exec() is dangerous",
                "severity": "high",
                "rule": "dangerous-call",
            })

        if "TODO" in stripped or "FIXME" in stripped:
            issues.append({
                "line": i,
                "message": "Unresolved TODO/FIXME comment",
                "severity": "medium",
                "rule": "todo-comment",
            })

    return issues