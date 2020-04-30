from tests.conftest import accessor as a
from tests.pages.auth.pages import Pages
from tests.steps.base.base_steps import BaseSteps


class Steps(BaseSteps):
    @staticmethod
    def open_auth_page():
        Pages.click_auth_modal()
        assert a.current_url == 'https://cinsear.ru/login'

    @staticmethod
    def enter_credentials():
        Pages.enter_username()
        Pages.enter_password()

    @staticmethod
    def login():
        Pages.click_login_button()
        Pages.wait_until_page_load()

    @staticmethod
    def auth():
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_credentials()
        Steps.login()

    @staticmethod
    def enter_register(name, login, pass1, pass2):
        Pages.set_register_name(name)
        Pages.set_register_email(login)
        Pages.set_register_password(pass1)
        Pages.set_register_password_clone(pass2)

    @staticmethod
    def submit_reqister():
        Pages.click_reqister_button()

    @staticmethod
    def find_register_name_error():
        Pages.find_register_name_error()

    @staticmethod
    def find_register_login_error():
        Pages.find_register_email_error()

    @staticmethod
    def find_register_password_error():
        Pages.find_register_password_error()

    @staticmethod
    def find_register_password_clone_error():
        Pages.find_register_password_clone_error()

    @staticmethod
    def find_register_error():
        Pages.find_register_error()

    @staticmethod
    def enter_incorrect_login(login):
        Pages.enter_login_login(login)

    @staticmethod
    def enter_correct_password():
        Pages.enter_password()

    @staticmethod
    def submit_login():
        Pages.click_login_button()

    @staticmethod
    def find_login_login_error():
        Pages.find_login_login_error()

    @staticmethod
    def find_login_password_error():
        Pages.find_login_password_error()

    @staticmethod
    def enter_correct_login():
        Pages.enter_username()

    @staticmethod
    def enter_incorrect_password(password):
        Pages.enter_login_password(password)
