# TC02 - Verify user cannot log in with invalid credentials

**Module:** Login
**Priority:** High

## Preconditions
- Browser is open
- User has invalid login credentials

## Test Steps
1. Navigate to "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
2. Enter "Invalidadmin" in the Username field
3. Enter "invalidadmin123" in the Password field
4. Click the "Login" button

## Expected Result
User is displayed an error message "Invalid credentials"

## Test Data
- Username: Invalidadmin
- Password: invalidadmin123