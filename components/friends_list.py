from components.base_component import BaseComponent


class FriendsList(BaseComponent):
    MESSAGE_DIALOG = "//i[@class='tico_img ic ic_message']"
    PATH_FOR_NAME_FRIEND = "//div[@class='ellip']/a[@hrev="

    def get_message_dialog_button(self):
        return self.get_clickable_element(self.MESSAGE_DIALOG)

    def find_friend_with_url(self, url):
        return self.driver.find_element_by_xpath(self.PATH_FOR_NAME_FRIEND + "'" + url + "']")
