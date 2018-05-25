from tests.pages.mobile.page import Page, Component


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)

    def auth(self, login, password):
        self.open()
        auth_form = self.form
        auth_form.set_login(login)
        auth_form.set_password(password)
        auth_form.submit()


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
