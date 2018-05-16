from components.base_component import BaseComponent


class FriendsList(BaseComponent):
    MESSAGE_DIALOG = "//i[@class='tico_img ic ic_message']"

    def get_message_dialog_button(self):
        return self.get_clickable_element(self.MESSAGE_DIALOG)
