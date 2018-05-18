from components.base_component import BaseComponent


class FriendsList(BaseComponent):
    MESSAGE_DIALOG = "//i[@class='tico_img ic ic_message']"
    SUBSCRIBERS_LIST = "//a[@class='nav-side_i  __ac' and @href='"
    SUBSCRIPTIONS_LIST = "//a[@class='nav-side_i' and @href='"


    def get_message_dialog_button(self):
        return self.get_clickable_element(self.MESSAGE_DIALOG)

    def subscribers_list(self, url):
    	return self.get_clickable_element(self.SUBSCRIBERS_LIST + url + "'/subscribers]")

    def subscriptions_list(self, url):
    	return self.get_clickable_element(self.SUBSCRIPTIONS_LIST + url + "/subscriptions']")