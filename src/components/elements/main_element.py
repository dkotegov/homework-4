from src.components.base_element import BaseElement


class MainElement(BaseElement):

    GIFTS_BUTTON = '//a[@data-l="t,giftsFront"]'

    def get_gifts_button(self):
        return self.get_button_by_xpath(self.GIFTS_BUTTON)
