# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopMarketPage, CatalogPage
from tests.common import getDriver, Auth, Main, Shop


class CatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'
    OTHER_CATALOG_NAME = u'Другой Каталог'
    CATALOG_IMAGE = 'catalog-icon.png'
    CHARS_IN_SUBSTRING = 83

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_create_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.upload_catalog_image(self.CATALOG_IMAGE)
        catalog_popup.waiting_until_image_upload()
        upload_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        catalog_widget = shop_market_page.catalog_widget()
        catalog_name = catalog_widget.get_catalog_name()
        self.assertEqual(self.CATALOG_NAME, catalog_name)

        number_of_products = catalog_widget.get_number_of_products()
        self.assertEqual(u'0', number_of_products)

        current_image_src = catalog_widget.get_image_src()
        self.assertEqual(upload_image_src[:self.CHARS_IN_SUBSTRING], current_image_src[:self.CHARS_IN_SUBSTRING])

    def test_edit_catalog(self):
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        catalog_widget = shop_market_page.catalog_widget()
        catalog_widget.open_catalog()

        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_name_before_edit = catalog_panel.get_catalog_name()
        self.assertEquals(self.CATALOG_NAME, catalog_name_before_edit)

        catalog_panel.edit_catalog()
        catalog_popup.set_catalog_name(self.OTHER_CATALOG_NAME)
        catalog_popup.upload_catalog_image(self.CATALOG_IMAGE)
        catalog_popup.waiting_until_image_upload()
        upload_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        catalog_name_after_edit = catalog_panel.get_catalog_name()
        self.assertEquals(self.OTHER_CATALOG_NAME, catalog_name_after_edit)

        current_image_src = catalog_panel.get_image_src()
        self.assertEqual(upload_image_src[:self.CHARS_IN_SUBSTRING], current_image_src[:self.CHARS_IN_SUBSTRING])
