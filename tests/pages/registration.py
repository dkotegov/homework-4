from selenium.webdriver.common.by import By
from tests.pages.base import Page
from tests.pages.component import FormComponent


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
    nickname_field = '//div[@class="profile-username"]'

    def set_mail(self, mail):
        self.fill_input(self.driver.find_element_by_xpath(self.mail), mail)

    def set_login(self, login):
        self.fill_input(self.driver.find_element_by_xpath(self.login), login)

    def set_password(self, password):
        self.fill_input(self.driver.find_element_by_xpath(self.password), password)

    def submit(self):
        self.driver.find_element_by_xpath(self.submit_button).click()

    def check_nickname(self):
        self.wait_for_visible(By.XPATH, self.nickname_field)
        return self.get_elem_text(self.nickname_field)

    def check_error_field(self):
        self.wait_for_visible(By.XPATH, self.incorrect_field)
        return self.get_elem_text(self.incorrect_field)
