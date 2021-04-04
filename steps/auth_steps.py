from pages.auth_page import AuthPage
from steps.base_steps import Steps


class AuthSteps(Steps):
    def __init__(self, driver):
        super().__init__(driver)
        self.page = AuthPage(driver)

    def open_login_form(self):
        self.page.navbar.click_menu()
        self.page.login_form.wait_until_visible()

    def fill_login_form(self, login, password):
        self.page.login_form.set_login_text(login)
        self.page.login_form.set_password_text(password)

    def close_login_form_by_submit(self):
        self.page.login_form.submit()
        self.page.login_form.wait_until_invisible()

    def close_login_form_by_button(self):
        self.page.login_form.click_close()
        self.page.login_form.wait_until_invisible()
