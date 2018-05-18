from src.components.base_element import BaseElement


class FriendsElement(BaseElement):

    MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=userFriend&st._aid=NavMenu_User_Friends"]' \
                          '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    XPATH_GRID = '//div[@class="portlet "]'

    def is_marked(self):
        """
        Check for the existence of marked friends item in nav bar
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.MARKED_ITEM_NAV_BAR)

    def get_grid(self):
        return self.get_field_by_xpath(self.XPATH_GRID)

    def get_friend_ico(self):
        grid = self.get_grid()
        return grid.find_element_by_class_name('photo_img')
