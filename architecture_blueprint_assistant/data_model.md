# Data Model

The StudySync application stores information about users, study sessions, learning materials, assignments, and AI-generated quizzes. The following entities represent the core data model.

---

## User

Represents a student, teacher, or administrator using the system.

**Attributes**
- id (UUID)
- full_name (String)
- email (String)
- role (Student, Teacher, Administrator)

---

## Study Session

Represents a scheduled learning session created by a student.

**Attributes**
- id (UUID)
- user_id (UUID)
- title (String)
- start_time (DateTime)
- end_time (DateTime)
- status (Scheduled, Completed, Cancelled)

**Relationship**
- A user can create multiple study sessions.

---

## Study Material

Represents notes, documents, presentations, or other learning resources uploaded by users.

**Attributes**
- id (UUID)
- user_id (UUID)
- title (String)
- subject (String)
- file_url (String)

**Relationship**
- A user can upload multiple study materials.
- One study material can be used to generate multiple quizzes.

---

## Assignment

Represents coursework assigned by teachers or submitted by students.

**Attributes**
- id (UUID)
- user_id (UUID)
- title (String)
- due_date (Date)
- status (Assigned, Submitted, Graded)

**Relationship**
- A user can have multiple assignments.
- Assignments may reference study materials.

---

## Quiz

Represents AI-generated quizzes created from study materials.

**Attributes**
- id (UUID)
- material_id (UUID)
- title (String)
- question_count (Integer)

**Relationship**
- A study material can generate multiple quizzes.

---

## Entity Relationships

- One **User** can create many **Study Sessions**.
- One **User** can upload many **Study Materials**.
- One **User** can submit multiple **Assignments**.
- One **Study Material** can generate multiple **Quizzes**.
- An **Assignment** can reference a **Study Material**.