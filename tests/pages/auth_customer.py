import page
from components.navbar import NavbarComponent


class CustomerAuthPage(page):
    PATH = '/login'
    LOGIN_INPUT = '//input[@name="login"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    SUBMIT_BUTTON = '//span[text()="Войти"]'
    REGISTRATION_BUTTON = '//span[text()="Я тут впервые"]'
    RESTAURANT_AUTH_BUTTON = '//span[text()="Войти как владелец ресторана"]'

    @property
    def navbar(self):
        return NavbarComponent(self.driver)

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN_INPUT).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD_INPUT).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT_BUTTON).click()

    def go_to_registration(self):
        self.driver.find_element_by_xpath(self.REGISTRATION_BUTTON).click()

    def go_to_restaurant_auth(self):
        self.driver.find_element_by_xpath(self.RESTAURANT_AUTH_BUTTON).click()
