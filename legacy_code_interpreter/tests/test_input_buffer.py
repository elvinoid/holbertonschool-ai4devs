def should_process_input(buffer: bytes):
    """A complete RESP request ends with CRLF."""
    return buffer.endswith(b"\r\n")


def test_incomplete_input_is_not_processed():
    request = b"*1\r\n$3\r\nGET"

    assert not should_process_input(request)


def test_complete_input_is_processed():
    request = b"*1\r\n$3\r\nGET\r\n"

    assert should_process_input(request)


def test_empty_input_is_not_processed():
    assert not should_process_input(b"")