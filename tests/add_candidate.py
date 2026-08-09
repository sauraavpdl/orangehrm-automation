from email.mime import base

import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path
import utils
import time

logger=logging.getLogger(__name__)

logger.info("Starting test: test_add_candidate")

def test_add_candidate(driver):
    """Verify user can add a new candidate successfully (TC07)."""
    first_name = "Alice"
    middle_name = "M"
    last_name = "Johnson1"
    email = "alicemjohnson1@yopmail.com"
    contact_number = "1234567890"
    Resume_path = str(Path(__file__).parent / "test_resume.pdf")  # Ensure this file exists in the same directory
    keywords = "Python, Selenium, Automation"
    note = "This is a test candidate for automation testing."

    logger.info("Opening the OrangeHRM application and logging in")
    utils.login(driver, "Admin", "admin123")
    driver.implicitly_wait(10)

    logger.info("Navigating to the Recruitment section")
    recruitment_module = driver.find_element(By.CSS_SELECTOR, "a[href='/web/index.php/recruitment/viewRecruitmentModule']")
    recruitment_module.click()      

    logger.info("Clicking on the 'Add' button to add a new candidate")

    add_candidate_button = driver.find_element(By.XPATH, "//button[normalize-space()='Add']")
    add_candidate_button.click()        

    logger.info("Filling in candidate details")
    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys(first_name)
  
    middle_name_field = driver.find_element(By.NAME, "middleName")
    middle_name_field.send_keys(middle_name)

    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys(last_name)

    logger.info("Selecting job vacancy from dropdown")
    dropdown=driver.find_element(By.CLASS_NAME,"oxd-select-wrapper")
    dropdown.click()
    dropdown_option=driver.find_elements(By.CSS_SELECTOR,"div[role='listbox'] span")[0]
    dropdown_option.click()
    
    email_field = driver.find_element(By.XPATH, "//label[text()='Email']/parent::div/following-sibling::div[1]//input")
    email_field.send_keys(email)

    contact_number_field = driver.find_element(By.XPATH, "//label[text()='Contact Number']/parent::div/following-sibling::div[1]//input")
    contact_number_field.send_keys(contact_number)  

    logger.info("Uploading resume and adding keywords")
    time.sleep(3)
    base_path=Path(__file__).parent.parent
    resume_file_path = base_path / "resources" / "resume" / "valid_resume.pdf"
    driver.find_element(By.CSS_SELECTOR, "input[type='file']").send_keys(str(resume_file_path))

    logger.info("Uploading resume and adding keywords")
    
    keywords_field = driver.find_element(By.XPATH, "//label[text()='Keywords']/parent::div/following-sibling::div[1]//input")
    keywords_field.send_keys(keywords)      

    logger.info("Adding a note for the candidate")
    note_field = driver.find_element(By.XPATH, "//label[text()='Notes']/parent::div/following-sibling::div[1]//textarea")        
    note_field.send_keys(note)
    
    concent_of_data_checkbox = driver.find_element(By.CLASS_NAME,"oxd-checkbox-wrapper")
    concent_of_data_checkbox.click()  
    logger.info("concent checkbox clicked")  

    logger.info("Submitting the candidate details")
    save_button = driver.find_element(By.XPATH, "//button[text()=' Save ']")
    save_button.click()

    logger.info("Candidate added successfully. Verifying the candidate details in the list.")

    assert driver.find_element(By.XPATH, "//label[text()='Name']/parent::div/following-sibling::div/p").text==f"{first_name} {middle_name} {last_name}"
