from components.base_component import BaseComponent


class GameForm(BaseComponent):
    GAME_DELETE = "//i[@class='tico_img ic ic_delete']"
    GAME_DELETE_REPEAD = "//input[@id='hook_FormButton_button_leave']"
    GAME_INVITE = "//i[@class='tico_img ic ic_group']"
    GAME_INVITE_NAME_FRIEND = "//div[@class='leftCardName ellip' and text()='"

    def game_delete(self): 
        return self.get_clickable_element(self.GAME_DELETE)

    def game_delete_repead(self): 
        return self.get_clickable_element(self.GAME_DELETE_REPEAD)

    def game_invite(self): 
        return self.get_clickable_element(self.GAME_INVITE)

    def game_invite_name_friend(self, name): 
        return self.get_clickable_element(self.GAME_INVITE_NAME_FRIEND + name + "']")