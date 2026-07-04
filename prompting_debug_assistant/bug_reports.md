# Bug Reports

## Bug Report – bug1.py
- **File Name**: bug1.py
- **Summary**: The program failed to execute due to a syntax error in a conditional statement.
- **Root Cause**: The `if` statement was missing a colon (`:`), preventing the Python interpreter from parsing the code.
- **Resolution**: The AI suggested adding the missing colon. I applied the change and verified that the program executed correctly and returned the expected average.
- **Lesson Learned**: Carefully review syntax when writing conditional statements, as small syntax errors can prevent a program from running.

---

## Bug Report – bug2.js
- **File Name**: bug2.js
- **Summary**: The program incorrectly identified odd numbers as even.
- **Root Cause**: The parity check used `number % 2 === 1`, which returns `true` for odd numbers instead of even numbers.
- **Resolution**: The AI suggested changing the condition to `number % 2 === 0`. I updated the function and verified that only even numbers were printed.
- **Lesson Learned**: Verify program logic with multiple test cases to ensure conditions produce the expected results.

---

## Bug Report – bug3.java
- **File Name**: bug3.java
- **Summary**: The application terminated with an `ArithmeticException` during execution.
- **Root Cause**: The program attempted to divide integers by zero.
- **Resolution**: The AI suggested using a non-zero divisor or checking the divisor before division. I changed the divisor to a non-zero value and confirmed the program executed successfully.
- **Lesson Learned**: Validate input values before performing arithmetic operations that can cause runtime exceptions.

---

## Bug Report – bug4.py
- **File Name**: bug4.py
- **Summary**: The program raised an `IndexError` while iterating through a list.
- **Root Cause**: The loop iterated one position beyond the last valid index by using `range(len(items) + 1)`.
- **Resolution**: The AI suggested changing the loop to `range(len(items))`. I applied the fix and confirmed that every item was printed exactly once.
- **Lesson Learned**: Pay close attention to loop boundaries to avoid off-by-one errors.

---

## Bug Report – bug5.js
- **File Name**: bug5.js
- **Summary**: The program produced an incorrect shopping cart total.
- **Root Cause**: One array element was stored as a string, causing JavaScript to concatenate strings instead of performing numeric addition.
- **Resolution**: The AI suggested converting each value using `Number(item)` before adding it to the total. I tested the change and verified the correct numeric total.
- **Lesson Learned**: Ensure data types are consistent before performing calculations, especially in dynamically typed languages.

---

## Bug Report – bug6.java
- **File Name**: bug6.java
- **Summary**: The program failed to parse a date string and threw a `DateTimeParseException`.
- **Root Cause**: `LocalDate.parse()` expects dates in ISO-8601 (`yyyy-MM-dd`) format, but the input used `dd/MM/yyyy`.
- **Resolution**: The AI suggested using a `DateTimeFormatter` with the correct pattern. I implemented the formatter and verified that the date was parsed successfully.
- **Lesson Learned**: Always verify the expected input format when using parsing APIs and other library methods.