from tests.pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from components.navbar import NavbarComponent
from selenium.common.exceptions import NoSuchElementException


class CustomerRegistrationPage(Page):
    PATH = '/signup'
    EMAIL_INPUT = '//input[@name="email"]'
    PHONE_INPUT = '//input[@name="phone"]'
    NAME_INPUT = '//input[@name="name"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    REPEAT_PASSWORD_INPUT = '//input[@name="repeatPassword"]'
    SUBMIT_BUTTON = '//input[@value="Зарегистрироваться"]'
    GO_TO_AUTH_BUTTON = '//p[text()="У меня уже есть аккаунт"]'
    EMAIL_ERROR = '//p[@id="emailError"]'
    PHONE_ERROR = '//p[@id="numberError"]'
    NAME_ERROR = '//p[@id="nameError"]'
    PASSWORD_ERROR = '//p[@id="passwordError"]'
    REPEAT_PASSWORD_ERROR = '//p[@id="repeatPasswordError"]'
    REGISTRATION_ERROR = '//p[@id="serverError"]'

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.PHONE_INPUT).send_keys(phone)

    def set_name(self, email):
        self.driver.find_element_by_xpath(self.NAME_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def set_repeat_password(self, password):
        self.driver.find_element_by_xpath(self.REPEAT_PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_until_registered(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.navbar.USERNAME)))

    def go_to_auth(self):
        self.driver.find_element_by_xpath(self.GO_TO_AUTH_BUTTON).click()

    def get_email_error(self):
        return self.driver.find_element_by_xpath(self.EMAIL_ERROR).text

    def get_phone_error(self):
        return self.driver.find_element_by_xpath(self.PHONE_ERROR).text

    def get_name_error(self):
        return self.driver.find_element_by_xpath(self.NAME_ERROR).text

    def get_password_error(self):
        return self.driver.find_element_by_xpath(self.PASSWORD_ERROR).text

    def get_repeat_password_error(self):
        return self.driver.find_element_by_xpath(self.REPEAT_PASSWORD_ERROR).text

    def check_if_error_occurred(self):
        try:
            self.driver.find_element_by_xpath(self.REGISTRATION_ERROR)
        except NoSuchElementException:
            return False
        return True

    def get_registration_error(self):
        return self.driver.find_element_by_xpath(self.REGISTRATION_ERROR).text
