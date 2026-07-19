# AI Coding Benchmark Tasks

## Task 1 – Create User CRUD Endpoint

**Estimated Time:** 15–20 minutes

### Requirements
Implement a `POST /users` endpoint using Express.js that creates a new user.

### Inputs
JSON request body:
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```

### Outputs
- Return the created user with a generated ID.
- HTTP Status: `201 Created`

### Acceptance Criteria
- Validates that `name` and `email` are provided.
- Returns `201` for successful creation.
- Returns `400` for invalid or missing input.
- Response is JSON.

---

## Task 2 – Update Existing User

**Estimated Time:** 15–25 minutes

### Requirements
Implement a `PUT /users/:id` endpoint to update an existing user's information.

### Inputs
- URL parameter: `id`
- JSON body:
```json
{
  "name": "Jane Doe",
  "email": "jane@example.com"
}
```

### Outputs
- Updated user object.
- HTTP Status: `200 OK`

### Acceptance Criteria
- Updates only an existing user.
- Returns `404` if the user does not exist.
- Returns the updated user as JSON.
- Preserves the user's ID.

---

## Task 3 – Retrieve Users with Pagination

**Estimated Time:** 20–30 minutes

### Requirements
Implement a `GET /users` endpoint supporting pagination.

### Inputs
Query parameters:
- `page`
- `limit`

Example:
```
GET /users?page=1&limit=10
```

### Outputs
JSON response:
```json
{
  "page": 1,
  "limit": 10,
  "total": 25,
  "items": []
}
```

### Acceptance Criteria
- Supports `page` and `limit` parameters.
- Returns paginated results.
- Returns `200 OK`.
- Response is valid JSON with `page`, `limit`, `total`, and `items`.