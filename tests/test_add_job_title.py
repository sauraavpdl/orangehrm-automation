from pages.add_job_title_page import AddJobTitlePage

def test_add_job_title(logged_in_driver):
    add_job_title_page = AddJobTitlePage(logged_in_driver)

    # Navigate to the Job Titles page
    add_job_title_page.click_admin_menu()
    add_job_title_page.click_job_title_menu()
    add_job_title_page.click_job_title_submenu()

    # Click the "Add" button to add a new job title
    add_job_title_page.click_add_button()

    # Fill in the job title details
    add_job_title_page.enter_job_title("Software Engineer")
    add_job_title_page.enter_job_description("Responsible for developing software applications.")
    add_job_title_page.enter_note("This is a note for the job title.")

    # Submit the form to save the new job title
    add_job_title_page.click_submit_button()