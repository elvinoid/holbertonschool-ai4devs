graph TD

A[Web Application]
B[Mobile Application]

A --> C[API Gateway]
B --> C

C --> D[Authentication Service]
C --> E[Study Management Service]
C --> F[AI Learning Service]
C --> G[Notification Service]

D --> H[(User Database)]
E --> I[(Study Database)]
F --> J[AI Model]
G --> K[Email / Push Notification Service]