# Fix Validation

## bug1_fixed.py

**Fixed File**: `bug1_fixed.py`

**Original Problem**: The average function divided the sum by `len(numbers) - 1`.

**Actual Fix**: The fixed implementation now returns `total / len(numbers)`.

**Test 1**: Input `[10, 20, 30, 40]` produced `25`. **Passed.**

**Test 2**: Input `[5]` produced `5`. **Passed.**

**Test 3**: Input `[]` produced `0`. **Passed.**

**Validation Result**: 3/3 tests passed.

---

## bug2_fixed.js

**Fixed File**: `bug2_fixed.js`

**Original Problem**: The user-search loop could access an invalid array index because it used `i <= users.length`.

**Actual Fix**: The fixed implementation now uses `i < users.length`, so the loop only accesses valid array indexes.

**Test 1**: Searching for `bob` returned the Bob user object. **Passed.**

**Test 2**: Searching for `alice` returned the Alice user object. **Passed.**

**Test 3**: Searching for a nonexistent username returned `null`. **Passed.**

**Validation Result**: 3/3 tests passed.

---

## bug3_fixed.java

**Fixed File**: `bug3_fixed.java`

**Original Problem**: The original implementation returned one less than the actual number of ERROR entries.

**Actual Fix**: The fixed implementation increments `errors` for every non-null log containing `ERROR` and returns `errors` directly.

**Test 1**: Two ERROR log entries returned `2`. **Passed.**

**Test 2**: Logs containing no ERROR entries returned `0`. **Passed.**

**Test 3**: A null log array returned `0`. **Passed.**

**Validation Result**: 3/3 tests passed.

---

## bug4_fixed.py

**Fixed File**: `bug4_fixed.py`

**Original Problem**: A user without an assigned role could incorrectly receive administrative privileges.

**Actual Fix**: The fixed implementation returns `guest` when the user is `None` or when the user has no role. Only a user whose role is explicitly `admin` can pass the `can_delete()` check.

**Test 1**: User with no role returned `guest`. **Passed.**

**Test 2**: User with role `admin` returned `admin`. **Passed.**

**Test 3**: A user without a role could not delete records because `can_delete()` returned `False`. **Passed.**

**Validation Result**: 3/3 tests passed.

---

## bug5_fixed.js

**Fixed File**: `bug5_fixed.js`

**Original Problem**: The original implementation treated `discountPercent` as a fixed amount instead of a percentage.

**Actual Fix**: The fixed implementation calculates the discount using `total * discountPercent / 100` and subtracts that amount from the total.

**Test 1**: Items totaling `40` with a `10%` discount produced `36`. **Passed.**

**Test 2**: Items totaling `40` with a `0%` discount produced `40`. **Passed.**

**Test 3**: Items totaling `40` with a `25%` discount produced `30`. **Passed.**

**Validation Result**: 3/3 tests passed.

---

## bug6_fixed.java

**Fixed File**: `bug6_fixed.java`

**Original Problem**: Unknown HTTP status codes were incorrectly reported as `OK`.

**Actual Fix**: The fixed implementation returns `Unknown Status` for status codes that are not explicitly handled by the switch statement.

**Test 1**: Status code `200` returned `OK`. **Passed.**

**Test 2**: Status code `404` returned `Not Found`. **Passed.**

**Test 3**: Status code `403` returned `Unknown Status`. **Passed.**

**Validation Result**: 3/3 tests passed.

---

## Overall Validation

**Fixed Files**: 6

**Total Tests**: 18

**Passed**: 18

**Failed**: 0

**Overall Result**: All six fixed implementations were validated against their intended corrected behavior.