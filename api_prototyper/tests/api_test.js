const request = require("supertest");
const express = require("express");

const app = express();
app.use(express.json());

let users = [];

app.get("/", (req, res) => {
  res.status(200).json({ message: "StudySync API is running" });
});

app.post("/users", (req, res) => {
  const user = {
    id: users.length + 1,
    name: req.body.name,
    email: req.body.email
  };

  users.push(user);
  res.status(201).json(user);
});

app.get("/users", (req, res) => {
  res.status(200).json(users);
});

app.get("/users/:id", (req, res) => {
  const user = users.find(u => u.id == req.params.id);

  if (!user) {
    return res.status(404).json({
      message: "User not found"
    });
  }

  res.json(user);
});

app.put("/users/:id", (req, res) => {
  const user = users.find(u => u.id == req.params.id);

  if (!user) {
    return res.status(404).json({
      message: "User not found"
    });
  }

  user.name = req.body.name;
  user.email = req.body.email;

  res.json(user);
});

app.delete("/users/:id", (req, res) => {
  users = users.filter(u => u.id != req.params.id);

  res.json({
    message: "User deleted successfully"
  });
});

describe("StudySync API", () => {

  test("GET /", async () => {
    const res = await request(app).get("/");
    expect(res.statusCode).toBe(200);
  });

  test("POST /users", async () => {
    const res = await request(app)
      .post("/users")
      .send({
        name: "John",
        email: "john@example.com"
      });

    expect(res.statusCode).toBe(201);
  });

  test("GET /users", async () => {
    const res = await request(app).get("/users");
    expect(res.statusCode).toBe(200);
  });

  test("GET /users/1", async () => {
    const res = await request(app).get("/users/1");
    expect(res.statusCode).toBe(200);
  });

  test("DELETE /users/1", async () => {
    const res = await request(app).delete("/users/1");
    expect(res.statusCode).toBe(200);
  });

});