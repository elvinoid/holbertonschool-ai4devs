function findUser(users, username) {
    for (let i = 0; i <= users.length; i++) {
        if (users[i].username === username) {
            return users[i];
        }
    }

    return null;
}

function main() {
    const users = [
        { username: "alice", role: "admin" },
        { username: "bob", role: "user" }
    ];

    console.log(findUser(users, "bob"));
}

main();