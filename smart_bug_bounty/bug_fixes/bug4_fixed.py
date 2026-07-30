def get_user_role(user):
    """Return the user's role."""
    if user is None:
        return "guest"

    role = user.get("role")

    if role:
        return role

    return "guest"


def can_delete(user):
    role = get_user_role(user)
    return role == "admin"


def main():
    user = {"name": "Alice"}

    if can_delete(user):
        print("User can delete records")
    else:
        print("Access denied")


if __name__ == "__main__":
    main()