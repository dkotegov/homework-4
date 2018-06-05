# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Shop, Main


class CreateRemoveShopTest(unittest.TestCase):
    SHOP_NAME = u'Ларек-Марек'
    SHOP_CATEGORY = u'Страница, Игры'

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()

        self.main_page = Main(self.driver)
        self.main_page.open_groups_page()

    def tearDown(self):
        self.driver.quit()

    def test_create_remove_shop(self):
        number_of_groups_before = self.get_current_number_of_groups()

        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)

        shop.open_feed_page()
        shop_name = shop.get_name()
        shop_category = shop.get_category()

        self.assertEqual(self.SHOP_NAME, shop_name)
        self.assertEqual(self.SHOP_CATEGORY, shop_category)

        shop.remove()

        number_of_groups_after = self.get_current_number_of_groups()
        self.assertEqual(number_of_groups_before, number_of_groups_after)

    def get_current_number_of_groups(self):
        are_there_any_groups = self.main_page.are_there_any_groups()
        if are_there_any_groups:
            return self.main_page.get_number_of_groups()
        else:
            return 0
