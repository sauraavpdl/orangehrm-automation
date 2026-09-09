from pages import login_page
import test_data.login_data as login_data
import logging
logger=logging.getLogger(__name__)

##test valid login

def test_valid_login(driver):
    login_page_obj = login_page.LoginPage(driver)
    login_page_obj.open()
    login_page_obj.enter_username(login_data.VALID_USERNAME)
    login_page_obj.enter_password(login_data.VALID_PASSWORD)
    login_page_obj.click_login()
    assert login_page_obj.get_dashboard_heading() == "Dashboard"


def test_invalid_login(driver):
    login_page_obj= login_page.LoginPage(driver)
    login_page_obj.open()
    login_page_obj.enter_username(login_data.INVALID_USERNAME)
    login_page_obj.enter_password(login_data.INVALID_PASSWORD)
    login_page_obj.click_login()
    assert login_page_obj.get_error_message()== "Invalid credentials"
    logger.info("test passed")
