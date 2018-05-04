# -*- coding: utf-8 -*-

import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait
from common_page_objects import Page, Commons, Component


class GroupsPage(Page):
    @property
    def popup(self):
        return Popup(self.driver)


class ShopAdminPage(Page):
    @property
    def top_menu(self):
        return TopMenu(self.driver)

    @property
    def shop_main_page(self):
        return ShopPage(self.driver)


class Popup(Component):
    CREATE_GROUP = '//div[@class="create-group"]//a'
    CREATE_SHOP = '//a[contains(@href,"SHOP")]'

    SHOP_NAME = '//input[@id="field_name"]'
    GAMES_SUBCATEGORY = '//select[@id="field_pageMixedCategory"]/option[@value="subcatVal12006"]'
    SUBMIT = '//input[@id="hook_FormButton_button_create"]'

    def open_popup(self):
        create_groups_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_GROUP)
        )
        create_groups_button.click()

    def create_shop(self):
        create_shop_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CREATE_SHOP)
        )
        create_shop_button.click()

    def set_shop_name(self, shop_name):
        shop_name_input = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SHOP_NAME)
        )
        shop_name_input.send_keys(shop_name)

    def set_subcategory(self):
        games_option = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.GAMES_SUBCATEGORY)
        )
        games_option.click()

    def submit_creation(self):
        submit_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT)
        )
        submit_button.click()


class TopMenu(Component):
    OPEN_SHOP_PAGE_LINK = '//div[contains(@class,"mctc_navMenu")]/a[contains(@hrefattrs,"altGroupMain")]'

    def open_shop_page(self):
        open_shop_link = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OPEN_SHOP_PAGE_LINK)
        )
        open_shop_link.click()


class ShopPage(Component):
    OTHER_ACTIONS_BUTTON = '//em[@class="tico_simb_txt"]'
    REMOVE_SHOP_BUTTON = '//a[contains(@hrefattrs,"RemoveAltGroup")]'
    SUBMIT_REMOVE_BUTTON = '//input[@name="button_delete"]'

    def other_actions(self):
        other_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.OTHER_ACTIONS_BUTTON)
        )
        other_button.click()

    def remove_shop(self):
        remove_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.REMOVE_SHOP_BUTTON)
        )
        remove_button.click()

    def submit_remove(self):
        submit_button = WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.SUBMIT_REMOVE_BUTTON)
        )
        submit_button.click()


class ShopTests(unittest.TestCase):
    SHOP_NAME = u'Ларек-Марек'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        commons = Commons(self.driver)
        commons.auth()
        commons.open_groups_page()

    def tearDown(self):
        shop_admin_page = ShopAdminPage(self.driver)
        top_menu = shop_admin_page.top_menu
        top_menu.open_shop_page()

        shop_page = shop_admin_page.shop_main_page
        shop_page.other_actions()
        shop_page.remove_shop()
        shop_page.submit_remove()

        self.driver.quit()

    def test(self):
        group_page = GroupsPage(self.driver)
        popup = group_page.popup
        popup.open_popup()

        popup.create_shop()

        popup.set_shop_name(self.SHOP_NAME)
        popup.set_subcategory()
        popup.submit_creation()
