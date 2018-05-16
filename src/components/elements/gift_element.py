from src.components.base_element import BaseElement


class GiftElement(BaseElement):
    GIFTS_MARKED_ITEM_NAV_BAR = '//a[@hrefattrs="st.cmd=giftsFront&st.or=NAV_MENU&st._aid=NavMenu_User_Presents"]' \
                                '[@class="mctc_navMenuSec mctc_navMenuActiveSec"]'

    LOGO = '//div[@id="topPanelLeftCorner"]'

    XPATH_FEED_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                               '[@hrefattrs="st.cmd=userMain&st._aid=NavMenu_User_Main"]'

    XPATH_FRIENDS_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                                  '[@hrefattrs="st.cmd=userFriend&st._aid=NavMenu_User_Friends"]'

    XPATH_PHOTO_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                                '[@hrefattrs="st.cmd=userPhotos&st._aid=NavMenu_User_Photos"]'

    XPATH_GROUPS_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                                 '[@hrefattrs="st.cmd=userAltGroup&st._aid=NavMenu_User_AltGroups"]'

    XPATH_GAMES_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                                '[@hrefattrs="st.cmd=appsShowcaseHD&st._aid=NavMenu_User_Apps"]'

    XPATH_NOTES_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                                '[@hrefattrs="st.cmd=userStatuses&st._aid=NavMenu_User_StatusHistory"]'

    XPATH_INVENTORIES_ITEM_NAV_MENU = '//a[@class="mctc_navMenuSec"]' \
                                      '[@hrefattrs="st.cmd=mall&st.section=main&st._aid=NavMenu_User_Mall"]'

    def is_marked(self):
        """
        Check for the existence of marked gifts item in nav bar
        :return: Bool
        """
        return self.existence_of_element_by_xpath(self.GIFTS_MARKED_ITEM_NAV_BAR)

    def get_logo(self):
        return self.get_button_by_xpath(self.LOGO)

    def get_feed_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_FEED_ITEM_NAV_MENU)

    def get_friends_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_FRIENDS_ITEM_NAV_MENU)

    def get_photo_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_PHOTO_ITEM_NAV_MENU)

    def get_groups_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_GROUPS_ITEM_NAV_MENU)

    def get_games_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_GAMES_ITEM_NAV_MENU)

    def get_notes_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_NOTES_ITEM_NAV_MENU)

    def get_inventories_item_nav_menu(self):
        return self.get_button_by_xpath(self.XPATH_INVENTORIES_ITEM_NAV_MENU)
