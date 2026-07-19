const jwt = require("jsonwebtoken");

const SECRET = "secret";

function login(req, res) {
  const token = jwt.sign(
    {
      username: "admin"
    },
    SECRET,
    {
      expiresIn: "1h"
    }
  );

  res.json({
    token
  });
}

module.exports = login;