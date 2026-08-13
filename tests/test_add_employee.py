import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login
from pathlib import Path
import time


logger = logging.getLogger(__name__)

def test_add_employee(driver,generate_time_based_emp_id):
    """Verify user can add a new employee successfully (TC04)."""
    first_name = "John121"
    last_name = "Doe"

    logger.info("Opening the OrangeHRM application and logging in")
    login(driver, "Admin", "admin123")

    logger.info("navigating to the PIM module")
    pim_module = driver.find_element(By.CSS_SELECTOR, "a[href='/web/index.php/pim/viewPimModule']")
    pim_module.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']")))
    logger.info("PIM module loaded successfully")
    wait.until(EC.invisibility_of_element((By.CLASS_NAME,"oxd-loading-spinner")))
    add_employee_button = driver.find_element(By.XPATH, "//button[text()=' Add ']")
    add_employee_button.click()
    wait.until(EC.invisibility_of_element((By.CLASS_NAME,"oxd-loading-spinner")))
    wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
    logger.info("Add Employee page loaded successfully")

    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys(first_name)
    
    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys(last_name)

    emp_id_field = driver.find_element(By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div[1]//input")
    emp_id_field.send_keys(generate_time_based_emp_id)   

    save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    save_button.click()
    logger.info("Clicked save button to add employee")

    full_name = f"{first_name} {last_name}"
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6"),full_name))
    name_heading = driver.find_element(By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6")
    assert full_name in name_heading.text
    logger.info(f"Test passed: Employee '{full_name}' added successfully")
    

def test_add_employee_with_login_details(driver,generate_time_based_emp_id):
    """Verify user can add a new employee with login details successfully (TC05)."""
    first_name = "Jane"
    middle_name = "Roth"
    last_name = "Smith"
    username = "janesmith123"
    password = "Password123"

    logger.info("Opening the OrangeHRM application and logging in")
    login(driver, "Admin", "admin123")

    logger.info("navigating to the PIM module")
    pim_module = driver.find_element(By.CSS_SELECTOR, "a[href='/web/index.php/pim/viewPimModule']")
    pim_module.click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='PIM']")))
    logger.info("PIM module loaded successfully")

    add_employee_button = driver.find_element(By.XPATH, "//button[text()=' Add ']")
    add_employee_button.click()
    wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
    logger.info("Add Employee page loaded successfully")

    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys(first_name)
    middle_name_field = driver.find_element(By.NAME, "middleName")
    middle_name_field.send_keys(middle_name)
    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys(last_name)
    logger.info(f"Entered employee details: {first_name} {middle_name} {last_name}")

    emp_id_field = driver.find_element(By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div[1]//input")
    emp_id_field.send_keys(generate_time_based_emp_id) 

    login_details_checkbox=driver.find_element(By.CLASS_NAME,"oxd-switch-wrapper")
    login_details_checkbox.click()
    logger.info("Clicked on 'Create Login Details' checkbox")


    user_name_field = driver.find_element(By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div[1]//input")
    user_name_field.click()
    user_name_field.send_keys(username)
    logger.info("Entered username for the new employee login details")

    password_field = driver.find_element(By.XPATH, "//label[text()='Password']/parent::div/following-sibling::div[1]//input")
    password_field.click()
    password_field.send_keys(password)
    logger.info("Entered password for the new employee login details")

    confirm_password_field = driver.find_element(By.XPATH, "//label[text()='Confirm Password']/parent::div/following-sibling::div[1]//input")
    confirm_password_field.click()
    confirm_password_field.send_keys(password) 
    logger.info("Entered confirm password for the new employee login details")

    
    base_dir=Path(__file__).parent.parent
    photo_path=base_dir / "resources" / "images"/"employee.png"
    driver.find_element(By.CLASS_NAME, "oxd-file-input").send_keys(str(photo_path))

    save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    save_button.click()
    logger.info("Clicked save button to add employee")

    full_name = f"{first_name} {last_name}"
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6"),full_name))
    name_heading = driver.find_element(By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6")
    assert full_name in name_heading.text
    logger.info(f"Test passed: Employee '{full_name}' added successfully")    