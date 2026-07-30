from reference.log_analyzer import LogAnalyzer


def test_keyword_not_found():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request successful"
    ]

    result = analyzer.analyze(logs, ["failed"])

    assert result["keyword_matches"]["failed"] == 0


def test_keyword_case_insensitive():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | ERROR | api | FAILED request"
    ]

    result = analyzer.analyze(logs, ["failed"])

    assert result["keyword_matches"]["failed"] == 1


def test_keyword_occurs_multiple_times():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | ERROR | api | failed failed failed"
    ]

    result = analyzer.analyze(logs, ["failed"])

    assert result["keyword_matches"]["failed"] == 3