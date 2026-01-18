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

### Code quality / design issues

- There's only one potential design issue I've noticed that the filtering for non-cancelled orders could be a recurring task which would be best to separate it as a function of it's own not to write the same filtering logic multiple times across the codebase.

## 2) Proposed Fixes / Improvements

### Summary of changes

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

-

### Edge cases & risks

-

### Code quality / design issues

-

## 2) Proposed Fixes / Improvements

### Summary of changes

-

### Corrected code

See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation

-

### Rewritten explanation

-

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings

### Critical bugs

-

### Edge cases & risks

-

### Code quality / design issues

-

## 2) Proposed Fixes / Improvements

### Summary of changes

-

### Corrected code

See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations

If you were to test this function, what areas or scenarios would you focus on, and why?

## 3) Explanation Review & Rewrite

### AI-generated explanation (original)

> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation

-

### Rewritten explanation

-

## 4) Final Judgment

- Decision: Approve / Request Changes / Reject
- Justification:
- Confidence & unknowns:
