from tests.components.component import Component

from selenium.webdriver.support.ui import WebDriverWait


class ProfileForm(Component):
    NAME_INPUT = '//input[@id="fname-input"]'
    NAME_ERROR = '//div[@id="fname-input-wrapper_err"]'
    SURNAME_INPUT = '//input[@id="lname-input"]'
    SURNAME_ERROR = '//div[@id="lname-input-wrapper_err"]'
    EMAIL_INPUT = '//input[@id="email-input"]'
    EMAIL_ERROR = '//div[@id="email-input-wrapper_err"]'
    SAVE_BUTTON = '//button[@id="profile-area__submit"]'
    LOG_OUT_BUTTON = '//button[@id="profile-area__log-out"]'

    def wait_open(self):
        return WebDriverWait(self.driver, 5, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SAVE_BUTTON).is_displayed()
        )

    def set_name(self, name):
        self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(name)

    def get_name_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_PHONE_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.INPUT_PHONE_ERROR).text

    def set_surname(self, surname):
        self.driver.find_element_by_xpath(self.SURNAME_INPUT).send_keys(surname)

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)

    def save(self):
        self.driver.find_element_by_xpath(self.SAVE_BUTTON).click()

    def logout(self):
        self.driver.find_element_by_xpath(self.LOG_OUT_BUTTON).click()

    def open(self):
        self.driver.find_element_by_xpath(self.LOGIN).click()

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.INPUT_PHONE).send_keys(phone)

    def get_phone_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_PHONE_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.INPUT_PHONE_ERROR).text

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.INPUT_PASSWORD).send_keys(password)

    def get_password_error(self):
        WebDriverWait(self.driver, 30, 1).until(
            lambda d: d.find_element_by_xpath(self.INPUT_PASSWORD_ERROR).text != ''
        )
        return self.driver.find_element_by_xpath(self.INPUT_PASSWORD_ERROR).text

    def clean_password(self):
        self.driver.find_element_by_xpath(self.INPUT_PASSWORD).clear()

    def clean_phone(self):
        self.driver.find_element_by_xpath(self.INPUT_PHONE).clear()

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()
