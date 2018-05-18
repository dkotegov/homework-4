from components.base_component import BaseComponent


class GameForm(BaseComponent):
    GAME_DELETE = "//i[@class='tico_img ic ic_delete']"
    GAME_DELETE_REPEAD = "//input[@id='hook_FormButton_button_leave']"

    def game_delete(self): 
        return self.get_clickable_element(self.GAME_DELETE)

    def game_delete_repead(self): 
        return self.get_clickable_element(self.GAME_DELETE_REPEAD)

