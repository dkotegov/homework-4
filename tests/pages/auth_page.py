from tests.pages.page import Page, Component


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    LOGIN_FIELD = 'field_login'
    PASSWORD_FIELD = 'field_password'
    SUBMIT_BUTTON = 'button_login'

    def set_login(self, login):
        self.driver.find_element_by_id(self.LOGIN_FIELD).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_id(self.PASSWORD_FIELD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_name(self.SUBMIT_BUTTON).click()
