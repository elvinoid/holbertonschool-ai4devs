# AI Debug Log

This document records AI-assisted analysis of each intentionally buggy code
snippet. Each analysis identifies the issue, explains why it occurs, and
provides a suggested fix.

## bug1.py

**AI Explanation**:  
The `calculate_average()` function divides the total by
`len(numbers) - 1`. This is an off-by-one error. The average of a list must
be calculated by dividing the sum of all values by the actual number of
values. For example, `[10, 20, 30, 40]` has four values, so the divisor must
be `4`, not `3`.

**Suggested Fix**:
```python
return total / len(numbers)