from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AddJobTitlePage(BasePage):

    ADMIN_MENU= (By.XPATH,"//span[normalize-space(.)='Admin']")
    JOB_TITLE_MENU= (By.XPATH,"//span[normalize-space(.)='Jobs']")
    JOB_TITLE_SUBMENU= (By.XPATH,"//a[normalize-space(.)='Job Titles']")
    ADD_BUTTON= (By.XPATH,"//button[normalize-space(.)='Add']")


    JOB_TITLE_INPUT= (By.XPATH,"//label[normalize-space(.)='Job Title')]/parent::div/following-sibling::div")
    JOB_DESCRIPTION_INPUT= (By.XPATH,"//label[normalize-space(.)='Job Description']/parent::div/following-sibling::div")
    NOTE_INPUT= (By.XPATH,"//label[normalize-space(.)='Note']//parent::div/following-sibling::div/textarea")

    SUBMIT_BUTTON= (By.XPATH,"//button[@type='submit']")
    CANCEL_BUTTON= (By.XPATH,"//button[@type='button']")

    def click_admin_menu(self):
        self.click(self.ADMIN_MENU)

    def click_job_title_menu(self):
        self.click(self.JOB_TITLE_MENU)

    def click_job_title_submenu(self):
        self.click(self.JOB_TITLE_SUBMENU)

    def click_add_button(self):
        self.click(self.ADD_BUTTON)

    def enter_job_title(self, job_title):
        self.type_text(self.JOB_TITLE_INPUT, job_title)

    def enter_job_description(self, job_description):
        self.type_text(self.JOB_DESCRIPTION_INPUT, job_description)


    def enter_note(self, note):
        self.type_text(self.NOTE_INPUT, note)

    def click_submit_button(self):
        self.click(self.SUBMIT_BUTTON)

    def click_cancel_button(self):
        self.click(self.CANCEL_BUTTON)