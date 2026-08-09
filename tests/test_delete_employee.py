import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import login

logger = logging.getLogger(__name__)

def test_delete_employee(driver):
    """Verify user can delete an existing employee successfully (TC06)."""
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

    search_employee_field = driver.find_element(By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div[1]//input")
    search_employee_field.send_keys(f"{first_name} {last_name}")

    search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    search_button.click()
    logger.info(f"Searched for employee '{first_name} {last_name}'")

    wait.until(EC.presence_of_element_located((By.XPATH, f"//div[text()='{first_name} {last_name}']")))
    logger.info(f"Employee '{first_name} {last_name}' found in the search results")

    delete_button = driver.find_element(By.XPATH, f"//div[text()='{first_name} {last_name}']/ancestor::tr//button[@title='Delete']")
    delete_button.click()
    logger.info(f"Clicked delete button for employee '{first_name} {last_name}'")

    confirm_delete_button = driver.find_element(By.XPATH, "//button[text()=' Yes, Delete ']")
    confirm_delete_button.click()
    logger.info(f"Confirmed deletion of employee '{first_name} {last_name}'")

    wait.until(EC.invisibility_of_element_located((By.XPATH, f"//div[text()='{first_name} {last_name}']")))
    logger.info(f"Employee '{first_name} {last_name}' deleted successfully")