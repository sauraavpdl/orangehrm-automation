# TC04 - Verify user can add a new employee with valid required fields

**Module:** PIM - Add Employee
**Priority:** High

## Preconditions
- User is logged in with valid credentials
- User has navigated to PIM > Add Employee

## Test Steps
1. Enter First Name "John"
2. Enter Last Name "Doe"
3. Leave Employee ID as auto-generated (or optionally edit it)
4. Leave "Create login details" toggle OFF
5. Click "Save"

## Expected Result
User is redirected to the employee's Personal Details page, with the page displaying the employee's full name ("John Doe") as the heading

## Test Data
- First Name: John
- Last Name: Doe