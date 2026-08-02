import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

@pytest.mark.smoke
def test_valid_login(driver):
    logger.info("Starting test: valid login")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logger.info("Navigated to login page")

    wait = WebDriverWait(driver, 10)

    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys("Admin")
    logger.info("Entered username")

    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("admin123")
    logger.info("Entered password")

    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    logger.info("Clicked login button")

    dashboard_heading = wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

    assert dashboard_heading.text == "Dashboard"
    logger.info("Test passed: Dashboard loaded successfully")


def test_invalid_login(driver):
    logger.info("Starting test: invalid login")

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    logger.info("Navigated to login page")

    wait = WebDriverWait(driver, 10)
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    username_field.send_keys("invaliduser")
    logger.info("Entered invalid username")
   
    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("invalidpass")
    logger.info("Entered invalid password")
   
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    logger.info("Clicked login button")

    error_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-alert-content-text")))

    assert error_message.text == "Invalid credentials"
    logger.info("Test passed: Invalid credentials message displayed")
