import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Authorization")
class TestLoginPage(BaseTest):

    @allure.title("Login in system")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_login_in_account(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()