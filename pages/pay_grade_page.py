from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class AddPayGradePage(BasePage):

    ADMIN_MENU= (By.XPATH,"//span[normalize-space(.)='Admin']")
    JOB_TITLE_MENU= (By.XPATH,"//span[normalize-space(.)='Job']")
    JOB_TITLE_SUBMENU= (By.XPATH,"//a[normalize-space(.)='Pay Grades']")
    ADD_BUTTON= (By.XPATH,"//button[normalize-space(.)='Add']")

    NAME_FIELD=(By.XPATH,"//label[normalize-space(.)='Name']/parent::div/following-sibling::div/input")
    SAVE_BUTTON= (By.XPATH,"//button[@type='submit']")
    CANCEL_BUTTON= (By.XPATH,"//button[normalize-space(.)='Cancel']")

    def click_admin_menu(self):
            self.click(self.ADMIN_MENU)
    
    def click_job_title_menu(self):
            self.click(self.JOB_TITLE_MENU)
    
    def click_job_title_submenu(self):
            self.click(self.JOB_TITLE_SUBMENU)
    
    def click_add_button(self):
            self.click(self.ADD_BUTTON)

    def enter_name(self, pay_grade_name):
           self.click(self.NAME_FIELD)
           self.type_text(self.NAME_FIELD,pay_grade_name)

    def save(self):
           self.click(self.SAVE_BUTTON)

    def cancel(self):
           self.click(self.CANCEL_BUTTON)
        