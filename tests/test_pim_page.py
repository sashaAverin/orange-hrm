from base.base_test import BaseTest
import allure
import pytest

@allure.feature("User operation functionality")
class TestPimPage(BaseTest):

    @allure.title("Remove user")
    @allure.severity("Major")
    @pytest.mark.adminFeatures
    def test_remove_user(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.open_pim_page()
        self.pim_page.is_opened()
        self.pim_page.enter_name_for_search("TestName")
        self.pim_page.click_on_search_button()
        self.pim_page.wait_disappear_of_spinner()
        self.pim_page.click_on_remove_button()
        self.pim_page.click_on_popup_delete_button()
        self.pim_page.check_success_status("Success", "Пользователь не удалён")
        self.pim_page.make_screenshot("Success")