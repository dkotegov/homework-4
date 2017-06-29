# coding=utf-8
from base import BasePage
from tests.elements.main import UserDropdown


class MainPage(BasePage):
    url = 'https://github.com/'

    def wait_username(self):
        user_drop_down = UserDropdown(self.driver)
        user_drop_down.check_user_nav().wait_for_visible()

    def get_username(self):
        self.navigate()
        user_drop_down = UserDropdown(self.driver)
        user_drop_down.get_drop_down().wait_for_clickable().get().click()
        return user_drop_down.get_user_name().wait_for_visible().get().text
