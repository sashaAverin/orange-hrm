import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    #locators
    PIM_LINK = ("xpath", "//span[text()='PIM']")
    MY_INFO_LINK = ("xpath", "//span[text()='My Info']")
    PROFILE_MENU_BUTTON = ("xpath", "//span[@class='oxd-userdropdown-tab']")
    LOGOUT_BUTTON = ("xpath", "//a[text()='Logout']")
    SUCCESS_STATUS = ("xpath", "//p[text()='Success']")
    LOAD_SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")
    POPUP_DELETE_BUTTON = ("xpath", "//div[@class='orangehrm-modal-footer']/button[2]")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    @allure.step("Click on 'PIM' link")
    def open_pim_page(self):
            self.wait.until(EC.element_to_be_clickable(self.PIM_LINK)).click()

    @allure.step("Click on 'My Info' link")
    def open_my_info_page(self):
            self.wait.until(EC.element_to_be_clickable(self.MY_INFO_LINK)).click()

    @allure.step("Open profile menu")
    def open_profile_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_MENU_BUTTON)).click()

    @allure.step("Logout from system")
    def logout_account(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON)).click()

    @allure.step("Action has been completed successfully")
    def check_success_status(self, text, error_message):
        success_status = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_STATUS))
        assert success_status.text == text, error_message

    @allure.step("Wait disappear of loader")
    def wait_disappear_of_spinner(self):
        self.wait.until(EC.invisibility_of_element_located(self.LOAD_SPINNER))

    @allure.step("Confirm deletion")
    def click_on_popup_delete_button(self):
        self.wait.until(EC.element_to_be_clickable(self.POPUP_DELETE_BUTTON)).click()

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )