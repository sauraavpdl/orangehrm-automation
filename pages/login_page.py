from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    DASHBOARD_HEADING = (By.XPATH, "//h6[text()='Dashboard']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-alert-content-text")
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def enter_username(self, username):
        self.type_text(self.USERNAME_FIELD, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_FIELD, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_dashboard_heading(self):
        return self.get_text(self.DASHBOARD_HEADING)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    
