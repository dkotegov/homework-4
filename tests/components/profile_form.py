from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class ProfileForm(Component):
    NAME_INPUT = '//input[@id="fname-input"]'
    NAME_ERROR = '//div[@id="fname-input-wrapper_err"]'
    SURNAME_INPUT = '//input[@id="lname-input"]'
    SURNAME_ERROR = '//div[@id="lname-input-wrapper_err"]'
    EMAIL_INPUT = '//input[@id="email-input"]'
    EMAIL_ERROR = '//div[@id="email-input-wrapper_err"]'
    PHOTO_INPUT = '//input[@id="profile-avatar-area__image-input"]'
    PHOTO_IMAGE = '//img[@class="profile-avatar-area__image"]'
    PHOTO_ERROR = '//div[@id="profile-avatar-error"]'
    SAVE_BUTTON = '//button[@id="profile-area__submit"]'
    PROFILE_BLOCK = '//div[@class="profile-view__profile-area"]'
    LOG_OUT_BUTTON = '//button[@id="profile-area__log-out"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.5).until(
            ec.element_to_be_clickable((By.XPATH, self.PROFILE_BLOCK))
        )

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(name)

    def get_name_error(self):
        curr_error = self.driver.find_element_by_xpath(self.NAME_ERROR).text
        WebDriverWait(self.driver, 5, 1).until(
            lambda d: d.find_element_by_xpath(self.NAME_ERROR).text == curr_error
                      and
                      d.find_element_by_xpath(self.NAME_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.NAME_ERROR).text

    def get_name(self):
        return self.driver.find_element_by_xpath(self.NAME_INPUT).get_attribute('value')

    def clear_name(self):
        self.driver.find_element_by_xpath(self.NAME_INPUT).clear()

    def set_surname(self, surname):
        self.driver.find_element_by_xpath(self.SURNAME_INPUT).send_keys(surname)

    def get_surname_error(self):
        curr_error = self.driver.find_element_by_xpath(self.SURNAME_ERROR).text
        WebDriverWait(self.driver, 5, 1).until(
            lambda d: d.find_element_by_xpath(self.SURNAME_ERROR).text != curr_error
                      and
                      d.find_element_by_xpath(self.SURNAME_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.SURNAME_ERROR).text

    def get_surname(self):
        return self.driver.find_element_by_xpath(self.SURNAME_INPUT).get_attribute('value')

    def clear_surname(self):
        self.driver.find_element_by_xpath(self.SURNAME_INPUT).clear()

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)

    def get_email_error(self):
        WebDriverWait(self.driver, 5, 1).until(
            lambda d: d.find_element_by_xpath(self.EMAIL_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.EMAIL_ERROR).text

    def get_email(self):
        return self.driver.find_element_by_xpath(self.EMAIL_INPUT).get_attribute('value')

    def clear_email(self):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).clear()

    def set_photo(self, photo):
        self.driver.find_element_by_xpath(self.PHOTO_INPUT).send_keys(photo)

    def get_photo_src(self):
        WebDriverWait(self.driver, 5, 1).until(
            lambda d: d.find_element_by_xpath(self.PHOTO_IMAGE).is_displayed()
        )
        return self.driver.find_element_by_xpath(self.PHOTO_IMAGE).get_attribute("src")

    def get_photo_error(self):
        WebDriverWait(self.driver, 5, 1).until(
            lambda d: d.find_element_by_xpath(self.PHOTO_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.PHOTO_ERROR).text

    def clear_all(self):
        self.clear_name()
        self.clear_surname()
        self.clear_email()

    def save(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOG_OUT_BUTTON).click()
