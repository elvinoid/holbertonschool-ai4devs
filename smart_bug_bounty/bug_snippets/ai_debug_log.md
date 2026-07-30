# AI Debug Log

This document contains AI-assisted analysis of all intentionally buggy
snippets. Each section explains the defect, its cause, the recommended fix,
and the confidence level of the analysis.

## bug1.py

**AI Explanation**:  
The `calculate_average()` function divides the total by `len(numbers) - 1`,
which is an off-by-one error. The average must be calculated by dividing the
sum of all numbers by the actual number of elements in the list.

For example, `[10, 20, 30, 40]` contains four values, so the divisor must be
`4`, not `3`. The current implementation therefore produces an incorrect
average.

**Suggested Fix**:

```python
return total / len(numbers)