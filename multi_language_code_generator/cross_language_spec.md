# Cross-Language Specification - Log Analyzer

## Algorithm

Parse application logs and calculate total entries, log-level counts, keyword matches, and repeated sources.

## Input Format

Input contains:
- `logs`: list of log strings
- `keywords`: list of search keywords
- `threshold`: minimum source occurrence count

Log format:
`YYYY-MM-DD HH:MM:SS | LEVEL | SOURCE | MESSAGE`

Example:
`2026-07-30 10:15:20 | ERROR | auth | Failed login`

## Output Format

Return:
- `total_entries`: number of valid entries
- `level_counts`: count for each log level
- `keyword_matches`: count for each keyword
- `repeated_sources`: sources occurring at least `threshold` times

Example:
`{"total_entries": 2, "level_counts": {"ERROR": 2}, "keyword_matches": {"failed": 2}, "repeated_sources": ["auth"]}`

## Edge Cases

- Empty logs
- Empty keywords
- Malformed entries
- Unknown log levels
- Duplicate entries
- Multiple keywords
- Case-insensitive keywords
- Threshold of 1
- Threshold larger than log count

Malformed entries must be skipped without stopping the analysis.

## Test Cases

### Test 1 - Normal
Input: 3 valid logs, 2 ERROR and 1 INFO.
Expected: `total_entries = 3`, `ERROR = 2`, `INFO = 1`.

### Test 2 - Empty
Input: `logs = []`.
Expected: `total_entries = 0`.

### Test 3 - Keyword
Input: 2 logs containing `Failed`, keyword = `failed`.
Expected: `failed = 2`.

### Test 4 - Malformed
Input: 1 valid log and 1 malformed log.
Expected: `total_entries = 1`, malformed log skipped.

### Test 5 - Repeated Source
Input: 3 logs from `auth`, threshold = 2.
Expected: `repeated_sources = ["auth"]`.

### Test 6 - Multiple Keywords
Input: message contains `failed` and `timeout`.
Expected: both keywords have count `1`.

## Cross-Language Requirements

Python, JavaScript, Java, C++, and other implementations must produce equivalent results for identical inputs.

Required behavior:
- Same input format
- Same output format
- Case-insensitive keyword matching
- Malformed entries skipped
- Same threshold behavior