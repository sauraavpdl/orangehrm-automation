from pages.add_employee_page import AddEmployeePage
from pathlib import Path
from test_data.new_employee_data import employees
import logging


def test_add_employee(logged_in_driver):
    """Add an employee with only personal details and verify the success toast."""
    logging.info("Starting test: add employee without login details")

    emp = employees["basic_employee"] 

    add_employee_obj = AddEmployeePage(logged_in_driver)

     # Navigate    
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()

    # Add Personal details
    logging.info("Adding employee details")

    logging.info("Entering name: %s %s %s", emp["first_name"], emp["middle_name"], emp["last_name"])
    add_employee_obj.enter_first_name(emp["first_name"])
    add_employee_obj.enter_middle_name(emp["middle_name"])
    add_employee_obj.enter_last_name(emp["last_name"])

    logging.info("Employee ID: %s", emp["employee_id"])
    add_employee_obj.enter_employee_id(emp["employee_id"])

    
    base_dir = Path(__file__).parent.parent
    photo_path = base_dir / "resources" / "images" / "employee.png"
    add_employee_obj.upload_photo(photo_path)

    # Save
    logging.info("clicking save button")
    add_employee_obj.click_save_button()
    

    toast_message=add_employee_obj.get_toast_message()
    logging.info("Toast message received: %s", toast_message)
    assert toast_message=="Successfully Saved" ,  f"Expected Success but got {toast_message}"
    logging.info("Test passed")



def test_add_employee_with_login_details(logged_in_driver):
    """Add an employee with both personal and login details and verify the success toast."""
    logging.info("Starting test: add employee with login details")

    emp = employees["employee_with_login"]

    logging.info("Starting test: add employee with login details")

    add_employee_obj = AddEmployeePage(logged_in_driver)

    # Navigate 
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()

    # Add Personal details
    logging.info("Adding employee details")
    logging.info("Entering name: %s %s %s", emp["first_name"], emp["middle_name"], emp["last_name"])
    
    add_employee_obj.enter_first_name(emp["first_name"])
    add_employee_obj.enter_middle_name(emp["middle_name"])
    add_employee_obj.enter_last_name(emp["last_name"])
    add_employee_obj.enter_employee_id(emp["employee_id"])

    # Photo upload
    base_dir = Path(__file__).parent.parent
    photo_path = base_dir / "resources" / "images" / "employee.png"
    add_employee_obj.upload_photo(photo_path)
   

    add_employee_obj.enable_login_details()

    # Add login details
    add_employee_obj.enter_username(emp["username"])
    add_employee_obj.enter_password(emp["password"])
    add_employee_obj.enter_confirm_password(emp["password"])

    # Save
    logging.info("clicking save button")
    add_employee_obj.click_save_button()

    toast_message= add_employee_obj.get_toast_message()
    logging.info("Toast message received: %s", toast_message)

    assert toast_message == "Successfully Saved" , f"Expected Success but got {toast_message}"
    logging.info("Test passed")