const express = require("express");

const app = express();
const PORT = 3000;

app.use(express.json());

let users = [];

// Root endpoint
app.get("/", (req, res) => {
  res.json({ message: "StudySync API is running" });
});

// CREATE
app.post("/users", (req, res) => {
  const user = {
    id: users.length + 1,
    ...req.body
  };

  users.push(user);
  res.status(201).json(user);
});

// READ ALL
app.get("/users", (req, res) => {
  res.json(users);
});

// READ ONE
app.get("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);

  const user = users.find(u => u.id === id);

  if (!user) {
    return res.status(404).json({ message: "User not found" });
  }

  res.json(user);
});

// UPDATE
app.put("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);

  const index = users.findIndex(u => u.id === id);

  if (index === -1) {
    return res.status(404).json({ message: "User not found" });
  }

  users[index] = {
    id,
    ...req.body
  };

  res.json(users[index]);
});

// DELETE
app.delete("/users/:id", (req, res) => {
  const id = parseInt(req.params.id);

  const index = users.findIndex(u => u.id === id);

  if (index === -1) {
    return res.status(404).json({ message: "User not found" });
  }

  users.splice(index, 1);

  res.json({ message: "User deleted successfully" });
});

app.listen(PORT, () => {
  console.log(`StudySync API running on http://localhost:${PORT}`);
});