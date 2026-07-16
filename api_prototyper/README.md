# StudySync API

A simple REST API prototype built with Express.js for the StudySync learning platform.

## Requirements

- Node.js 18+
- npm

## Installation

```bash
cd src
npm install
```

## Run the API

```bash
npm start
```

The server starts on:

```
http://localhost:3000
```

## Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API status |
| POST | /users | Create a user |
| GET | /users | List all users |
| GET | /users/:id | Get user by ID |
| PUT | /users/:id | Update a user |
| DELETE | /users/:id | Delete a user |

## Example Request

Create a user:

```http
POST /users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}
```

Example response:

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Notes

- Data is stored in memory and is not persisted after the server stops.
- This project demonstrates basic CRUD functionality using Express.js.