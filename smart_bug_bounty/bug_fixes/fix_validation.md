# Fix Validation

## bug1_fixed.py

- **Original Issue**: The average calculation divided the total by `len(numbers) - 1`, causing an off-by-one error.
- **Fix Applied**: Changed the divisor to `len(numbers)`.
- **Test Case 1**: `[10, 20, 30, 40]` → Expected `25` → **Passed**
- **Test Case 2**: `[5]` → Expected `5` → **Passed**
- **Test Case 3**: `[]` → Expected `0` → **Passed**
- **Test Results**: 3/3 test cases passed.

## bug2_fixed.js

- **Original Issue**: The loop used `i <= users.length`, which could access an invalid array position.
- **Fix Applied**: Changed the loop condition to `i < users.length`.
- **Test Case 1**: Find existing user `bob` → Expected Bob object → **Passed**
- **Test Case 2**: Find existing user `alice` → Expected Alice object → **Passed**
- **Test Case 3**: Search for nonexistent user → Expected `null` → **Passed**
- **Test Results**: 3/3 test cases passed.

## bug3_fixed.java

- **Original Issue**: The method returned `errors - 1`, producing an incorrect error count.
- **Fix Applied**: Changed the return statement to `return errors`.
- **Test Case 1**: Two ERROR entries → Expected `2` → **Passed**
- **Test Case 2**: No ERROR entries → Expected `0` → **Passed**
- **Test Case 3**: Null log array → Expected `0` → **Passed**
- **Test Results**: 3/3 test cases passed.

## bug4_fixed.py

- **Original Issue**: Users without a role were incorrectly assigned the `admin` role.
- **Fix Applied**: Changed the default role from `admin` to `guest`.
- **Test Case 1**: User without role → Expected `guest` → **Passed**
- **Test Case 2**: Admin user → Expected `admin` → **Passed**
- **Test Case 3**: Guest user attempting deletion → Expected `False` → **Passed**
- **Test Results**: 3/3 test cases passed.

## bug5_fixed.js

- **Original Issue**: A percentage discount was subtracted as a fixed monetary amount.
- **Fix Applied**: Calculated the discount using `total * discountPercent / 100`.
- **Test Case 1**: Total `40`, discount `10%` → Expected `36` → **Passed**
- **Test Case 2**: Total `40`, discount `0%` → Expected `40` → **Passed**
- **Test Case 3**: Total `40`, discount `25%` → Expected `30` → **Passed**
- **Test Results**: 3/3 test cases passed.

## bug6_fixed.java

- **Original Issue**: Unknown HTTP status codes incorrectly returned `OK`.
- **Fix Applied**: Changed the default case to return `Unknown Status`.
- **Test Case 1**: Status `200` → Expected `OK` → **Passed**
- **Test Case 2**: Status `404` → Expected `Not Found` → **Passed**
- **Test Case 3**: Status `403` → Expected `Unknown Status` → **Passed**
- **Test Results**: 3/3 test cases passed.

## Overall Validation

- **Total Fixed Files**: 6
- **Total Test Cases**: 18
- **Passed**: 18
- **Failed**: 0
- **Overall Result**: All fixes validated successfully.