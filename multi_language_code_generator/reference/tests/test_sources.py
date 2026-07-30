from reference.log_analyzer import LogAnalyzer


def test_repeated_source():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request one",
        "2026-07-30 10:01:00 | INFO | api | Request two",
        "2026-07-30 10:02:00 | ERROR | api | Request three",
    ]

    result = analyzer.analyze(logs, threshold=2)

    assert result["repeated_sources"] == ["api"]


def test_multiple_repeated_sources():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request",
        "2026-07-30 10:01:00 | INFO | api | Request",
        "2026-07-30 10:02:00 | INFO | db | Query",
        "2026-07-30 10:03:00 | INFO | db | Query",
    ]

    result = analyzer.analyze(logs, threshold=2)

    assert result["repeated_sources"] == ["api", "db"]


def test_source_not_repeated():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request",
        "2026-07-30 10:01:00 | INFO | db | Query",
    ]

    result = analyzer.analyze(logs, threshold=2)

    assert result["repeated_sources"] == []