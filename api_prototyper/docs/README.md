# StudySync API Documentation

## Base URL

```
http://localhost:3000
```

## Endpoints

### GET /

Returns API status.

### POST /users

Creates a new user.

### GET /users

Returns all users.

### GET /users/:id

Returns a single user.

### PUT /users/:id

Updates a user.

### DELETE /users/:id

Deletes a user.

## Authentication

Authentication is not implemented in this prototype.

## Response Format

All responses are returned in JSON format.

## Testing

The API can be tested using the included Postman collection located in:

```
tests/postman_collection.json
```