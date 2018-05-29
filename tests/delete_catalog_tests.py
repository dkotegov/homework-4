# -*- coding: utf-8 -*-
import unittest

from Components.market_page_components import RemoveCatalogPopup
from PageObjects.page_objects import ShopMarketPage, CatalogPage
from tests.common import get_driver, Auth, Main, Shop


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
        # check stub
        shop_market_page = ShopMarketPage(self.driver)
        catalog_stub = shop_market_page.catalog_stub
        self.check_catalog_stub(catalog_stub)

        # creating catalog
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup_from_catalog_panel()
        catalog_popup.set_catalog_name()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check widget
        catalog_widget = shop_market_page.catalog_widget
        self.check_catalog_widget(catalog_widget)

        # removing catalog
        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_panel.remove_catalog()
        remove_catalog_popup = RemoveCatalogPopup(self.driver)
        remove_catalog_popup.submit_remove()
        remove_catalog_popup.waiting_until_close()

        # check stub
        self.check_catalog_stub(catalog_stub)

    def check_catalog_stub(self, catalog_stub):
        is_exist_catalog_stub = catalog_stub.is_exist_catalog_stub()
        self.assertTrue(is_exist_catalog_stub)

    def check_catalog_widget(self, catalog_widget):
        is_exist_catalog_widget = catalog_widget.is_exist_catalog_widget()
        self.assertTrue(is_exist_catalog_widget)