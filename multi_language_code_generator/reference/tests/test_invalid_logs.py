import pytest

from reference.log_analyzer import LogAnalyzer


def test_invalid_log_format():
    analyzer = LogAnalyzer()

    with pytest.raises(ValueError):
        analyzer.parse_line("not a valid log")


def test_missing_source():
    analyzer = LogAnalyzer()

    with pytest.raises(ValueError):
        analyzer.parse_line(
            "2026-07-30 10:00:00 | ERROR | | Failed"
        )


def test_unknown_level():
    analyzer = LogAnalyzer()

    with pytest.raises(ValueError):
        analyzer.parse_line(
            "2026-07-30 10:00:00 | UNKNOWN | api | Message"
        )