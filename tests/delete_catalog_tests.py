# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopMarketPage
from tests.common import get_driver, Auth, Main, Shop, Catalog


class DeleteCatalogTests(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_delete_empty_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)

        # check stub
        catalog_stub = shop_market_page.catalog_stub
        is_exist_catalog_stub = catalog_stub.is_exist_catalog_stub()
        self.assertTrue(is_exist_catalog_stub)

        catalog = Catalog(self.driver)
        catalog.create()

        # check widget
        catalog_widget = shop_market_page.catalog_widget
        is_exist_catalog_widget = catalog_widget.is_exist_catalog_widget()
        self.assertTrue(is_exist_catalog_widget)

        # check counter
        catalog_counter = shop_market_page.catalog_counter
        number_of_catalogs = catalog_counter.get_number_of_catalogs()
        self.assertEqual(1, number_of_catalogs)

        catalog.remove()

        # check stub
        is_exist_catalog_stub = catalog_stub.is_exist_catalog_stub()
        self.assertTrue(is_exist_catalog_stub)

        # check counter
        is_not_exist_counter = catalog_counter.is_not_exist_counter()
        self.assertTrue(is_not_exist_counter)
