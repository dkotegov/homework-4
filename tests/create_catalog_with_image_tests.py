# -*- coding: utf-8 -*-
import unittest

from tests.common import get_driver, Auth, Main, Shop, Catalog


class CreateCatalogWithImageTests(unittest.TestCase):

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

    def test_create_catalog_with_small_jpg_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_64x64.jpg')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_small_png_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_64x64.png')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_small_gif_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_64x64.gif')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_medium_jpg_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_512x512.jpg')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_medium_png_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_512x512.png')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_medium_gif_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_512x512.gif')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_large_jpg_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_4K.jpg')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_large_png_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_4K.png')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)

    def test_create_catalog_with_large_gif_image(self):
        upload_image_src = Catalog(self.driver).create_with_image('image_4K.gif')

        widget_image_src = self.catalog_widget.get_image_src()
        self.assertEqual(upload_image_src, widget_image_src)
