from tests.steps.auth.steps import Steps
from tests.conftest import accessor as a

NAME_VALID = "sanya" 
NAME_NOT_VALID = "a"
EMAIL_VALID = "a@a.a"
EMAIL_NOT_VALID = "a"
PASSWORD_VALID = "11111"
PASSWORD_NOT_VALID = "1"


class TestLogin:
    def test_name_not_valid(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_register(NAME_NOT_VALID, EMAIL_VALID, PASSWORD_VALID, PASSWORD_VALID)
        Steps.submit_reqister()
        Steps.find_register_name_error()
        Steps.find_register_error()

    def test_login_not_valid(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_register(NAME_VALID, EMAIL_NOT_VALID, PASSWORD_VALID, PASSWORD_VALID)
        Steps.submit_reqister()
        Steps.find_register_login_error()
        Steps.find_register_error()

    def test_password_not_valid(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_register(NAME_VALID, EMAIL_VALID, PASSWORD_NOT_VALID, PASSWORD_VALID)
        Steps.submit_reqister()
        Steps.find_register_password_error()
        Steps.find_register_error()
    
    def test_passwords_dont_match(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_register(NAME_VALID, EMAIL_VALID, PASSWORD_VALID, PASSWORD_VALID+PASSWORD_VALID)
        Steps.submit_reqister()
        Steps.find_register_password_clone_error()
        Steps.find_register_error()

    def test_empty(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_register("", "", "","")
        Steps.submit_reqister()
        Steps.find_register_error()

    def test_email_registred(self):
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_register(NAME_VALID, a.username, PASSWORD_VALID, PASSWORD_VALID)
        Steps.submit_reqister()
        Steps.find_register_error()