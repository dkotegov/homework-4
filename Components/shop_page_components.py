# -*- coding: utf-8 -*-
from Components.component import Component


class TopMenu(Component):
    OPEN_SHOP_PAGE_LINK = '//div[contains(@class,"mctc_navMenu")]/a[contains(@hrefattrs,"altGroupMain")]'

    def open_shop_page(self):
        super(TopMenu, self).click_element(self.OPEN_SHOP_PAGE_LINK)


class ShopPage(Component):
    OTHER_ACTIONS_BUTTON = '//em[@class="tico_simb_txt"]'
    REMOVE_SHOP_BUTTON = '//a[contains(@hrefattrs,"RemoveAltGroup")]'
    SUBMIT_REMOVE_BUTTON = '//input[@name="button_delete"]'

    def other_actions(self):
        super(ShopPage, self).click_element(self.OTHER_ACTIONS_BUTTON)

    def remove_shop(self):
        super(ShopPage, self).click_element(self.REMOVE_SHOP_BUTTON)

    def submit_remove(self):
        super(ShopPage, self).click_element(self.SUBMIT_REMOVE_BUTTON)
