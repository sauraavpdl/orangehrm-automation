# TC08 - Verify user can delete an existing employee successfully

# Module: PIM - Employee List / Delete Employee Priority: High

## Preconditions
1. User is logged in with valid credentials
2. User has navigated to PIM > Employee List
3. At least one employee exists in the system to delete

# Test Steps
1. Search for the target employee by first and last name (optional, to narrow the list)
2. Locate the target employee's row in the Employee List table
3. Click the "Delete" (trash) icon in that row
4. In the confirmation dialog, click "Yes, Delete"

## Expected Result
Employee is removed from the Employee List table, and a toast message with the text "Successfully Deleted" is displayed

## Test Data
First Name: John1
Last Name: Doe