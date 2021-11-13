from tests.pages.base import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from components.navbar import NavbarComponent
from selenium.common.exceptions import NoSuchElementException


class RestaurantAuthPage(Page):
    PATH = '/restaurants/signin'
    LOGIN_INPUT = '//input[@name="login"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    SUBMIT_BUTTON = '//input[@value="Войти"]'
    REGISTRATION_BUTTON = '//a[text()="Зарегистрировать свой ресторан"]'
    CUSTOMER_AUTH_BUTTON = '//a[text()="У меня нет ресторана, я просто хочу кушать"]'
    LOGIN_ERROR = '//p[@id="loginError"]'
    PASSWORD_ERROR = '//p[@id="passwordError"]'
    AUTH_ERROR = '//p[@id="serverError"]'

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN_INPUT).send_keys(login)

    def set_password(self, password):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(password)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def wait_until_login(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, self.navbar.RESTAURANT_NAME)))

    def go_to_registration(self):
        self.driver.find_element_by_xpath(self.REGISTRATION_BUTTON).click()

    def go_to_customer_auth(self):
        self.driver.find_element_by_xpath(self.CUSTOMER_AUTH_BUTTON).click()

    def get_login_error(self):
        return self.driver.find_element_by_xpath(self.LOGIN_ERROR).text

    def get_password_error(self):
        return self.driver.find_element_by_xpath(self.PASSWORD_ERROR).text

    def check_if_error_occurred(self):
        try:
            self.driver.find_element_by_xpath(self.AUTH_ERROR)
        except NoSuchElementException:
            return False
        return True

    def get_auth_error(self):
        return self.driver.find_element_by_xpath(self.AUTH_ERROR).text
