from base.base_test import BaseTest
import allure
import pytest
import random

@allure.feature("Admin features functionality")
class TestAddEmployeePage(BaseTest):

    @allure.title("Create a new user")
    @allure.severity("Critical")
    @pytest.mark.adminFeatures
    def test_add_new_employee(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.open_pim_page()
        self.pim_page.is_opened()
        self.pim_page.click_on_add_button()
        self.add_employee_page.is_opened()
        self.add_employee_page.enter_first_name("TestName")
        self.add_employee_page.enter_middle_name("TestName")
        self.add_employee_page.enter_last_name("TestName")
        self.add_employee_page.change_employee_id(f"{random.randint(1000, 9999)}")
        self.add_employee_page.show_login_details()
        self.add_employee_page.create_username(self.data.EMPLOYEE_LOGIN)
        self.add_employee_page.create_password(self.data.EMPLOYEE_PASSWORD)
        self.add_employee_page.confirm_created_password(self.data.EMPLOYEE_PASSWORD)
        self.add_employee_page.click_on_save_button()
        self.add_employee_page.check_success_status("Success", "Новый пользователь не создан")
        self.add_employee_page.make_screenshot("Success")