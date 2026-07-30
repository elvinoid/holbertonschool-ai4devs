from reference.log_analyzer import LogAnalyzer


def test_normal_log_analysis():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request received",
        "2026-07-30 10:01:00 | ERROR | auth | Failed login",
        "2026-07-30 10:02:00 | ERROR | auth | Failed login",
    ]

    result = analyzer.analyze(
        logs,
        ["failed"],
        2,
    )

    assert result["total_entries"] == 3
    assert result["level_counts"]["INFO"] == 1
    assert result["level_counts"]["ERROR"] == 2
    assert result["keyword_matches"]["failed"] == 2
    assert result["repeated_sources"] == ["auth"]


def test_single_log():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request received"
    ]

    result = analyzer.analyze(logs)

    assert result["total_entries"] == 1
    assert result["level_counts"] == {"INFO": 1}


def test_multiple_log_levels():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | DEBUG | api | Debug",
        "2026-07-30 10:01:00 | INFO | api | Info",
        "2026-07-30 10:02:00 | WARNING | api | Warning",
        "2026-07-30 10:03:00 | ERROR | api | Error",
        "2026-07-30 10:04:00 | CRITICAL | api | Critical",
    ]

    result = analyzer.analyze(logs)

    assert result["total_entries"] == 5
    assert result["level_counts"] == {
        "DEBUG": 1,
        "INFO": 1,
        "WARNING": 1,
        "ERROR": 1,
        "CRITICAL": 1,
    }