from src.components.base_element import BaseElement


class FriendProfileElement(BaseElement):

    XPATH_MAKE_GIFT_ICO = '//i[@class="tico_img ic ic_present"]'

    def get_make_gift_ico(self):
        return self.get_button_by_xpath(self.XPATH_MAKE_GIFT_ICO)
