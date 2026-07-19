const express = require("express");
const app = express();

app.use(express.json());

let users = [];

app.post("/users", (req, res) => {
  const { name, email } = req.body;

  if (!name || !email) {
    return res.status(400).json({
      message: "Name and email are required"
    });
  }

  const user = {
    id: users.length + 1,
    name,
    email
  };

  users.push(user);

  res.status(201).json(user);
});

module.exports = app;