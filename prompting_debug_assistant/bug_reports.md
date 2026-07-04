# Bug Reports

## Bug Report – bug1.py
- **Summary**: The program failed to execute due to a syntax error in a conditional statement.
- **Root Cause**: The `if` statement was missing a colon (`:`), preventing the Python interpreter from parsing the code.
- **Resolution**: The AI suggested adding the missing colon. After applying this change, the program executed correctly and returned the expected average.
- **Lesson Learned**: Carefully review syntax when writing conditional statements, as small syntax errors can prevent a program from running.

---

## Bug Report – bug2.js
- **Summary**: The program incorrectly identified odd numbers as even.
- **Root Cause**: The parity check used `number % 2 === 1`, which evaluates to `true` for odd numbers rather than even numbers.
- **Resolution**: The AI suggested changing the condition to `number % 2 === 0`. The function was also simplified by directly returning the Boolean expression.
- **Lesson Learned**: Verify program logic with multiple test cases to ensure conditions produce the expected results.

---

## Bug Report – bug3.java
- **Summary**: The application terminated with an `ArithmeticException` during execution.
- **Root Cause**: The program attempted to divide integers by zero.
- **Resolution**: The AI suggested using a non-zero divisor or validating the divisor before performing the division. The implemented fix changed the divisor to a valid non-zero value.
- **Lesson Learned**: Validate input values before performing arithmetic operations that can cause runtime exceptions.

---

## Bug Report – bug4.py
- **Summary**: The program raised an `IndexError` while iterating through a list.
- **Root Cause**: The loop iterated one position beyond the last valid list index by using `range(len(items) + 1)`.
- **Resolution**: The AI suggested changing the loop to `range(len(items))`. This corrected the iteration and prevented the exception.
- **Lesson Learned**: Pay close attention to loop boundaries to avoid off-by-one errors.

---

## Bug Report – bug5.js
- **Summary**: The program produced an incorrect shopping cart total.
- **Root Cause**: One element in the array was stored as a string, causing JavaScript to perform string concatenation instead of numeric addition.
- **Resolution**: The AI suggested converting each value to a number using `Number(item)` before adding it to the total. This produced the correct numeric result.
- **Lesson Learned**: Ensure data types are consistent before performing calculations, especially in dynamically typed languages.

---

## Bug Report – bug6.java
- **Summary**: The program failed to parse a date string and threw a `DateTimeParseException`.
- **Root Cause**: `LocalDate.parse()` expects dates in ISO-8601 format (`yyyy-MM-dd`), while the input string used the format `dd/MM/yyyy`.
- **Resolution**: The AI suggested using a `DateTimeFormatter` configured with the appropriate date pattern. After applying the formatter, the date was parsed successfully.
- **Lesson Learned**: Always verify the expected input format when using library methods, particularly for parsing dates and structured data.