import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login
logger = logging.getLogger(__name__)

def test_add_employee(driver):
    """Verify user can add a new employee successfully (TC04)."""
    first_name = "John1"
    last_name = "Doe"

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
    wait.until(EC.presence_of_element_located((By.XPATH, "//h6[text()='Add Employee']")))
    logger.info("Add Employee page loaded successfully")

    first_name_field = driver.find_element(By.NAME, "firstName")
    first_name_field.send_keys(first_name)
    last_name_field = driver.find_element(By.NAME, "lastName")
    last_name_field.send_keys(last_name)

    save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    save_button.click()
    logger.info("Clicked save button to add employee")

    full_name = f"{first_name} {last_name}"
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6"),full_name))
    name_heading = driver.find_element(By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6")
    assert full_name in name_heading.text
    logger.info(f"Test passed: Employee '{full_name}' added successfully")