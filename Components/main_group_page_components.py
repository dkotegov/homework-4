# -*- coding: utf-8 -*-
from Components.component import Component
from selenium.webdriver.support.ui import WebDriverWait

import time


class GroupTopMenu(Component):
    # Попроще сделать в формат
    THEMES_BUTTON = u'//div[contains(@class,"mctc_navMenu")]/a[contains(@hrefattrs,"altGroupForum")]'
    SHOP_MAIN_PAGE_BUTTON = u'//div[contains(@class,"mctc_navMenu")]/a[contains(@hrefattrs,"altGroupMain")]'

    def themes_page_open(self):
        themes_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.THEMES_BUTTON)
        )
        themes_button.click()

    def shop_main_page_open(self):
        # Надо придумать что с этим делать
        time.sleep(2)
        shop_main_page_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SHOP_MAIN_PAGE_BUTTON)
        )
        shop_main_page_button.click()


class ShopMainPage(Component):
    REMOVE_SHOP_BUTTON = u'//a[contains(@hrefattrs,"RemoveAltGroup")]'
    OTHER_ACTION_BUTTON = u'//span[em[contains(text(),"Другие действия")]]'
    SUBMIT_REMOVE_BUTTON = u'//input[@name="button_delete"]'

    def delete_group(self):
        (WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OTHER_ACTION_BUTTON)
        )).click()

        themes_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_SHOP_BUTTON)
        )
        themes_button.click()

        confirm_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_REMOVE_BUTTON)
        )
        confirm_button.click()