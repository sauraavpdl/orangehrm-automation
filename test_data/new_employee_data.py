# test_data/employee_data.py
from utils.data_generator import unique_name, unique_employee_id

employees = {
    "basic_employee": {
        "first_name": "first",
        "middle_name": "middle",
        "last_name": unique_name("last"),
        "employee_id": unique_employee_id(),
    },
    "employee_with_login": {
        "first_name": "first",
        "middle_name": "middle",
        "last_name": unique_name("last"),
        "employee_id": unique_employee_id(),
        "username": unique_name("firstmiddlelast"),
        "password": "SecurePass123!",
    },
}