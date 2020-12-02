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
        link = Pages.click_chat()
        return link

    @staticmethod
    def following():
        label = Pages.click_following_user()
        return label

    @staticmethod
    def unfollowing():
        label = Pages.click_unfollowing_user()
        return label

    @staticmethod
    def open_desk():
        link = Pages.open_first_desk()
        return link

    @staticmethod
    def open_settings():
        link = Pages.click_settings()
        return link

    @staticmethod
    def new_pin():
        text = Pages.click_new_pin()
        return text

    @staticmethod
    def open_subs():
        link = Pages.click_subs()
        return link

    @staticmethod
    def open_empty_pins():
        Pages.click_user_pins()
        label = Pages.find_empty_feed()
        return label

    @staticmethod
    def open_user_pins():
        link = Pages.click_user_pins()
        return link

    @staticmethod
    def logout():
        label = Pages.click_exit()
        return label

    @staticmethod
    def click_empty_followers():
        Pages.click_user_followers()
        label = Pages.find_empty_modal()
        return label

    @staticmethod
    def click_empty_followings():
        Pages.click_user_followings()
        label = Pages.find_empty_modal()
        return label

    @staticmethod
    def click_followers():
        Pages.click_user_followers()
        label = Pages.find_users_modal()
        return label

    @staticmethod
    def click_followings():
        Pages.click_user_followings()
        label = Pages.find_users_modal()
        return label
