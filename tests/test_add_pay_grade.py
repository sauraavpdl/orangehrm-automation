from pages.pay_grade_page import AddPayGradePage
from utils.data_generator import unique_name
import logging


def test_add_pay_grade_shows_success_toast(logged_in_driver):
    grade_name = unique_name("Secretary")

    logging.info("Starting test: test_add_pay_grade")
    AddPayGradeObj = AddPayGradePage(logged_in_driver)

    #Navigate
    logging.info("Navigating to the pay grade page")
    AddPayGradeObj.click_admin_menu()
    AddPayGradeObj.click_job_title_menu()
    AddPayGradeObj.click_job_title_submenu()

    logging.info("Clicking add button")
    AddPayGradeObj.click_add_button()

    # Details
    logging.info(f"Entering pay grade name: %s",grade_name)
    AddPayGradeObj.enter_name(grade_name)

    logging.info("Clicking save button")
    AddPayGradeObj.save()

    #Assertion
    logging.info("Checking success")
    name = AddPayGradeObj.confirm() 
    assert name==grade_name , f"Expected {grade_name} but got {name} "

    logging.info("Test Pass")



