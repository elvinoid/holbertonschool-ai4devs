import pytest


def parse_simple_resp_array(data: bytes):
    """Parse a small RESP2 array containing bulk strings."""
    lines = data.split(b"\r\n")
    assert lines[0].startswith(b"*")
    count = int(lines[0][1:])
    result = []
    index = 1

    for _ in range(count):
        assert lines[index].startswith(b"$")
        length = int(lines[index][1:])
        index += 1
        value = lines[index]
        assert len(value) == length
        result.append(value.decode())
        index += 2  # value + CRLF

    return result


def incremental_rehash(items, bucket_count):
    """Small model of moving items into a resized hash table."""
    new_count = bucket_count * 2
    return {item: hash(item) % new_count for item in items}


def command_is_known(command, commands):
    return command.lower() in {item.lower() for item in commands}


def should_process_input(buffer: bytes):
    """A simple model: a complete RESP request ends with CRLF."""
    return buffer.endswith(b"\r\n")


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


def test_parse_resp_array():
    request = b"*2\r\n$3\r\nGET\r\n$3\r\nkey\r\n"

    assert parse_simple_resp_array(request) == ["GET", "key"]


def test_parse_resp_array_rejects_wrong_bulk_length():
    request = b"*1\r\n$5\r\nGET\r\n"

    with pytest.raises(AssertionError):
        parse_simple_resp_array(request)


def test_command_lookup_is_case_insensitive():
    assert command_is_known("gEt", ["GET", "SET", "DEL"])
    assert not command_is_known("UNKNOWN", ["GET", "SET", "DEL"])


def test_incremental_rehash_changes_bucket_distribution():
    items = ["alpha", "beta", "gamma", "delta"]

    old = {
        item: hash(item) % 4
        for item in items
    }

    new = incremental_rehash(items, 4)

    assert set(new) == set(items)
    assert all(0 <= bucket < 8 for bucket in new.values())

    # The resize must use the new table size.
    assert any(
        old[item] != new[item]
        for item in items
    ) or len(items) == 0


def test_input_processing_requires_complete_line():
    assert not should_process_input(
        b"*1\r\n$3\r\nGET"
    )

    assert should_process_input(
        b"*1\r\n$3\r\nGET\r\n"
    )


def test_bulk_string_response_has_expected_shape():
    assert response_is_bulk_string(
        b"$3\r\nGET\r\n"
    )

    assert not response_is_bulk_string(
        b"+OK\r\n"
    )


def test_bulk_string_response_rejects_invalid_length():
    assert not response_is_bulk_string(
        b"$10\r\nGET\r\n"
    )