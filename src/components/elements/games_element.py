from src.components.base_element import BaseElement


class GamesElement(BaseElement):

    MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=appsShowcaseHD&st._aid=NavMenu_User_Apps"]' \
                          '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    def is_marked(self):
        """
        Check for the existence of marked friends item in nav bar
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.MARKED_ITEM_NAV_BAR)
