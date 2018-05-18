from src.components.base_element import BaseElement


class SelfGiftElement(BaseElement):

    SELF_GIFTS_MARKED_ITEM_LEFT_COLUMN = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st.cat=my"]' \
                                         '[@class="nav-side_i  __ac __with-ic"]'
    LIKE_BUTTON = '//span[@data-id1="784462592490"]'
    DIAOLOG_BUTTON = '//*[@id="hook_Block_GiftsFrontContentRBx"]/div/div[2]/div/div/div/ul/li'

    def is_marked(self):
        """
        Check for the existence of marked gifts item in left Column
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.SELF_GIFTS_MARKED_ITEM_LEFT_COLUMN)

    def get_like_button(self):
        return self.get_button_by_xpath(self.LIKE_BUTTON)

    def get_dialog_button(self):
        return self.get_button_by_xpath(self.DIAOLOG_BUTTON)

