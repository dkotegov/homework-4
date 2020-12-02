from romanov.steps.common import CommonSteps
from romanov.pages.profile import Pages as UserPages
from romanov.pages.new_pin_desk import Pages
from romanov.app.driver import connect

class Steps(CommonSteps):
    def __init__(self):
        connect.init()

    def __del__(self):
        connect.destroy()

    @staticmethod
    def open_new_pin():
        Pages.click_new_menu()
        Pages.click_new_pin()

    @staticmethod
    def open_new_desk():
        Pages.click_new_menu()
        Pages.click_new_desk()

    @staticmethod
    def add_image(url):
        Pages.add_image(url)

    @staticmethod
    def add_true_image(url):
        Pages.add_image(url)
        Pages.wait_image()

    @staticmethod
    def clear_name():
        Pages.clear_name()

    @staticmethod
    def find_no_error():
        label = Pages.find_no_error()
        return label

    @staticmethod
    def find_pin_error():
        label = Pages.find_pin_error()
        return label

    @staticmethod
    def find_desk_error():
        label = Pages.find_desk_error()
        return label

    @staticmethod
    def create_pin():
        Pages.click_create_pin()

    @staticmethod
    def find_ok_messsage():
        label = Pages.find_ok_messsage()
        return label

    @staticmethod
    def create_desk():
        Pages.click_create_desk()

    @staticmethod
    def create_end_desk(name, desc):
        Steps.open_new_desk()
        Steps.enter_name(name)
        Steps.enter_desc(desc)
        Steps.create_desk()
        Steps.find_ok_messsage()

    @staticmethod
    def check_created_desk_pin_page(name):
        Pages.check_created_desk_pin_page(name)

    @staticmethod
    def check_created_desk_user_page(name):
        Pages.check_created_desk_user_page(name)

    @staticmethod
    def enter_name(name):
        Pages.enter_name(name)

    @staticmethod
    def enter_desc(desc):
        Pages.enter_desc(desc)