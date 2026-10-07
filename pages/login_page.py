import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage  # keep your existing import

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DASHBOARD_HEADING = (By.XPATH, "//h6[text()='Dashboard']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def enter_username(self, username):
        logger.info("Entering username: %s", username)
        self.type_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        logger.info("Entering password: ********")
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        logger.info("Clicking login button")
        self.click(self.LOGIN_BUTTON)

    def login(self, username, password):
        """Log in with any credentials passed by the caller."""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def get_dashboard_heading(self):
        return self.get_text(self.DASHBOARD_HEADING)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)