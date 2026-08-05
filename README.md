# OrangeHRM Login Automation

Automated test suite for the login functionality of [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/), built as a portfolio project to demonstrate QA automation fundamentals using Python, Selenium, and pytest.

## Tech Stack
- Python
- Selenium WebDriver
- pytest
- webdriver-manager

## Project Structure
orangehrm-automation/
├── tests/
│ ├── conftest.py # Shared fixtures (browser setup/teardown) and logging config
│ ├── test_login.py # Automated login test cases
│ └── test_cases_docs/ # Test cases documented in plain English before automation
│ ├── TC01_login_valid.md
│ └── TC02_login_invalid.md
├── pytest.ini # pytest configuration and custom markers
├── requirements.txt # Project dependencies
└── README.md

## Test Cases Covered
| ID | Description | Status |
|---|---|---|
1. TC01 - Verify user can log in with valid credentials | Automated |
2. TC02 - Verify user cannot log in with invalid credentials | Automated |
3. TC03 - Verify user can logout from the site | Automated |
4. TC04 - Verify user can add new employee | Automated |
5. TC05 - Verify user can add new employee with login details |Automated|


## Key Practices Used
- **Fixtures** (`conftest.py`) for reusable browser setup/teardown
- **Explicit waits** (`WebDriverWait`) instead of hard-coded sleeps
- **Logging** for test execution traceability
- **Custom markers** (`@pytest.mark.smoke`) for selective test runs
- **Test cases documented before automation**, mirroring real QA workflow

## How to Run
```bash
# Clone the repo
git clone https://github.com/sauraavpdl/orangehrm-automation.git
cd orangehrm-automation

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/test_login.py -v

# Run only smoke tests
pytest -m smoke
```

## Author
Saurav — QA Engineer transitioning to SDET

A couple of things to note: