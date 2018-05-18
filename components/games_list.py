from components.base_component import BaseComponent


class GamesList(BaseComponent):
    INVITE_FRIENDS_BUTTON = "//a[contains(@hrefattrs, 'SM_AppCtrl_Invite')]"
    GAME_BUTTON = "//div[@class='ucard-v __xs']"
    USER_AVATAR = "//div[@class='avatar user']"
    CHOOSE_USER = "//div[@class='leftCardAddInfo']"
    CONFIRM_CHOICE = "//input[@name='button_invite']"

    def get_invite_friends_button(self):
        return self.get_clickable_element(self.INVITE_FRIENDS_BUTTON)

    def get_game(self):
        el = self.get_elements_by_path(self.GAME_BUTTON)[0]
        return el
        #return self.get_clickable_element_by_element(el)

    def get_user_avatar(self):
        return self.get_clickable_element(self.USER_AVATAR)

    def get_choose_user(self):
        return self.get_clickable_element(self.CHOOSE_USER)

    def get_confirm_user(self):
        return self.get_clickable_element(self.CONFIRM_CHOICE)