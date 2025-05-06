from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    # locators
    SUCCESS_STATUS = ("xpath", "//p[text()='Success']")

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def is_opened(self):
        self.wait.until(EC.url_to_be(self.PAGE_URL))

    def check_success_status(self, text, error_message):
        success_status = self.wait.until(EC.visibility_of_element_located(self.SUCCESS_STATUS))
        assert success_status.text == text, error_message