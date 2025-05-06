import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    # locators
    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    LOGIN_BUTTON = ("xpath", "//button[@type='submit']")

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_FIELD)).send_keys(login)

    @allure.step("Enter password")
    def enter_password(self,  password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_FIELD)).send_keys(password)

    @allure.step("Click on submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()