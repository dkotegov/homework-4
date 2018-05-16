# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopMarketPage, CatalogPage
from tests.common import getDriver, Auth, Main, Shop


class CatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'
    OTHER_CATALOG_NAME = u'Другой Каталог'
    CATALOG_ICON = 'catalog-icon.png'

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()

        Shop(self.driver).create()

    def tearDown(self):
        # TODO Element <a ...> is not clickable
        import time; time.sleep(1)

        Shop(self.driver).remove()
        self.driver.quit()

    def test_create_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.upload_icon(self.CATALOG_ICON)
        catalog_popup.save()

        catalog_widget = shop_market_page.catalog_widget()
        catalog_name = catalog_widget.get_catalog_name()
        number_of_products = catalog_widget.get_number_of_products()

        self.assertEqual(self.CATALOG_NAME, catalog_name)
        self.assertEqual(u'0', number_of_products)

    def test_edit_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.save()

        catalog_widget = shop_market_page.catalog_widget()
        catalog_widget.open_catalog()

        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_name_before_edit = catalog_panel.get_catalog_name()
        self.assertEquals(self.CATALOG_NAME, catalog_name_before_edit)

        catalog_panel.edit_catalog()
        catalog_popup.set_catalog_name(self.OTHER_CATALOG_NAME)
        # catalog_popup.upload_icon(self.CATALOG_ICON)
        catalog_popup.save()

        catalog_name_after_edit = catalog_panel.get_catalog_name()
        self.assertEquals(self.OTHER_CATALOG_NAME, catalog_name_after_edit)
