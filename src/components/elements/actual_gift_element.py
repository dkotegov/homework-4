from src.components.base_element import BaseElement


class ActualGiftElement(BaseElement):

    GIFTS_MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st._aid=NavMenu_User_Presents"]' \
                                '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    def __init__(self, driver):
        super(ActualGiftElement, self).__init__(driver)

    def is_marked(self):
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)
