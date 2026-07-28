def command_is_known(command, commands):
    return command.lower() in {
        item.lower()
        for item in commands
    }


def test_known_command():
    assert command_is_known(
        "GET",
        ["GET", "SET", "DEL"]
    )


def test_command_lookup_is_case_insensitive():
    assert command_is_known(
        "gEt",
        ["GET", "SET", "DEL"]
    )


def test_unknown_command():
    assert not command_is_known(
        "UNKNOWN",
        ["GET", "SET", "DEL"]
    )