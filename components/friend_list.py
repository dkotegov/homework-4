from components.base_component import BaseComponent


class FriendsList(BaseComponent):
    FRIENDS_BUTTON = "//a[@data-l='t,userFriend']"

    def open_friends_list(self):
        self.driver.find_element_by_xpath(self.FRIENDS_BUTTON).click()
