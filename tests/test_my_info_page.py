from base.base_test import BaseTest

class TestChangeProfileInfo(BaseTest):

    def test_change_profile_info(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(self.data.EMPLOYEE_LOGIN)
        self.login_page.enter_password(self.data.EMPLOYEE_PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard_page.is_opened()
        self.dashboard_page.open_my_info_page()
        self.my_info_page.select_day_of_expire_date(1)
        self.my_info_page.select_nationality("Russian")
        self.my_info_page.upload_profile_photo("/source/avatar.png")
        self.my_info_page.click_on_save_button()
        self.my_info_page.check_success_status("Success", "Изменения не сохранены")