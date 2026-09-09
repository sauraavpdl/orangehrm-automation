from pages import add_employee_page
from pathlib import Path
from test_data.new_employee_data import employees


def test_add_employee(logged_in_driver):
    emp = employees["basic_employee"]

    add_employee_obj = add_employee_page.AddEmployeePage(logged_in_driver)
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()
    add_employee_obj.enter_first_name(emp["first_name"])
    add_employee_obj.enter_middle_name(emp["middle_name"])
    add_employee_obj.enter_last_name(emp["last_name"])
    add_employee_obj.enter_employee_id(emp["employee_id"])

    base_dir = Path(__file__).parent.parent.parent
    photo_path = base_dir / "resources" / "images" / "employee.png"
    add_employee_obj.upload_photo(photo_path)
    add_employee_obj.click_save_button()


def test_add_employee_with_login_details(logged_in_driver):
    emp = employees["employee_with_login"]

    add_employee_obj = add_employee_page.AddEmployeePage(logged_in_driver)
    add_employee_obj.click_pim_link()
    add_employee_obj.click_add_employee_button()
    add_employee_obj.enter_first_name(emp["first_name"])
    add_employee_obj.enter_middle_name(emp["middle_name"])
    add_employee_obj.enter_last_name(emp["last_name"])
    add_employee_obj.enter_employee_id(emp["employee_id"])

    base_dir = Path(__file__).parent.parent.parent
    photo_path = base_dir / "resources" / "images" / "employee.png"
    add_employee_obj.upload_photo(photo_path)

    add_employee_obj.enable_login_details()
    add_employee_obj.enter_username(emp["username"])
    add_employee_obj.enter_password(emp["password"])
    add_employee_obj.enter_confirm_password(emp["password"])
    add_employee_obj.click_save_button()