from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class AddEmployeePage(BasePage):

    PIM_LINK = (By.XPATH, "//span[normalize-space()='PIM']")
    PIM_HEADER = (By.XPATH, "//h6[text()='PIM']")
    LOADING_SPINNER = (By.CLASS_NAME, "oxd-loading-spinner")

    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//button[text()=' Add ']")
    FIRST_NAME_INPUT = (By.NAME, "firstName")
    MIDDLE_NAME_INPUT = (By.NAME, "middleName")
    LAST_NAME_INPUT = (By.NAME, "lastName")
    EMPLOYEE_ID_INPUT = (By.XPATH, "//label[text()='Employee Id']/parent::div/following-sibling::div[1]//input")

    CREATE_LOGIN_TOGGLE = (By.CLASS_NAME, "oxd-switch-wrapper")
    USERNAME_INPUT = (By.XPATH, "//label[text()='Username']/parent::div/following-sibling::div[1]//input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Password']/parent::div/following-sibling::div[1]//input")
    CONFIRM_PASSWORD_INPUT = (By.XPATH, "//label[text()='Confirm Password']/parent::div/following-sibling::div[1]//input")
    PHOTO_UPLOAD_INPUT = (By.CLASS_NAME, "oxd-file-input")

    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    EMPLOYEE_NAME_HEADING = (By.CSS_SELECTOR, "div.orangehrm-edit-employee-name h6")

    def click_pim_link(self):
        self.click(self.PIM_LINK)
        self.wait.until(EC.presence_of_element_located(self.PIM_HEADER))

    def click_add_employee_button(self):
        self.wait.until(EC.invisibility_of_element(self.LOADING_SPINNER))
        self.click(self.ADD_EMPLOYEE_BUTTON)
        self.wait.until(EC.invisibility_of_element(self.LOADING_SPINNER))
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_INPUT))

    def enter_first_name(self, first_name):
        self.wait.until(EC.invisibility_of_element(self.LOADING_SPINNER))
        self.type_text(self.FIRST_NAME_INPUT, first_name)

    def enter_middle_name(self, middle_name):
        self.type_text(self.MIDDLE_NAME_INPUT, middle_name)

    def enter_last_name(self, last_name):
        self.type_text(self.LAST_NAME_INPUT, last_name)

    def enter_employee_id(self, emp_id):
        self.type_text(self.EMPLOYEE_ID_INPUT, emp_id)

    def enable_login_details(self):
        self.click(self.CREATE_LOGIN_TOGGLE)

    def enter_username(self, username):
        self.type_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type_text(self.PASSWORD_INPUT, password)

    def enter_confirm_password(self, password):
        self.type_text(self.CONFIRM_PASSWORD_INPUT, password)

    def upload_photo(self, photo_path):
        self.driver.find_element(*self.PHOTO_UPLOAD_INPUT).send_keys(str(photo_path))

    def click_save_button(self):
        self.click(self.SAVE_BUTTON)

    def get_employee_name_heading(self, expected_full_name):
        self.wait.until(EC.text_to_be_present_in_element(self.EMPLOYEE_NAME_HEADING, expected_full_name))
        return self.get_text(self.EMPLOYEE_NAME_HEADING)
