import pytest

from reference.log_analyzer import LogAnalyzer


def test_empty_logs():
    analyzer = LogAnalyzer()

    result = analyzer.analyze([])

    assert result == {
        "total_entries": 0,
        "level_counts": {},
        "keyword_matches": {},
        "repeated_sources": [],
    }


def test_empty_keywords():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request received"
    ]

    result = analyzer.analyze(logs, [])

    assert result["total_entries"] == 1
    assert result["keyword_matches"] == {}


def test_malformed_entry_is_skipped():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Valid request",
        "this is not a valid log",
    ]

    result = analyzer.analyze(logs)

    assert result["total_entries"] == 1


def test_unknown_log_level_is_skipped():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INVALID | api | Invalid level",
        "2026-07-30 10:01:00 | ERROR | api | Valid error",
    ]

    result = analyzer.analyze(logs)

    assert result["total_entries"] == 1
    assert result["level_counts"] == {"ERROR": 1}


def test_threshold_one():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request",
        "2026-07-30 10:01:00 | INFO | db | Query",
    ]

    result = analyzer.analyze(logs, threshold=1)

    assert result["repeated_sources"] == ["api", "db"]


def test_invalid_threshold():
    analyzer = LogAnalyzer()

    with pytest.raises(ValueError):
        analyzer.analyze([], threshold=0)


def test_source_below_threshold():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | Request",
        "2026-07-30 10:01:00 | INFO | db | Query",
    ]

    result = analyzer.analyze(logs, threshold=2)

    assert result["repeated_sources"] == []