from components.base_component import BaseComponent


class FriendsList(BaseComponent):
    #MESSAGE_DIALOG = "//i[@class='tico_img ic ic_message']"
    MESSAGE_WITH_55_DIALOG = "//div[@class='caption']/a[@href='/messages/578592967841' and contains(@hrefattrs,'st.convId=PRIVATE_578592967841')]"
    MESSAGE_WITH_46_DIALOG = "//div[@class='caption']/a[@href='/messages/574747890819' and contains(@hrefattrs,'st.convId=PRIVATE_574747890819')]"

    def get_message_with_55_dialog_button(self):
        return self.get_clickable_element(self.MESSAGE_WITH_55_DIALOG)

    def get_message_with_46_dialog_button(self):
        return self.get_clickable_element(self.MESSAGE_WITH_46_DIALOG)
