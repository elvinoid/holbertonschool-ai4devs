# Bug Descriptions

This document describes the intended behavior and known defect in each
intentionally flawed code snippet.

## bug1.py

- **Language**: Python
- **Category**: Arithmetic / off-by-one
- **Intended Behavior**: Calculate the arithmetic mean of all values in the input list.
- **Current Issue**: The total is divided by `len(numbers) - 1` instead of `len(numbers)`.
- **Example**: `[10, 20, 30, 40]` should produce `25`, but the current implementation produces an incorrect result.
- **Expected Fix**: Divide the total by the number of elements.

## bug2.js

- **Language**: JavaScript
- **Category**: Array boundary / runtime error
- **Intended Behavior**: Search the array and return the user with the requested username.
- **Current Issue**: The loop uses `i <= users.length` instead of `i < users.length`.
- **Potential Impact**: The code can access an undefined array element and attempt to read its `username` property.
- **Expected Fix**: Change the loop condition to `i < users.length`.

## bug3.java

- **Language**: Java
- **Category**: Incorrect calculation
- **Intended Behavior**: Return the number of log entries containing `ERROR`.
- **Current Issue**: The method subtracts one from the calculated error count.
- **Example**: Two ERROR entries should return `2`, but the method returns `1`.
- **Expected Fix**: Return `errors` directly.

## bug4.py

- **Language**: Python
- **Category**: Authorization / incorrect default
- **Intended Behavior**: Users without an explicitly assigned role should be treated as guests.
- **Current Issue**: Missing roles incorrectly default to `admin`.
- **Potential Impact**: An unprivileged user could incorrectly receive administrative permissions.
- **Expected Fix**: Change the default role from `admin` to `guest`.

## bug5.js

- **Language**: JavaScript
- **Category**: Percentage calculation
- **Intended Behavior**: Apply a percentage discount to the calculated order total.
- **Current Issue**: The discount percentage is subtracted as a fixed monetary amount.
- **Example**: A `$40` total with a `10%` discount should become `$36`, not `$30`.
- **Expected Fix**: Calculate the discount using `total * discountPercent / 100`.

## bug6.java

- **Language**: Java
- **Category**: Incorrect default case
- **Intended Behavior**: Return an appropriate description for known HTTP status codes and indicate that an unknown status is unsupported.
- **Current Issue**: Unknown status codes incorrectly return `OK`.
- **Example**: Status `403` should not return `OK`.
- **Potential Impact**: Incorrect status reporting can cause incorrect application behavior and misleading diagnostics.
- **Expected Fix**: Return an explicit `Unknown Status` or similar value in the default case.