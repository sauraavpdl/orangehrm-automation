from pages.add_job_title_page import AddJobTitlePage
import logging
import time




def test_add_job_title(logged_in_driver):

    job_title=f"software engineer {int(time.time())}"
    logging.info("Starting test: test_add_job_title")

    add_job_title_obj = AddJobTitlePage(logged_in_driver)

    logging.info("Navigating to the Job Titles page")

    # Navigate to the Job Titles page
    add_job_title_obj.click_admin_menu()

    logging.info("Clicking on Job Title menu and submenu")
    add_job_title_obj.click_job_title_menu()
    add_job_title_obj.click_job_title_submenu()

    logging.info("Clicking the 'Add' button to add a new job title")

    # Click the "Add" button to add a new job title
    add_job_title_obj.click_add_button()

    logging.info("Filling in the job title details")

    # Fill in the job title details
    add_job_title_obj.enter_job_title(job_title)
    add_job_title_obj.enter_job_description("Responsible for developing software applications.")
    add_job_title_obj.enter_note("This is a note for the job title.")

    logging.info("Submitting the form to save the new job title")

    # Submit the form to save the new job title
    add_job_title_obj.click_submit_button()
    
    logging.info ("verify form submission")

    toast_title=add_job_title_obj.toast_title()
    
    toast_message=add_job_title_obj.toast_message()
    
    
    assert toast_title == "Success" , f"Expected Success but got {toast_title}"
    assert toast_message == "Successfully Saved" , f"Expected Successfully Saved but got {toast_message}"

