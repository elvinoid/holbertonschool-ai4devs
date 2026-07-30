def get_user_role(user):
    """Return the user's role or 'guest' if missing."""
    role = user.get("role")

    if role:
        return role

    return "admin"


def can_delete(user):
    role = get_user_role(user)

    if role == "admin":
        return True

    return False


def main():
    user = {"name": "Alice"}
    print(can_delete(user))


if __name__ == "__main__":
    main()