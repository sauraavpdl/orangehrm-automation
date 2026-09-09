from pages import apply_leave_page
import time


def test_apply_leave(logged_in_driver):
    apply_leave_obj=apply_leave_page.ApplyLeavePage(logged_in_driver)
    apply_leave_obj.navigate_to_leave_page()

    
    
    apply_leave_obj.leave_type_dropdown()
    
    apply_leave_obj.click_from_date_field()
    apply_leave_obj.click_from_date_picker()
    apply_leave_obj.click_to_date_field()
    apply_leave_obj.click_to_date_picker()
    apply_leave_obj.click_apply_button()
