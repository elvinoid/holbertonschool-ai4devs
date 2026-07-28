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
        index += 2

    return result


def test_parse_resp_array():
    request = b"*2\r\n$3\r\nGET\r\n$3\r\nkey\r\n"

    assert parse_simple_resp_array(request) == ["GET", "key"]


def test_parse_empty_resp_array():
    request = b"*0\r\n"

    assert parse_simple_resp_array(request) == []