from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def login(driver, username, password):
    """Logs into OrangeHRM with given credentials and waits for the dashboard to load."""
    wait = WebDriverWait(driver, 20)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//h6[text()='Dashboard']")))

