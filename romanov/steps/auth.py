from romanov.steps.common import CommonSteps
from romanov.pages.auth import Pages
from romanov.app.driver import connect


class Steps(CommonSteps):
    def __init__(self):
        connect.init()

    def __del__(self):
        connect.destroy()

    @staticmethod
    def open_login():
        Pages.click_login_modal()

    @staticmethod
    def enter_login_data():
        Pages.enter_login()
        Pages.enter_pass()

    @staticmethod
    def open_reg():
        Pages.click_reg_modal()

    @staticmethod
    def enter_reg_data(email, login, password):
        Pages.enter_email(email)
        Pages.enter_login(login)
        Pages.enter_pass(password)

    @staticmethod
    def login():
        Pages.click_login()
        Pages.wait_modal_welcome()

    @staticmethod
    def reg():
        Pages.click_reg()
        Pages.wait_modal_welcome()

    @staticmethod
    def enter_login(login):
        Pages.enter_login(login)

    @staticmethod
    def enter_pass(password):
        Pages.enter_pass(password)

    @staticmethod
    def click_login():
        Pages.click_login()

    @staticmethod
    def login_app():
        Steps.open_app()
        Steps.open_login()
        Steps.enter_login_data()
        Steps.login()
        Steps.close_welcome()

    @staticmethod
    def close_welcome():
        Pages.close_welcome()

    @staticmethod
    def click_reg():
        Pages.click_reg()

    @staticmethod
    def clear():
        Pages.clear_auth()

    @staticmethod
    def find_info_error():
        Pages.find_info_error()

    @staticmethod
    def find_auth_menu():
        Pages.find_auth_menu()