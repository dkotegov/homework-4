from src.components.base_element import BaseElement


class GiftElement(BaseElement):

    GIFTS_MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st._aid=NavMenu_User_Presents"]' \
                                '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    LOGO = '//div[@id="topPanelLeftCorner"]'

    def is_marked(self):
        """
        Check for the existence of marked gifts item in nav bar
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)

    def get_logo(self):
        return self.get_button_by_xpath(self.LOGO)

