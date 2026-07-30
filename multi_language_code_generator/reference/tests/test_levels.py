from reference.log_analyzer import LogAnalyzer


def test_debug_level():
    analyzer = LogAnalyzer()

    result = analyzer.analyze([
        "2026-07-30 10:00:00 | DEBUG | api | Debug message"
    ])

    assert result["level_counts"]["DEBUG"] == 1


def test_warning_level():
    analyzer = LogAnalyzer()

    result = analyzer.analyze([
        "2026-07-30 10:00:00 | WARNING | api | Warning message"
    ])

    assert result["level_counts"]["WARNING"] == 1


def test_critical_level():
    analyzer = LogAnalyzer()

    result = analyzer.analyze([
        "2026-07-30 10:00:00 | CRITICAL | api | Critical message"
    ])

    assert result["level_counts"]["CRITICAL"] == 1
