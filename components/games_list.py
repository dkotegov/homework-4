from selenium.common.exceptions import TimeoutException

from components.base_component import BaseComponent
from constants import game


class GamesList(BaseComponent):
    INVITE_FRIENDS_BUTTON = "//a[contains(@hrefattrs, 'SM_AppCtrl_Invite')]"
    GAME_BUTTON = "//div[@class='ucard-v __xs']"
    USER_AVATAR = "//div[@class='avatar user']"
    CHOOSE_USER = "//div[@class='leftCardAddInfo']"
    CONFIRM_CHOICE = "//input[@name='button_invite']"
    LOCK_MARK = "//div[contains(@class, 'ic_closed')]"

    def __init__(self, driver):
        super(GamesList, self).__init__(driver)
        self.app_id = 0
        self.el = ''

    def get_invite_friends_button(self):
        return self.get_clickable_element(self.INVITE_FRIENDS_BUTTON)

    def get_game(self):
        self.el = self.get_elements_by_path(game.THRONEWARS_ID)[0]
        return self.el
        # return self.get_clickable_element_by_element(el)

    def get_user_avatar(self):
        return self.get_element_by_path(self.USER_AVATAR)

    def get_choose_user(self):
        return self.get_clickable_element(self.CHOOSE_USER)

    def get_confirm_user(self):
        return self.get_clickable_element(self.CONFIRM_CHOICE)

    # def get_appId(self):
    #     element_hrefattrs = self.get_clickable_element(self.APP_ID).get_attribute('hrefattrs')
    #     self.app_id =
    def get_lock(self):
        try:
            return self.get_clickable_element(self.LOCK_MARK)
        except TimeoutException:
            return False
