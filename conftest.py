import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import datetime
from pages.login_page import LoginPage


# ---- Logger setup ----
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("test_run.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ---- Reusable browser fixture ----
@pytest.fixture
def driver():
    browser_name = "chrome"  # just change this line instead of commenting code

    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.maximize_window()
    yield driver
    driver.quit()

# ---AutoLogin---

@pytest.fixture
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    return driver



@pytest.fixture
def generate_time_based_emp_id():
    return datetime.datetime.now().strftime("d%M%S")
