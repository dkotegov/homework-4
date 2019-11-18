from pages.auth import AuthPage


def login(self):
    auth_page = AuthPage(self.driver)
    auth_page.open()

    auth_form = auth_page.form
    auth_form.set_login(self.LOGIN)
    auth_form.submit_account_name()
    auth_form.set_password(self.PASSWORD)
    auth_form.submit()
