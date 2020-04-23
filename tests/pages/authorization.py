from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.profile import ProfilePage
from tests.pages.registration import RegPage


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
    mail = '//input[@id="emailinput"]'
    password = '//input[@id="passwordinput"]'
    submit_button = '//input[@type="submit"]'
    incorrect_field = '//div[@id="loginTextErr"]'
    reg_button = '//a[@href="/"]'

    def set_mail(self, mail):
        self.fill_input(self.driver.find_element_by_xpath(self.mail), mail)

    def set_password(self, password):
        self.fill_input(self.driver.find_element_by_xpath(self.password), password)

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def authorise(self, mail, password):
        self.set_mail(mail)
        self.set_password(password)
        self.submit()

        ProfilePage(self.driver, open=False).wait_for_load()

    def incorrect_authorise(self, mail, password):
        self.set_mail(mail)
        self.set_password(password)
        self.submit()

        self.wait_for_visible(By.XPATH, self.incorrect_field)

    def to_registration_page(self):
        self.driver.find_element_by_xpath(self.reg_button).click()
        RegPage(self.driver, open=False).wait_for_load()


