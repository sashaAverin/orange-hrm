import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class PimPage(BasePage):

    PAGE_URL = Links.PIM_PAGE

    # locators
    USERNAME_SEARCH_FIELD = ("xpath", "(//input[@placeholder='Type for hints...'])[1]")
    ADD_BUTTON = ("xpath", "//button[text()=' Add ']")
    SEARCH_BUTTON = ("xpath", "//button[@type='submit']")
    REMOVE_BUTTON = ("xpath", "//div[@class='oxd-table-cell-actions']/button[2]")

    @allure.step("Click on add button")
    def click_on_add_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_BUTTON)).click()

    def enter_name_for_search(self, name):
        with allure.step(f"Search by name {name}"):
            self.wait.until(EC.element_to_be_clickable(self.USERNAME_SEARCH_FIELD)).send_keys(name)

    @allure.step("Click on search button")
    def click_on_search_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()

    @allure.step("Click on remove button")
    def click_on_remove_button(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_BUTTON)).click()