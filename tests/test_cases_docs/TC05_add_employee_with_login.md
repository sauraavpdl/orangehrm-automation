# TC05 - Verify user can add an employee with profile photo and login details

**Module:** PIM - Add Employee
**Priority:** Medium

## Preconditions
- User is logged in with valid credentials
- User has navigated to PIM > Add Employee

## Test Steps
1. Enter First Name and Last Name
2. Upload a profile photo
3. Toggle "Create login details" ON
4. Enter Username
5. Enter Password and Confirm Password
6. Set Status to "Enabled"
7. Click "Save"

## Expected Result
Employee is created successfully with the uploaded photo and login credentials, and user is redirected to the employee's Personal Details page

## Test Data
- First Name: Jane
- Last Name: Smith
- Username: jane.smith
- Password: Test@1234