import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.pim_page import PimPage
from pages.dashboard_page import DashboardPage
from pages.add_employee_page import AddEmployeePage
from pages.my_info_page import MyInfoPage

class BaseTest:
    data: Data

    login_page: LoginPage
    pim_page: PimPage
    dashboard_page: DashboardPage
    add_employee_page: AddEmployeePage
    my_info_page: MyInfoPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.login_page = LoginPage(driver)
        request.cls.pim_page = PimPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.add_employee_page = AddEmployeePage(driver)
        request.cls.my_info_page = MyInfoPage(driver)