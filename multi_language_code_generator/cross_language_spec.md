# Cross-Language Specification - Log Analyzer

## Algorithm

Parse application logs and calculate:

- Total number of valid log entries
- Number of entries for each log level
- Number of keyword matches
- Sources that appear repeatedly

The algorithm must produce equivalent results when implemented in different programming languages.

## Input Format

The algorithm accepts:

- `logs`: A list of log entries
- `keywords`: A list of keywords
- `threshold`: Minimum number of occurrences required for a source to be considered repeated

Each log entry follows this format:

```text
YYYY-MM-DD HH:MM:SS | LEVEL | SOURCE | MESSAGE