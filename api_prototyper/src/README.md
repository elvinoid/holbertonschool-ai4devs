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

The server starts on:

http://localhost:3000

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | API status |
| POST | /users | Create user |
| GET | /users | List users |
| GET | /users/:id | Get user |
| PUT | /users/:id | Update user |
| DELETE | /users/:id | Delete user |

## Notes

- Data is stored in memory.
- Data is not persisted after the server stops.
- Demonstrates basic CRUD operations with Express.js.
