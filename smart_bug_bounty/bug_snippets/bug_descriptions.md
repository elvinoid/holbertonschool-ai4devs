# Bug Descriptions

## bug1.py

- **Language**: Python
- **Intended Behavior**: Calculate and return the arithmetic average of all numbers in a list.
- **Current Issue**: The function divides the total by `len(numbers) - 1` instead of `len(numbers)`.
- **Example**: `[10, 20, 30]` should return `20`, but the buggy implementation returns `30`.

## bug2.js

- **Language**: JavaScript
- **Intended Behavior**: Find and return a user whose username matches the requested username.
- **Current Issue**: The loop uses `i <= users.length` instead of `i < users.length`.
- **Potential Impact**: When the loop reaches the array length, `users[i]` is undefined and accessing `.username` can cause a runtime error.

## bug3.java

- **Language**: Java
- **Intended Behavior**: Count all log entries containing `ERROR` or `error`.
- **Current Issue**: The method subtracts 1 from the final error count.
- **Example**: Two ERROR entries should return `2`, but the implementation returns `1`.

## bug4.py

- **Language**: Python
- **Intended Behavior**: Return the user's role and default to `guest` when no role is specified.
- **Current Issue**: Users without a role are incorrectly assigned the `admin` role.
- **Potential Impact**: This can result in unauthorized administrative privileges.

## bug5.js

- **Language**: JavaScript
- **Intended Behavior**: Calculate the total price and apply a percentage discount.
- **Current Issue**: The discount value is subtracted directly from the total instead of being interpreted as a percentage.
- **Example**: A total of `$40` with a `10%` discount should become `$36`, but the buggy code returns `$30`.