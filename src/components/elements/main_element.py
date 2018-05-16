from src.components.base_element import BaseElement


class MainElement(BaseElement):

    MESSAGE_BUTTON = '//div[@id="msg_toolbar_button"]'
    NEW_MESSAGE_TEXT_IN_NOTIFICATION = '//div[contains(@data-l, "lastMessage")]/div[1]'
    GIFTS_BUTTON = '//a[@data-l="t,giftsFront"]'

    NAV_SIDE = '//div[@class="nav-side __navigation"]'

    def get_message_button(self):
        return self.get_button_by_xpath(self.MESSAGE_BUTTON)

    def get_gifts_button(self):
        return self.get_button_by_xpath(self.GIFTS_BUTTON)

    def is_exist_nav_side(self):
        return self.existence_of_element_by_xpath(self.NAV_SIDE)
