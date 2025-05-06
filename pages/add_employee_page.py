from base.base_page import BasePage
from config.links import Links
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

class AddEmployeePage(BasePage):

    PAGE_URL = Links.ADD_EMPLOYEE_PAGE

    # locators
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    EMPLOYEE_ID_FIELD = ("xpath", "(//div[contains(@class, 'oxd-grid-2')])[1]//input")
    USERNAME_CREATE_FIELD = ("xpath", "(//input[@ autocomplete='off'])[1]")
    PASSWORD_CREATE_FIELD = ("xpath", "(//input[@type='password'])[1]")
    PASSWORD_CONFIRM_CREATE_FIELD = ("xpath", "(//input[@type='password'])[2]")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")
    TOGGLE_LOGIN_DETAILS = ("xpath", "//span[contains(@class, 'oxd-switch-input--active')]")

    def enter_first_name(self, first_name):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(first_name)

    def enter_middle_name(self, middle_name):
        self.wait.until(EC.element_to_be_clickable(self.MIDDLE_NAME_FIELD)).send_keys(middle_name)

    def enter_last_name(self, last_name):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(last_name)

    def change_employee_id(self, id):
        employee_id = self.wait.until(EC.element_to_be_clickable(self.EMPLOYEE_ID_FIELD))
        employee_id.send_keys(Keys.COMMAND + "A")
        employee_id.send_keys(Keys.DELETE)
        employee_id.send_keys(id)

    def show_login_details(self):
        self.wait.until(EC.element_to_be_clickable(self.TOGGLE_LOGIN_DETAILS)).click()

    def create_username(self, username):
        self.wait.until(EC.element_to_be_clickable(self.USERNAME_CREATE_FIELD)).send_keys(username)

    def create_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_CREATE_FIELD)).send_keys(password)

    def confirm_created_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self.PASSWORD_CONFIRM_CREATE_FIELD)).send_keys(password)

    def click_on_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()