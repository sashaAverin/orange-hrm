from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class PimPage(BasePage):

    PAGE_URL = Links.PIM_PAGE

    # locators
    ADD_BUTTON = ("xpath", "//button[text()=' Add ']")

    def click_on_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()