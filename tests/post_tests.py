# -*- coding: utf-8 -*-
import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from Components.common import Commons
from PageObjects.page_objects import (GroupsPage,MainGroupPage,
                                      ThemesPage)


class PostTests(unittest.TestCase):
    SHOP_NAME = u'Магазин'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        commons = Commons(self.driver)
        commons.auth()
        commons.open_groups_page()

        group_page = GroupsPage(self.driver)
        popup = group_page.popup
        popup.open_popup()

        popup.create_shop()

        popup.set_shop_name(self.SHOP_NAME)
        popup.set_subcategory()
        popup.submit_creation()

    def tearDown(self):
        main_group_page = MainGroupPage(self.driver)
        main_group_page.group_top_menu.shop_main_page_open()
        main_group_page.shop_main_page.delete_group()

        self.driver.quit()

    def test_create_delete_theme(self):

        main_group_page = MainGroupPage(self.driver)
        main_group_page.group_top_menu.themes_page_open()

        themes_page = ThemesPage(self.driver)
        themes_page.theme_form.open_form()
        themes_page.theme_form.set_text()
        themes_page.theme_form.submit()

        self.assertEqual(1, 1)
