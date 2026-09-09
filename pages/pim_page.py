from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class PIMPage(BasePage):

    #employee information page locators
    EMPLOYEE_NAME = (
        By.XPATH,
        "//label[normalize-space()='Employee Name']/parent::div/following-sibling::div[1]//input",
    )
    EMPLOYEE_ID = (
        By.XPATH,
        "//label[normalize-space()='Employee Id']/parent::div/following-sibling::div[1]//input",
    )
    EMPLOYMENT_STATUS = (
        By.XPATH,
        "//label[normalize-space()='Employment Status']/parent::div/following-sibling::div[1]//div[@class='oxd-select-text-input']",
    )
    INCLUDE = (
        By.XPATH,
        "//label[normalize-space()='Include']/parent::div/following-sibling::div[1]//div[@class='oxd-select-text-input']",
    )
    SUPERVISOR_NAME = (
        By.XPATH,
        "//label[normalize-space()='Supervisor Name']/parent::div/following-sibling::div[1]//input",
    )
    JOB_TITLE = (
        By.XPATH,
        "//label[normalize-space()='Job Title']/parent::div/following-sibling::div[1]//div[@class='oxd-select-text-input']",
    )
    SUB_UNIT = (
        By.XPATH,
        "//label[normalize-space()='Sub Unit']/parent::div/following-sibling::div[1]//div[@class='oxd-select-text-input']",
    )

    # Dropdown option / autocomplete suggestion, filled in with .format() at use-time
    DROPDOWN_OPTION_BY_TEXT = (By.XPATH, f"//div[@role='option']//span[normalize-space()='{option_text}']")
    

    RESET_BUTTON = (By.CSS_SELECTOR, "button[type='reset']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    #Add employee button 
    
    ADD_BUTTON = (By.XPATH, "//button[.//text()[contains(.,'Add')]]")

 
    ROW_EDIT_BUTTON = ".//button[.//i[contains(@class,'bi-pencil-fill')]]"
    ROW_DELETE_BUTTON = ".//button[.//i[contains(@class,'bi-trash')]]"

    # ---Pagination locators ------------------------------------------------
    PAGINATION_NEXT_BUTTON = By.CSS_SELECTOR("i.bi-chevron-right")
    PAGINATION_PREVIOUS_BUTTON = By.CSS_SELECTOR("i.bi-chevron-left")
    PAGINATION_PAGE_BY_NUMBER = (By.XPATH,"//button[contains(@class,'oxd-pagination-page-item--page')][normalize-space()='2']",)

    

    def _enter_employee_name(self, name):
        self.type_text(self.EMPLOYEE_NAME,name)

    def _enter_employee_id(self, employee_id):
        self.type_text(self.EMPLOYEE_ID, employee_id)

    def _select_status(self, status):
        self.click(self.EMPLOYMENT_STATUS)
        option_locator =





    
        
        self.SEARCH_BUTTON()


    
    