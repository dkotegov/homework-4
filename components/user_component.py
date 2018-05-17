from components.base_component import BaseComponent
from selenium.common.exceptions import NoSuchElementException



class UserForm(BaseComponent):
    BUTTON_REQUEST_SENT = "//span[@class='dropdown_ac button-pro __sec __with-arrow']"
    BUTTON_ADD_TO_FRIENDS = "//span[@class='dropdown_ac button-pro __wide']"
    BUTTON_ACCEPT_FRIEND_REQUEST = "//a[@class='dropdown_ac button-pro']"
    BUTTON_FRIENDS = "//span[@class='dropdown_ac button-pro __sec __with-arrow']"

    def sent_request_add_to_friends(self):
        return self.driver.find_element_by_xpath(self.BUTTON_ADD_TO_FRIENDS)

    def accept_friend_request(self):
        return self.driver.find_element_by_xpath(self.BUTTON_ACCEPT_FRIEND_REQUEST)

    def is_friend(self):
        try:
            self.driver.find_element_by_xpath(self.BUTTON_FRIENDS)
            return True
        except NoSuchElementException:
            return False



