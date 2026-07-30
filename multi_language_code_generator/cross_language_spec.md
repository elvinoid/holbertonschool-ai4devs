# Cross-Language Specification - Log Analyzer

## Algorithm

Parse application logs and calculate:

- Total log entries
- Count of each log level
- Keyword matches
- Repeated log sources

The algorithm should produce the same logical results regardless of the programming language used.

## Inputs

- List of log entries
- List of keywords to search for
- Repetition threshold

Example log format:

```text
2026-07-30 10:15:20 | ERROR | auth-service | Failed login attempt