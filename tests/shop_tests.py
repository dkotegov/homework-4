# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopAdminPage, GroupsPage
from tests.common import getDriver, Auth, Groups


class ShopTests(unittest.TestCase):
    SHOP_NAME = u'Ларек-Марек'

    def setUp(self):
        self.driver = getDriver()

        auth = Auth(self.driver)
        auth.auth()

        groups = Groups(self.driver)
        groups.open_groups_page()

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
