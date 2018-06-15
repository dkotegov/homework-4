# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Main, Shop, Catalog


class EditCatalogTests(unittest.TestCase):
    CATALOG_NAME = u'Каталог'
    OTHER_CATALOG_NAME = u'Другой каталог'

    def setUp(self):
        self.driver = get_driver()
        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        self.shop = Shop(self.driver)
        self.shop.create()
        self.catalog_widget = self.shop.market_page.catalog_widget

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_edit_catalog_name(self):
        catalog = Catalog(self.driver)
        catalog.create(self.CATALOG_NAME)
        catalog.open()

        catalog_name_before_edit = catalog.get_name()
        self.assertEquals(self.CATALOG_NAME, catalog_name_before_edit)

        catalog.reset_name(self.OTHER_CATALOG_NAME)

        catalog_name_after_edit = catalog.get_name()
        self.assertEquals(self.OTHER_CATALOG_NAME, catalog_name_after_edit)

    def test_upload_image_after_creating_catalog(self):
        # creating catalog without image
        catalog = Catalog(self.driver)
        catalog.create()

        # check image stub on widget
        is_exist_image_stub_on_widget = self.catalog_widget.is_exist_image_stub()
        self.assertTrue(is_exist_image_stub_on_widget)

        # check image stub on panel
        catalog_page = catalog.open()
        catalog_panel = catalog_page.catalog_panel
        is_exist_image_stub_on_panel = catalog_panel.is_exist_image_stub()
        self.assertTrue(is_exist_image_stub_on_panel)

        # upload image
        upload_image_src = catalog.set_image()

        # check upload image
        panel_image_src = catalog_panel.get_image_src()
        self.assertEqual(upload_image_src, panel_image_src)

    def test_edit_catalog_image(self):
        # creating catalog with image
        catalog = Catalog(self.driver)
        creating_image_src = catalog.create_with_image('image_64x64.jpg')

        # check image on widget
        widget_creating_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(creating_image_src, widget_creating_image_src)

        # check image on panel
        catalog_page = catalog.open()
        catalog_panel = catalog_page.catalog_panel
        panel_creating_image_src = catalog_panel.get_image_src()
        self.assertEqual(creating_image_src, panel_creating_image_src)

        # upload other image
        editing_image_src = catalog.set_image('image_512x512.jpg')

        # check upload image
        panel_editing_image_src = catalog_panel.get_image_src()
        self.assertEqual(editing_image_src, panel_editing_image_src)
