# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopMarketPage, CatalogPage
from tests.common import getDriver, Auth, Main, Shop


class EditCatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'
    CHARS_IN_SUBSTRING = 83

    def setUp(self):
        self.driver = getDriver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_edit_catalog_name(self):
        # creating catalog
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup_from_catalog_panel()
        catalog_popup.set_catalog_name(self.CATALOG_NAME)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check name before
        catalog_widget = shop_market_page.catalog_widget
        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        catalog_name_before_edit = catalog_panel.get_catalog_name()
        self.assertEquals(self.CATALOG_NAME, catalog_name_before_edit)

        # editing catalog name
        other_catalog_name = u'Другой каталог'

        catalog_panel.edit_catalog()
        catalog_popup.set_catalog_name(other_catalog_name)
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check name after
        catalog_name_after_edit = catalog_panel.get_catalog_name()
        self.assertEquals(other_catalog_name, catalog_name_after_edit)

    def test_upload_image_after_creating_catalog(self):
        # creating catalog without image
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup_from_catalog_panel()
        catalog_popup.set_catalog_name()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check image stub
        catalog_widget = shop_market_page.catalog_widget
        is_exist_image_stub_on_widget = catalog_widget.is_exist_image_stub()
        self.assertTrue(is_exist_image_stub_on_widget)

        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        is_exist_image_stub_on_panel = catalog_panel.is_exist_image_stub()
        self.assertTrue(is_exist_image_stub_on_panel)

        # editing catalog
        catalog_panel.edit_catalog()
        catalog_popup.upload_catalog_image()
        catalog_popup.waiting_until_image_upload()
        upload_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check upload image
        panel_image_src = catalog_panel.get_image_src()
        self.assertEqual(upload_image_src[:self.CHARS_IN_SUBSTRING], panel_image_src[:self.CHARS_IN_SUBSTRING])

    def test_edit_catalog_image(self):
        # creating catalog with image
        shop_market_page = ShopMarketPage(self.driver)
        catalog_popup = shop_market_page.catalog_popup
        catalog_popup.open_popup_from_catalog_panel()
        catalog_popup.set_catalog_name()
        catalog_popup.upload_catalog_image('image_64x64.jpg')
        catalog_popup.waiting_until_image_upload()
        creating_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check image
        catalog_widget = shop_market_page.catalog_widget
        widget_creating_image_src = catalog_widget.get_image_src()
        self.assertEqual(creating_image_src[:self.CHARS_IN_SUBSTRING], widget_creating_image_src[:self.CHARS_IN_SUBSTRING])

        catalog_widget.open_catalog()
        catalog_page = CatalogPage(self.driver)
        catalog_panel = catalog_page.catalog_panel

        panel_creating_image_src = catalog_panel.get_image_src()
        self.assertEqual(creating_image_src[:self.CHARS_IN_SUBSTRING], panel_creating_image_src[:self.CHARS_IN_SUBSTRING])

        # editing catalog
        catalog_panel.edit_catalog()
        catalog_popup.upload_catalog_image('image_512x512.jpg')
        catalog_popup.waiting_until_image_upload()
        editing_image_src = catalog_popup.get_image_src()
        catalog_popup.save()
        catalog_popup.waiting_until_close()

        # check upload image
        panel_editing_image_src = catalog_panel.get_image_src()
        self.assertEqual(editing_image_src[:self.CHARS_IN_SUBSTRING], panel_editing_image_src[:self.CHARS_IN_SUBSTRING])