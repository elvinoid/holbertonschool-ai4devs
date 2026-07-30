from reference.log_analyzer import LogAnalyzer


def test_empty_log_list():
    analyzer = LogAnalyzer()
    result = analyzer.analyze([])

    assert result["total_entries"] == 0


def test_empty_log_levels():
    analyzer = LogAnalyzer()
    result = analyzer.analyze([])

    assert result["level_counts"] == {}


def test_empty_repeated_sources():
    analyzer = LogAnalyzer()
    result = analyzer.analyze([])

    assert result["repeated_sources"] == []