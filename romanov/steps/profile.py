from romanov.steps.common import CommonSteps
from romanov.pages.profile import Pages
from romanov.app.driver import connect

class Steps(CommonSteps):
    def __init__(self):
        connect.init()

    def __del__(self):
        connect.destroy()

    @staticmethod
    def open_user_profile(id=None):
        if id:
            connect.driver.get('https://zinterest.ru/user/' + str(id))
        else:
            Pages.click_user_menu()

    @staticmethod
    def open_chat():
        Pages.click_chat()

    @staticmethod
    def following():
        Pages.click_following_user()

    @staticmethod
    def unfollowing():
        Pages.click_unfollowing_user()

    @staticmethod
    def open_desk():
        Pages.open_first_desk()

    @staticmethod
    def open_settings():
        Pages.click_settings()

    @staticmethod
    def new_pin():
        Pages.click_new_pin()

    @staticmethod
    def open_subs():
        Pages.click_subs()

    @staticmethod
    def open_empty_pins():
        Pages.click_user_pins()
        Pages.find_empty_feed()

    @staticmethod
    def open_user_pins():
        Pages.click_user_pins()

    @staticmethod
    def logout():
        Pages.click_exit()

    @staticmethod
    def click_empty_followers():
        Pages.click_user_followers()
        Pages.find_empty_modal()

    @staticmethod
    def click_empty_followings():
        Pages.click_user_followings()
        Pages.find_empty_modal()

    @staticmethod
    def click_followers():
        Pages.click_user_followers()
        Pages.find_users_modal()

    @staticmethod
    def click_followings():
        Pages.click_user_followings()
        Pages.find_users_modal()
