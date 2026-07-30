# Data Model - AI Code Modernization Assistant

## Entity 1 - User

Stores information about users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique user ID |
| name | String | User name |
| email | String | User email |

## Entity 2 - Project

Stores code projects being analyzed.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique project ID |
| name | String | Project name |
| language | String | Programming language |
| user_id | Integer | Project owner |

## Entity 3 - Analysis

Stores AI analysis results.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique analysis ID |
| project_id | Integer | Related project |
| explanation | Text | AI explanation |
| created_at | DateTime | Analysis date |

## Entity 4 - Bug

Stores bugs found during analysis.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique bug ID |
| analysis_id | Integer | Related analysis |
| description | Text | Bug description |
| severity | String | Low, Medium, or High |
| suggested_fix | Text | Suggested solution |

## Relationships

- One User can have many Projects.
- One Project can have many Analyses.
- One Analysis can have many Bugs.
- Each Bug belongs to one Analysis.