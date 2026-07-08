# Technical Specification

## System Components

### 1. Authentication Service
Responsible for user registration, login, authentication, and authorization.

**Responsibilities:**
- User registration
- User login
- Password reset
- JWT token generation
- Role-based access control (Student, Teacher, Administrator)

---

### 2. Study Management Service
Manages study schedules, notes, assignments, and learning materials.

**Responsibilities:**
- Create and manage study schedules
- Upload study materials
- Store notes
- Manage assignments
- Calendar integration

---

### 3. AI Learning Service
Provides AI-powered learning assistance.

**Responsibilities:**
- Generate summaries
- Generate quizzes
- Generate flashcards
- Recommend study plans

---

### 4. Notification Service

Responsible for sending reminders and notifications.

**Responsibilities:**
- Study reminders
- Assignment deadlines
- Quiz notifications
- Email and push notifications

---

## Data Models

### User

| Field | Type |
|--------|------|
| id | UUID |
| full_name | String |
| email | String |
| password_hash | String |
| role | Student \| Teacher \| Admin |
| created_at | DateTime |

---

### StudyMaterial

| Field | Type |
|--------|------|
| id | UUID |
| title | String |
| file_url | String |
| uploaded_by | UUID |
| subject | String |
| created_at | DateTime |

---

### StudySession

| Field | Type |
|--------|------|
| id | UUID |
| user_id | UUID |
| title | String |
| start_time | DateTime |
| end_time | DateTime |
| status | Scheduled \| Completed |

---

## API Endpoints

### Register User

**POST** `/api/auth/register`

Parameters

```json
{
  "full_name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

---

### Login

**POST** `/api/auth/login`

Parameters

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

---

### Upload Study Material

**POST** `/api/materials/upload`

Parameters

- Authorization Token
- File
- Title
- Subject

---

### Generate AI Summary

**POST** `/api/ai/summarize`

Parameters

```json
{
  "material_id": "uuid"
}
```

---

### Generate Quiz

**POST** `/api/ai/quiz`

Parameters

```json
{
  "material_id": "uuid",
  "question_count": 10
}
```

---

### Create Study Session

**POST** `/api/study-sessions`

Parameters

```json
{
  "title": "Math Revision",
  "start_time": "2026-07-09T18:00:00",
  "end_time": "2026-07-09T19:00:00"
}
```

---

### Get Dashboard

**GET** `/api/dashboard`

Parameters

- Authorization Token

Returns

- Upcoming study sessions
- Recent materials
- Quiz statistics
- Progress summary