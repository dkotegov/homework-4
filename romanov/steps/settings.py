from romanov.steps.common import CommonSteps
from romanov.pages.profile import Pages as UserPages
from romanov.pages.settings import Pages
from romanov.app.driver import connect

class Steps(CommonSteps):
    def __init__(self):
        connect.init()

    def __del__(self):
        connect.destroy()

    @staticmethod
    def open_settings():
        UserPages.click_user_menu()
        UserPages.click_settings()

    @staticmethod
    def change_avatar(url):
        Pages.load_avatar(url)

    @staticmethod
    def change_pass(password=None):
        if password is None:
            Pages.enter_pass()
        else:
            Pages.enter_pass(password)
        Pages.save_pass()

    @staticmethod
    def change_email(email):
        Pages.enter_email(email)
        Pages.save_data()

    @staticmethod
    def change_login(login=None):
        if login is None:
            Pages.enter_login()
        else:
            Pages.enter_login(login)
        Pages.save_data()

    @staticmethod
    def change_desc(desc):
        Pages.enter_desc(desc)
        Pages.save_data()

    @staticmethod
    def change_data(email, desc, login=None, password=None):
        Steps.change_login(login)
        Pages.close_done()
        Steps.change_pass(password)
        Pages.close_done()
        Steps.change_email(email)
        Pages.close_done()
        Steps.change_desc(desc)
        Pages.close_done()

    @staticmethod
    def get_data():
        return Pages.get_data()

    @staticmethod
    def find_success_modal():
        label = Pages.find_success_modal()
        return label

    @staticmethod
    def find_info_error():
        label = Pages.find_info_error()
        return label
