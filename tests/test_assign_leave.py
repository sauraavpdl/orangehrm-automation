import logging
from pages import apply_leave_page
from selenium.webdriver.support.ui import Select

logger = logging.getLogger(__name__)


def test_apply_leave(logged_in_driver):
    logger.info("Navigating to Assign Leave page")

    leave_page_obj = apply_leave_page.ApplyLeavePage(logged_in_driver)
    leave_page_obj.click(leave_page_obj.LEAVE_PAGE_BUTTON)
    leave_page_obj.click(leave_page_obj.LEAVE_ASSIGN_BUTTON)

    logger.info("Selecting date range for leave application")

       




 # adjust to a real option

    # logger.info("Clicking From Date field and picking a date")
    # leave_page_obj.click_from_date_field()
    # leave_page_obj.click_from_date_picker()

    # logger.info("Clicking To Date field and picking a date")
    # leave_page_obj.click_to_date_field()
    # leave_page_obj.click_to_date_picker()

    # logger.info("Clicking Apply button")
    # leave_page_obj.click_apply_button()

    # balance_text = leave_page_obj.get_leave_balance_text()
    # logger.info(f"Leave balance shown: {balance_text}")
    # assert balance_text != "", "Expected leave balance text to be present"