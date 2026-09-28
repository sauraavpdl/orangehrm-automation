from pages.pay_grade_page import AddPayGradePage
# from utils.wait_utils import wait_for_toast_text
import logging


def test_add_pay_grade_shows_success_toast(logged_in_driver):
    name = "Secretary10191"
    logging.info("Starting test: test_add_pay_grade")
    AddPayGradeObj = AddPayGradePage(logged_in_driver)

    logging.info("Navigating to the pay grade page")
    AddPayGradeObj.click_admin_menu()
    AddPayGradeObj.click_job_title_menu()
    AddPayGradeObj.click_job_title_submenu()

    logging.info("Clicking add button")
    AddPayGradeObj.click_add_button()

    logging.info("Entering pay grade name")
    AddPayGradeObj.enter_name(name)

    logging.info("Clicking save button")
    AddPayGradeObj.save()

    logging.info("Checking success toast")
    
    assert AddPayGradeObj.confirm() == name

    logging.info("Test Pass")



