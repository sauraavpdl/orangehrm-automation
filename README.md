# OrangeHRM Test Automation

Automated UI test suite for [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/), built as a portfolio project to demonstrate QA automation fundamentals with Python, Selenium, and pytest using the Page Object Model.

## Tech Stack

- Python
- Selenium WebDriver
- pytest
- webdriver-manager

## Project Structure

```
orangehrm-automation/
├── config/
│   └── config.py              # Base URL and shared settings
├── pages/                     # Page Objects: one class per page
│   ├── base_page.py           # Shared actions (click, type, waits, toast)
│   ├── login_page.py
│   ├── pim_page.py
│   ├── add_employee_page.py
│   ├── add_job_title_page.py
│   ├── pay_grade_page.py
│   └── apply_leave_page.py
├── tests/
│   ├── test_login.py
│   ├── test_add_employee.py
│   ├── test_add_job_title.py
│   ├── test_add_pay_grade.py
│   ├── test_apply_leave.py
│   └── test_assign_leave.py
├── test_data/
│   ├── login_data.py          # Valid and invalid credentials
│   └── new_employee_data.py   # Base employee data
├── utils/
│   ├── data_generator.py      # Unique names, IDs and usernames per run
│   └── wait_utils.py          # Reusable wait helpers
├── resources/
│   ├── images/                # Upload files (e.g. employee photo)
│   └── resume/                # Upload files for candidate tests
├── conftest.py                # Fixtures (driver, logged_in_driver) and logging setup
├── pytest.ini                 # pytest configuration and markers
├── requirements.txt           # Dependencies
└── README.md


## Test Coverage

| Area | Scenarios | Status |
|---|---|---|
| Login | Valid login, invalid login | Automated |
| Employee | Add without login details, add with login details, new employee can log in | Automated |
| Admin | Add job title | Automated |
| Admin | Add pay grade | Automated |
| Leave | Apply leave, assign leave | Automated |

## Key Practices

- **Page Object Model:** locators and actions live in `pages/`, and tests only describe the scenario
- **Fixtures** in `conftest.py` for browser setup/teardown and an authenticated session
- **Explicit waits** (`WebDriverWait`) instead of hard-coded sleeps
- **Unique test data per run** (random suffixes) so tests can be rerun without duplicate errors
- **Data-driven credentials** kept separate from test logic in `test_data/`
- **Logging** to console and `test_run.log`, with passwords masked
- **Assertions with clear failure messages** (expected vs. actual)

## How to Run

```bash
# Clone the repo
git clone https://github.com/sauraavpdl/orangehrm-automation.git
cd orangehrm-automation

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows

# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest -v

# Run a single file
pytest tests/test_add_employee.py -v

# Run only smoke tests (if markers are defined in pytest.ini)
pytest -m smoke
```

Logs are written to `test_run.log` after each run.

## Author

Saurav, QA Engineer 