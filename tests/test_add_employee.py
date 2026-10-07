import logging
from pathlib import Path

from pages.add_employee_page import AddEmployeePage
from pages.login_page import LoginPage
from test_data.new_employee_data import employees
from utils.data_generator import unique_name, unique_employee_id

logger = logging.getLogger(__name__)

PHOTO_PATH = Path(__file__).parent.parent / "resources" / "images" / "employee.png"


def build_employee(key):
    """Copy the base data and make the fields OrangeHRM requires to be unique."""
    emp = {**employees[key], "employee_id": unique_employee_id()}
    if "username" in emp:
        emp["username"] = unique_name("alice.johnson")
    return emp


def test_add_employee_without_login_details(logged_in_driver):
    """Add an employee with only personal details and verify the success toast."""
    emp = build_employee("basic_employee")
    logger.info("START: add employee WITHOUT login details")

    add_employee_obj = AddEmployeePage(logged_in_driver)

    # Navigate
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()

    # Fill the form
    add_employee_obj.fill_personal_details(emp)
    add_employee_obj.upload_photo(PHOTO_PATH)

    # Save and verify
    add_employee_obj.click_save_button()
    toast_message = add_employee_obj.get_toast_message()
    logger.info("Toast message received: %s", toast_message)

    assert toast_message == "Successfully Saved", (
        f"Expected 'Successfully Saved' but got '{toast_message}'"
    )
    logger.info("PASSED: add employee WITHOUT login details")


def test_add_employee_with_login_details(logged_in_driver):
    """Add an employee with personal and login details and verify the success toast."""
    emp = build_employee("employee_with_login")
    logger.info("START: add employee WITH login details")

    add_employee_obj = AddEmployeePage(logged_in_driver)

    # Navigate
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()

    # Fill the form
    add_employee_obj.fill_personal_details(emp)
    add_employee_obj.upload_photo(PHOTO_PATH)
    add_employee_obj.fill_login_details(emp)

    # Save and verify
    add_employee_obj.click_save_button()
    toast_message = add_employee_obj.get_toast_message()
    logger.info("Toast message received: %s", toast_message)

    assert toast_message == "Successfully Saved", (
        f"Expected 'Successfully Saved' but got '{toast_message}'"
    )
    logger.info("PASSED: add employee WITH login details")


def test_new_employee_can_log_in(logged_in_driver):
    """Create an employee with login details, then log in as that employee."""
    emp = build_employee("employee_with_login")
    logger.info("START: new employee can log in")

    add_employee_obj = AddEmployeePage(logged_in_driver)
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()
    add_employee_obj.fill_personal_details(emp)
    add_employee_obj.fill_login_details(emp)
    add_employee_obj.click_save_button()

    toast_message = add_employee_obj.get_toast_message()
    assert toast_message == "Successfully Saved", (
        f"Employee was not created. Toast: '{toast_message}'"
    )

    # End the admin session
    logged_in_driver.delete_all_cookies()

    login_page_obj = LoginPage(logged_in_driver)
    login_page_obj.open()
    login_page_obj.login(emp["username"], emp["password"])

    heading = login_page_obj.get_dashboard_heading()
    assert heading == "Dashboard", f"New employee could not log in. Heading: '{heading}'"
    logger.info("PASSED: new employee can log in")