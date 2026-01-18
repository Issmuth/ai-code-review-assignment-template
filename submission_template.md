# AI Code Review Assignment (Python)

## Candidate

- Name: <strong>Ismael Muzemil</strong>
- Approximate time spent:

---

# Task 1 — Average Order Value

## 1) Code Review Findings

### Critical bugs

- The average order calculation was incorrect, the code doesnt take the cancelled orders into account for the denominator, since it's just taking the entire lists length as the count.

### Edge cases & risks

- Code can experience Zero Division Error under two circumstances:
  1. The order list is empty hence `count` isn't incremented
  2. All the order items in the list are cancelled.
- Malformed order objects can result in Key Error or Type Error under three circumstances:
  1. A key is missing (e.g. no "status" key)
  2. The object is None
  3. the `amount` field is a non-numeric type like a string or even None
  4. `orders` isn't an iterable.

### Code quality / design issues

- There's only one potential design issue I've noticed that the filtering for non-cancelled orders could be a recurring task which would be best to separate it as a function of it's own not to write the same filtering logic multiple times across the codebase.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Added type check for `orders`
- Count is now calculated witin the filtering logic
- Check if order is not `None` before trying to access the content
- Changed index based access with the get method on the order object with default value for the `amount` field.
- Added type validation before incrementation of the `total`
- Added checks to avoid zero division error for all edge cases

### Corrected code

See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

### Testing Considerations

## 3) Explanation Review & Rewrite

I would focus on testing different edge cases of malformed or enexpected values for the order dictionary, this can help simulate how the function fares against real data recieved that might be parsed json, csv or even API responses that tend to be messy.

### AI-generated explanation (original)

> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation

- Aside from being factually incorrect the explanation seems to be reflecting the bug it had originally created, and doesn't explicitly state that it divides by the number of total non-cancelled orders.

### Rewritten explanation

- This function calculates average order value by summing the amounts of all valid non-cancelled orders and dividing by the number of non-cancelled orders. It correctly excludes cancelled and invalid orders from the calculation.

## 4) Final Judgment

- Decision: Request Changes
- Justification:
  > The original code has fatal errors without any proper handling that could result in the function crashing the entire app, further more the logical error that doesn't account for cancelled orders in the `count` could potentially result in an incorrect/misleading results.
- Confidence & unknowns:
  > The corrected code ensures the function doesn't have any fatal bugs that can crash the system. Moreover, error handling wasn't applied in the corrected as there wasn't sufficient context to know it was required.

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings

### Critical bugs

- The validation check skips multiple steps that make an email valid, the mere existence of the '@' isn't a sufficient verification the the email is valid.

### Edge cases & risks

- The code's logic fails in the following cases:
  1. multiple `@`s
  2. a string with just `@` and nothing else
  3. No `.` for domain validity
  4. Simply put any incorrect arrangement of the `@` and `.` sybmols e.g. `com.ismael@eskalate`
  5. invalid characters like ` / , < , ~` can still be counted as valid emails
  6. the email string exceeds 255 characters
- The app could crash with TypeError in the following cases:
  1. `emails` is None or note an iterable
  2. if an element in the list in not a String.

### Code quality / design issues

- Similarl to the first task separation of concerns would be great here as well, separating the validation logic from the counting logic would be more efficient since we're bound to validate emails again in other scenarios than just counting.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Added type guard for the emails list
- Added regex pattern for cleaner validation
- added string type and character count checks before regex matching

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

Aside from testing the the edge cases stated above I would perform a stress test in accordance to the volumne that we typically work with to ensure performance doesn't drop.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

- No issue besides the factual incorrectness between the intention and actual implementation.

### Rewritten explanation

- This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

## 4) Final Judgment

- Decision: Request Changes
- Justification:
  > The original code is a highly flawed and ineffective implementation, it overlooks multiple edge cases and scenarios which creates openings that can lead to wrong output or crash the entire app.
- Confidence & unknowns: The new implementation follows standard guidelines for email validation in a typical user setting.

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

- Along with some incorrect assumptions that can crash the system, it has the same bug as task number one, which didn't account for the ignored values in the denominator `count`.

### Edge cases & risks

- Code can experience Zero Division Error under two circumstances:
  1. The values list is empty hence `count` isn't incremented
  2. All the values items in the list are invalid. (after correction)
- The value of V can result in Value Error or Type Error under the following circumstances:
  1. `v` in `values` can not be converted to float
  2. `values` isn't an iterable.

### Code quality / design issues

- Similar to the first two tasks, separation of concerns would be useful here as well.

## 2) Proposed Fixes / Improvements

### Summary of changes

- Added type check for `values`
- count is now calculated dynamically as we filter for valid measurement values
- added try-catch block to ignore invalid measurements more rigirousely
- Avoided zero division error by adding checks on count

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

Similary I would go all out in testing with unconventional edge cases since the function make multiple assumptions about the incoming data.

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

- After correcting the code the explanation can work, to actually safely handle mixed inputs the explanation works, however the inital code didn't handle mixed input `safely`, as the app could have a fatal error for values that couldn't be converted to float.

### Rewritten explanation

- This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

## 4) Final Judgment

- Decision: Request Changes
- Justification:
  The initial code made multiple assumptions that highly critical and could result in flawed result or system failures in inprecedented ways. Which is why the correction was necessary.
- Confidence & unknowns: After tests with some edge cases it is clear the original code was flawed, yet the new correction has resoled these flaws. Unknowns for this include whether the values could be negative as I couldn't surely assume nature of the measurments.
