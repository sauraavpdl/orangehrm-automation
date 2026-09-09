# TC07 - Verify 'No Records Found' message is displayed when searching for a non-existent employee name

# Module: PIM - Employee List / Search Priority: Medium

## Preconditions
1. User is logged in with valid credentials
2. User has navigated to PIM > Employee List

## Test Steps
1. Enter a non-existent employee name (e.g. "Zzxxqq Notreal") in the Employee Name search field
2. Click "Search"

## Expected Result
Employee list table shows no rows, and a toast message with the text "No Records Found" is displayed

# Test Data: 
First Name: John1
Last Name: Doe