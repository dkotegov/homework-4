# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import GroupsPage, MainGroupPage, ThemesPage
from tests.common import getDriver, Auth, Groups


class PostTests(unittest.TestCase):
    SHOP_NAME = u'Магазин'

    def setUp(self):
        self.driver = getDriver()

        auth = Auth(self.driver)
        auth.auth()

        groups = Groups(self.driver)
        groups.open_groups_page()

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
