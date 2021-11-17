from tests.pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from components.navbar import NavbarComponent
from selenium.common.exceptions import NoSuchElementException


class RestaurantRegistrationPage(Page):
    PATH = '/restaurants/signup'
    EMAIL_INPUT = '//input[@name="email"]'
    PHONE_INPUT = '//input[@name="phone"]'
    TITLE_INPUT = '//input[@name="title"]'
    ADDRESS_INPUT = '//input[@id="js__map-signup-address"]'
    RADIUS_INPUT = '//input[@name="radius"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    REPEAT_PASSWORD_INPUT = '//input[@name="repeatPassword"]'
    SUBMIT_BUTTON = '//input[@value="Зарегистрировать свой ресторан"]'
    GO_TO_RESTAURANT_AUTH_BUTTON = '//a[text()="Уже зарегистрирован"]'
    GO_TO_CUSTOMER_AUTH_BUTTON = '//a[text()="У меня нет ресторана, я просто хочу кушать"]'
    EMAIL_ERROR = '//p[@id="emailError"]'
    PHONE_ERROR = '//p[@id="numberError"]'
    TITLE_ERROR = '//p[@id="titleError"]'
    PASSWORD_ERROR = '//p[@id="passwordError"]'
    REPEAT_PASSWORD_ERROR = '//p[@id="repeatPasswordError"]'
    RADIUS_ERROR = '//p[@id="radiusError"]'
    REGISTRATION_ERROR = '//p[@id="serverError"]'

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def set_email(self, email):
        self.driver.find_element_by_xpath(self.EMAIL_INPUT).send_keys(email)

    def set_phone(self, phone):
        self.driver.find_element_by_xpath(self.PHONE_INPUT).send_keys(phone)

    def set_title(self, email):
        self.driver.find_element_by_xpath(self.TITLE_INPUT).send_keys(email)

    def set_address(self, address):
        self.driver.find_element_by_xpath(self.ADDRESS_INPUT).send_keys(address)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def set_repeat_password(self, password):
        self.driver.find_element_by_xpath(self.REPEAT_PASSWORD_INPUT).send_keys(password)

    def set_radius(self, radius):
        self.driver.find_element_by_xpath(self.RADIUS_INPUT).send_keys(radius)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_until_registered(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.navbar.USERNAME)))

    def go_to_restaurant_auth(self):
        self.driver.find_element_by_xpath(self.GO_TO_RESTAURANT_AUTH_BUTTON).click()

    def go_to_customer_auth(self):
        self.driver.find_element_by_xpath(self.GO_TO_CUSTOMER_AUTH_BUTTON).click()

    def get_email_error(self):
        return self.driver.find_element_by_xpath(self.EMAIL_ERROR).text

    def get_phone_error(self):
        return self.driver.find_element_by_xpath(self.PHONE_ERROR).text

    def get_title_error(self):
        return self.driver.find_element_by_xpath(self.TITLE_ERROR).text

    def get_password_error(self):
        return self.driver.find_element_by_xpath(self.PASSWORD_ERROR).text

    def get_repeat_password_error(self):
        return self.driver.find_element_by_xpath(self.REPEAT_PASSWORD_ERROR).text

    def get_radius_error(self):
        return self.driver.find_element_by_xpath(self.RADIUS_ERROR).text

    def check_if_error_occurred(self):
        try:
            self.driver.find_element_by_xpath(self.REGISTRATION_ERROR)
        except NoSuchElementException:
            return False
        return True

    def get_registration_error(self):
        return self.driver.find_element_by_xpath(self.REGISTRATION_ERROR).text
