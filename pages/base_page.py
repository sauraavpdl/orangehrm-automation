from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        
    def open(self):
        self.driver.get(self.url)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def get_value(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")

    # locator
    LOADER = (By.CSS_SELECTOR, ".oxd-loading-spinner")

    # function
    def wait_for_loader_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))

    # locators
    TOAST_TITLE = (By.XPATH, "//p[contains(@class,'oxd-text--toast-title') and contains(text(),'Success')]")
    TOAST_MESSAGE = (By.CSS_SELECTOR, ".oxd-text--toast-message")
    TOAST_CLOSE = (By.CSS_SELECTOR, ".oxd-toast-close")

    # function
    def wait_for_toast(self):
        self.wait.until(EC.visibility_of_element_located(self.TOAST_CLOSE)).click()

    def get_toast_message(self):
        toast_msg = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located(
                        (By.CSS_SELECTOR, "p.oxd-text--toast-message")
                        )
                    )
        return toast_msg.text

    def get_toast_title(self):
        toast_title = WebDriverWait(self.driver, 10).until(
                            EC.visibility_of_element_located(
                                (By.CSS_SELECTOR, "p.oxd-text--toast-title")
                                )
                            )
        return toast_title.text

   