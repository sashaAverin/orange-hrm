import os
import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class MyInfoPage(BasePage):

    #locators
    LICENSE_DATE_FIELD = ("xpath", "(//input[@placeholder='yyyy-dd-mm'])[1]")
    NATIONALITY_FIELD = ("xpath", "(//div[@class='oxd-select-text-input'])[1]")
    NATIONALITY_OPTION = ("xpath", "//span[text()='Russian']")
    UPLOAD_PICTURE_FIELD = ("xpath", "//input[@type='file']")
    DAY_OF_LICENSE_BUTTON = ("xpath", "//div[contains(@class, 'oxd-calendar-date-wrapper')][1]")
    PROFILE_IMAGE_BUTTON = ("xpath", "//div[@class='orangehrm-edit-employee-image-wrapper']")
    SAVE_BUTTON = ("xpath", "//button[@type='submit']")

    def select_day_of_expire_date(self, day):
        with allure.step(f"The expire day of driver license - {day}"):
            self.wait.until(EC.element_to_be_clickable(self.LICENSE_DATE_FIELD)).click()
            day_of_expire_data = f"//div[contains(@class, 'oxd-calendar-date-wrapper')][{day}]"
            self.wait.until(EC.element_to_be_clickable(self.driver.find_element("xpath", day_of_expire_data))).click()

    def select_nationality(self, nationality):
        with allure.step(f"Nationality has been selected as '{nationality}'"):
            self.wait.until(EC.element_to_be_clickable(self.NATIONALITY_FIELD)).click()
            option = f"//span[text()='{nationality}']"
            self.wait.until(EC.element_to_be_clickable(self.driver.find_element("xpath", option))).click()

    @allure.step("Upload profile photo")
    def upload_profile_photo(self, picture_way):
        self.wait.until(EC.element_to_be_clickable(self.PROFILE_IMAGE_BUTTON)).click()
        upload_picture = self.wait.until(EC.presence_of_element_located(self.UPLOAD_PICTURE_FIELD))
        upload_picture.send_keys(f"{os.getcwd()}{picture_way}")

    @allure.step("Click on save button")
    def click_on_save_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()