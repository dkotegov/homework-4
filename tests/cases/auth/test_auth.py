from tests.steps.auth.steps import Steps


class TestLogin:
    INCORRECT_LOGIN = 'aaaa@'
    INCORRECT_PASSWORD = '1'

    def test_success_login(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_credentials()
        Steps.login()

    def test_incorrect_login_correct_password(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_incorrect_login(self.INCORRECT_LOGIN)
        Steps.enter_correct_password()
        Steps.submit_login()
        Steps.find_login_login_error()

    def test_correct_login_incorrect_password(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_correct_login()
        Steps.enter_incorrect_password(self.INCORRECT_PASSWORD)
        Steps.submit_login()
        Steps.find_login_password_error()

    def test_incorrect_login_incorrect_password(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_incorrect_login(self.INCORRECT_LOGIN)
        Steps.enter_incorrect_password(self.INCORRECT_PASSWORD)
        Steps.submit_login()
        Steps.find_login_login_error()
        Steps.find_login_password_error()
