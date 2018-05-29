# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopFeedPage
from tests.common import get_driver, Auth, Shop, Main


class CreateShopTest(unittest.TestCase):
    SHOP_NAME = u'Ларек-Марек'
    SHOP_CATEGORY = u'Страница, Игры'

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test(self):
        shop = Shop(self.driver)
        shop.create(self.SHOP_NAME)

        shop.open_feed_page()

        header = ShopFeedPage(self.driver).header

        shop_name = header.get_shop_name()
        shop_category = header.get_shop_category()

        self.assertEqual(self.SHOP_NAME, shop_name)
        self.assertEqual(self.SHOP_CATEGORY, shop_category)
