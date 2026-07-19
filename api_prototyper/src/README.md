# StudySync API

A minimal REST API prototype built with Express.js for the StudySync learning platform.

## Requirements

- Node.js 18+
- npm

## Installation

```bash
npm install
```

## Run the API

```bash
node index.js
```

The server will start on:

```
http://localhost:3000
```

## Available Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | API status |
| POST | /users | Create a user |
| GET | /users | Get all users |
| GET | /users/:id | Get a user by ID |
| PUT | /users/:id | Update a user |
| DELETE | /users/:id | Delete a user |

## Example Request

```http
POST /users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Example Response

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## Notes

- Data is stored in memory.
- The data will be lost when the server stops.
- This project demonstrates basic CRUD operations using Express.js.
