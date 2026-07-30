from reference.log_analyzer import LogAnalyzer


def test_parse_valid_log():
    analyzer = LogAnalyzer()

    result = analyzer.parse_line(
        "2026-07-30 10:00:00 | INFO | api | Request received"
    )

    assert result["timestamp"] == "2026-07-30 10:00:00"
    assert result["level"] == "INFO"
    assert result["source"] == "api"
    assert result["message"] == "Request received"


def test_parse_log_with_pipe_in_message():
    analyzer = LogAnalyzer()

    result = analyzer.parse_line(
        "2026-07-30 10:00:00 | ERROR | api | Error | connection failed"
    )

    assert result["level"] == "ERROR"
    assert result["source"] == "api"
    assert result["message"] == "Error | connection failed"


def test_parse_malformed_log():
    analyzer = LogAnalyzer()

    try:
        analyzer.parse_line("invalid log")
        assert False
    except ValueError:
        assert True