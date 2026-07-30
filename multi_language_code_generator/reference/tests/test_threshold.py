import pytest

from reference.log_analyzer import LogAnalyzer


def test_threshold_two():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | One",
        "2026-07-30 10:01:00 | INFO | api | Two",
    ]

    result = analyzer.analyze(logs, threshold=2)

    assert result["repeated_sources"] == ["api"]


def test_threshold_above_source_count():
    analyzer = LogAnalyzer()

    logs = [
        "2026-07-30 10:00:00 | INFO | api | One",
    ]

    result = analyzer.analyze(logs, threshold=2)

    assert result["repeated_sources"] == []


def test_zero_threshold_is_invalid():
    analyzer = LogAnalyzer()

    with pytest.raises(ValueError):
        analyzer.analyze([], threshold=0)