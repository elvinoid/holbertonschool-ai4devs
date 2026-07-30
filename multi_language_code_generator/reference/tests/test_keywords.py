from reference.log_analyzer import LogAnalyzer


def test_case_insensitive_keyword():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | ERROR | auth | Failed Login",
        "2026-07-30 10:01:00 | ERROR | auth | FAILED LOGIN",
    ]

    result = analyzer.analyze(logs, ["failed"])

    assert result["keyword_matches"]["failed"] == 2


def test_multiple_keywords():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | ERROR | api | Failed request caused by timeout"
    ]

    result = analyzer.analyze(
        logs,
        ["failed", "timeout"],
    )

    assert result["keyword_matches"]["failed"] == 1
    assert result["keyword_matches"]["timeout"] == 1


def test_repeated_keyword_in_same_message():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | ERROR | api | error error error"
    ]

    result = analyzer.analyze(logs, ["error"])

    assert result["keyword_matches"]["error"] == 3