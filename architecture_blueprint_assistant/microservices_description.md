# Microservices Architecture

The StudySync application is designed using a microservices architecture in which each business capability is implemented as an independent service. Services communicate through APIs, allowing them to be developed, deployed, and scaled independently. Each service maintains its own database to improve scalability, reliability, and data isolation.

## Services

- **API Gateway**
  - Serves as the single entry point for all client requests. It routes requests to the appropriate microservice, performs request validation, and can enforce authentication and rate limiting.

- **Authentication Service**
  - Manages user registration, login, password management, authentication, authorization, and JWT token generation. Stores authentication data in the Auth Database.

- **User Service**
  - Maintains user profiles, account settings, user roles, and permissions. Stores user information in the User Database.

- **Study Management Service**
  - Handles study schedules, study sessions, notes, and learning materials. Stores educational content in the Study Database.

- **AI Learning Service**
  - Generates AI-powered summaries, quizzes, flashcards, and personalized study recommendations. Operates independently and stores AI-related data in the AI Database.

- **Assignment Service**
  - Manages assignment creation, submission, grading, and assignment status. Stores assignment information in the Assignment Database.

- **Notification Service**
  - Sends email and push notifications for study reminders, assignments, announcements, and other important events. Stores notification history in the Notification Database.

- **Analytics Service**
  - Collects application metrics, tracks learning progress, generates reports, and provides usage analytics for teachers and administrators. Stores analytical data in the Analytics Database.

## Service Interactions

- The **Web & Mobile Client** sends all requests through the **API Gateway**.
- The **API Gateway** routes requests to the appropriate microservice.
- The **Authentication Service** validates user identity before protected services are accessed.
- The **Study Management Service** can request summaries or quizzes from the **AI Learning Service**.
- The **Assignment Service** can trigger the **Notification Service** to remind students about deadlines.
- The **Analytics Service** receives activity data from the other services to generate reports and dashboards.
- Each microservice manages its own dedicated database to ensure loose coupling and independent scalability.