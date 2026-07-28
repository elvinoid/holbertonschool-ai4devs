def response_is_bulk_string(response: bytes):
    """Validate the basic shape of a RESP bulk-string response."""
    if not response.startswith(b"$"):
        return False

    header, separator, body = response.partition(b"\r\n")

    if separator != b"\r\n":
        return False

    try:
        length = int(header[1:])
    except ValueError:
        return False

    return len(body) >= length


def test_valid_bulk_string():
    assert response_is_bulk_string(
        b"$3\r\nGET\r\n"
    )


def test_non_bulk_response_is_rejected():
    assert not response_is_bulk_string(
        b"+OK\r\n"
    )


def test_invalid_length_is_rejected():
    assert not response_is_bulk_string(
        b"$10\r\nGET\r\n"
    )