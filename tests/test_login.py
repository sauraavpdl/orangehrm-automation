from pages import login_page
import test_data.login_data as login_data
import logging
logger=logging.getLogger(__name__)

##test valid login

def test_valid_login(driver):
    logger.info("Opening the browser")
    login_page_obj = login_page.LoginPage(driver)
    login_page_obj.open()
    logger.info("Adding username")
    login_page_obj.enter_username(login_data.VALID_USERNAME)
    logger.info("Adding password")
    login_page_obj.enter_password(login_data.VALID_PASSWORD)
    logger.info("click on login")
    login_page_obj.click_login()

    actual_heading = login_page_obj.get_dashboard_heading()
    assert actual_heading == "Dashboard", "Failed to get dashboard"
    logger.info("logged in successfully")


def test_invalid_login(driver):
    login_page_obj= login_page.LoginPage(driver)

    logger.info("Navigating to login page")
    login_page_obj.open()

    logger.info("Entering invalid username")
    login_page_obj.enter_username(login_data.INVALID_USERNAME)

    logger.info("Entering invalid password")
    login_page_obj.enter_password(login_data.INVALID_PASSWORD)

    logger.info("Clicking login button")
    login_page_obj.click_login()

    actual_error=login_page_obj.get_error_message() 
    assert actual_error == "Invalid credentials" , "Test Failed"
    logger.info("test passed")
