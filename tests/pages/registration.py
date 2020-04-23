from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent
from tests.pages.profile import ProfilePage
from tests.pages.solarsunrise_urls import AuthPage

class RegPage(Page):
    PATH = '/'
    ROOT = {
        'method': By.ID,
        'key': 'signup-page'
    }

    def __init__(self, driver, open=True):
        Page.__init__(self, driver)
        if open:
            self.open()

    @property
    def form(self):
        return RegForm(self.driver)


class RegForm(FormComponent):
    mail = '//input[@id="signUpEmail"]'
    login = '//input[@id="signUpUsername"]'
    password = '//input[@id="signUpPassword"]'
    submit_button = '//button[@class="buttonComponent"]'
    incorrect_field = '//div[@id="errorText"]'
    login_button = '//a[@href="/login"]'

    def set_mail(self, mail):
        self.fill_input(self.driver.find_element_by_xpath(self.mail), mail)

    def set_login(self, login):
        self.fill_input(self.driver.find_element_by_xpath(self.login), login)

    def set_password(self, password):
        self.fill_input(self.driver.find_element_by_xpath(self.password), password)

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def registration(self, mail, login, password):
        self.set_mail(mail)
        self.set_login(login)
        self.set_password(password)
        self.submit()

        ProfilePage(self.driver, open=False).wait_for_load()

    def test_error_text(self, errtext=''):
        if errtext != '':
            assert self.get_elem_text(self.incorrect_field) != errtext

    def incorrect_registration(self, mail, login, password, errtext=''):
        self.set_mail(mail)
        self.set_login(login)
        self.set_password(password)
        self.submit()

        self.wait_for_visible(By.XPATH, self.incorrect_field)
        # self.test_error_text(errtext)

    def to_login_page(self):
        self.driver.find_element_by_xpath(self.login_button).click()
        AuthPage(self.driver, open=False).wait_for_load()

