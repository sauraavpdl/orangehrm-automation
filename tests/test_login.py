import logging

import test_data.login_data as login_data
from pages import login_page

logger = logging.getLogger(__name__)


def test_valid_login(driver):
    """Log in with valid credentials and verify the dashboard loads."""
    logger.info("START: valid login")
    login_page_obj = login_page.LoginPage(driver)
    login_page_obj.open()

    login_page_obj.login(login_data.VALID_USERNAME, login_data.VALID_PASSWORD)

    actual_heading = login_page_obj.get_dashboard_heading()
    assert actual_heading == "Dashboard", f"Expected 'Dashboard' but got '{actual_heading}'"
    logger.info("PASSED: valid login")


def test_invalid_login(driver):
    """Log in with wrong credentials and verify the error message."""
    logger.info("START: invalid login")
    login_page_obj = login_page.LoginPage(driver)
    login_page_obj.open()

    login_page_obj.login(login_data.INVALID_USERNAME, login_data.INVALID_PASSWORD)

    error = login_page_obj.get_error_message()
    assert error == "Invalid credentials", f"Unexpected error: '{error}'"
    logger.info("PASSED: invalid login")
