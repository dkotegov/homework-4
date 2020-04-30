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

    def auth():
        Steps.open_site()
        Steps.open_auth_page()
        Steps.enter_credentials()
        Steps.login()