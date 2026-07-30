# Data Model

## Entity 1 - User

Stores information about users.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique user ID |
| name | String | User name |
| email | String | User email |

## Entity 2 - Project

Stores information about code projects.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique project ID |
| name | String | Project name |
| language | String | Main programming language |
| user_id | Integer | Project owner |

## Entity 3 - Analysis

Stores AI analysis results for a project.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique analysis ID |
| project_id | Integer | Related project |
| explanation | Text | AI-generated explanation |
| created_at | DateTime | Analysis date |

## Entity 4 - Issue

Stores bugs and risks found during analysis.

| Field | Type | Description |
|---|---|---|
| id | Integer | Unique issue ID |
| analysis_id | Integer | Related analysis |
| type | String | Bug or Risk |
| description | Text | Issue description |
| severity | String | Low, Medium, or High |
| suggested_fix | Text | Suggested solution |

## Relationships

- One User can have many Projects.
- One Project can have many Analyses.
- One Analysis can have many Issues.
- Each Issue belongs to one Analysis.