from selenium.common.exceptions import TimeoutException

from components.base_component import BaseComponent
from constants import game


class GamesList(BaseComponent):
    INVITE_FRIENDS_BUTTON = "//i[@class ='tico_img ic ic_group']"
    GAME_DELETE = "//div[@class='user-settings __apps']/div[1]"
    GAME_DELETE_BUTTON = "//div[@class='user-settings __apps']/div[1]/div/div/a[2]"
    GAME_BUTTON = "//div[@class='ucard-v __xs']"
    USER_AVATAR = "//span[@data-id='578592967841']/../img"
    CHOOSE_USER = "//input[@value='578592967841']/../div/div[2]/div[2]/div[2]/div[2]"
    CONFIRM_CHOICE = "//input[@name='button_invite']"
    LOCK_MARK = "//div[contains(@class, 'ic_closed')]"
    DELETE_BUTTON = "//ul[@class='u-menu']"
    BACK_BUTTON = "//div[@class='layerPanelClose ic ic_close']"
    BLOOD_BUTTON_GAME = "//div[@class='apps-showcase__list']/div[8] //div[@class='uslider_hld']/div[9]/div/div[1]/a"
    RIGHT_ARROW = "//div[@class='apps-showcase__list']/div[8]/div[2]/div[2]"
    HOVER_RIGHT_ARROW = "//div[@class='apps-showcase__list']/div[8]"


    def __init__(self, driver):
        super(GamesList, self).__init__(driver)
        self.app_id = 0
        self.el = ''

    def get_invite_friends_button(self):
        return self.get_clickable_element(self.INVITE_FRIENDS_BUTTON)

    def get_hover_right_arrow(self):
        return self.get_visibility_element(self.HOVER_RIGHT_ARROW)

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

    def get_delete_button(self):
        return self.get_visibility_element(self.DELETE_BUTTON)

    def get_blood(self):
        if self.get_visibility_element_with_exception(game.BLOODOFTITANS_ID) is False:
            return False
        #return self.get_visibility_element_with_exception(game.BLOODOFTITANS_ID)
        return True

    def get_invite(self):
        self.get_searching_element(self.INVITE_FRIENDS_BUTTON)

    def get_delete_game(self):
        return self.get_visibility_element(self.GAME_DELETE)

    def get_delete_game_button(self):
        return self.get_visibility_element(self.GAME_DELETE_BUTTON)

    def get_back_button(self):
        return self.get_visibility_element(self.BACK_BUTTON)

    def get_blood_button_game(self):
        return self.get_visibility_element(self.BLOOD_BUTTON_GAME)

    def get_right_arrow(self):
        return self.get_visibility_element(self.RIGHT_ARROW)