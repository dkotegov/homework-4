from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.profile import ProfilePage


class AuthPage(Page):
    PATH = '/login'
    ROOT = {
        'method': By.ID,
        'key': 'login-page'
    }

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.open()

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(FormComponent):
    login = '//input[@id="emailinput"]'
    password = '//input[@id="passwordinput"]'
    submit_button = '//input[@type="submit"]'

    def set_login(self, login):
        self.fill_input(self.driver.find_element_by_xpath(self.login), login)

    def set_password(self, password):
        self.fill_input(self.driver.find_element_by_xpath(self.password), password)

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def authorise(self, login, password):
        self.set_login(login)
        self.set_password(password)
        self.submit()

        ProfilePage(self.driver, open=False).wait_for_load()


