from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ApplyLeavePage(BasePage):

    from_date = '26'
    to_date = '30'
    LEAVE_PAGE_BUTTON = (By.XPATH, "//a[normalize-space()='Leave']")
    LEAVE_NAV_BUTTON=(By.XPATH, "//nav[@class='oxd-topbar-body-nav']//a[normalize-space(text())='Apply']")
    LEAVE_ASSIGN_BUTTON = (By.XPATH, "//a[normalize-space()='Assign Leave']")
    APPLY_LEAVE_TYPE_DROPDOWN = (By.CLASS_NAME, 'oxd-select-text-input')
    APPLY_LEAVE_TYPE_OPTION = (By.CSS_SELECTOR, "div[role='option'] span")
    APPLY_LEAVE_FROM_DATE_FIELD = (By.XPATH,"//label[contains(normalize-space(.), 'From Date')]/parent::div/following-sibling::div")
    APPLY_LEAVE_FROM_DATE_PICKER = (By.XPATH, "//div[contains(@class,'oxd-calendar-date') and contains(@class,'--today')]")
    APPLY_LEAVE_TO_DATE_FIELD = (By.XPATH, "//label[contains(normalize-space(.), 'To Date')]/parent::div/following-sibling::div")
    APPLY_LEAVE_TO_DATE_PICKER = (By.XPATH, f"//a[contains(text(),{to_date})]")
    COMMENTS_FIELD = (By.CSS_SELECTOR, "div textarea")
    APPLY_BUTTON = (By.CSS_SELECTOR,"button[type='submit']")
    LEAVE_BALANCE_LEFT = (By.XPATH, "//div[@id='applyleave_leaveBalance']")

    
    def navigate_to_leave_page(self):
        self.click(self.LEAVE_PAGE_BUTTON)
        self.click(self.LEAVE_NAV_BUTTON)
        time.sleep(5)

    def leave_type_dropdown(self):
        self.click(self.APPLY_LEAVE_TYPE_DROPDOWN)
        options = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[role='option'] span")))
        time.sleep(2)  # Wait for the options to be visible
        self.click(options[0])


    def click_from_date_field(self):
        self.click(self.APPLY_LEAVE_FROM_DATE_FIELD)

    def click_from_date_picker(self):
        self.click(self.APPLY_LEAVE_FROM_DATE_PICKER)

    def click_to_date_field(self):
        self.click(self.APPLY_LEAVE_TO_DATE_FIELD)

    def click_to_date_picker(self):
        self.click(self.APPLY_LEAVE_TO_DATE_PICKER)

    def click_apply_button(self):
        self.click(self.APPLY_BUTTON)

    def get_leave_balance_text(self):
        return self.get_text(self.LEAVE_BALANCE_LEFT)