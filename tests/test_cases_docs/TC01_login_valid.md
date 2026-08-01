# TC01 - Verify user can log in with valid credentials

**Module:** Login
**Priority:** High

## Preconditions
- Browser is open
- User has valid login credentials

## Test Steps
1. Navigate to "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
2. Enter "Admin" in the Username field
3. Enter "admin123" in the Password field
4. Click the "Login" button

## Expected Result
User is redirected to the Dashboard page, and the page displays "Dashboard" in the header

## Test Data
- Username: Admin
- Password: admin123