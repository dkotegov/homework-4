from components.base_component import BaseComponent


class BlackList(BaseComponent):

    DELETE_BUTTON = "//div[@class='ic12 ic12_close-w']"
    CONFIRM_BUTTON = "//input[@class='button-pro form-actions_yes']"

    def get_delete_button(self):
        return self.get_clickable_element(self.DELETE_BUTTON)

    def get_confirm_button(self):
        return self.get_clickable_element(self.CONFIRM_BUTTON)