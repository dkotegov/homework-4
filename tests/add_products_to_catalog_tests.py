# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import CatalogPage
from tests.common import get_driver, Auth, Main, Shop, Catalog, Product


class AddProductsToCatalogTests(unittest.TestCase):
    PRODUCT_NAME = u'Товар'

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

        catalog = Catalog(self.driver)
        catalog.create()
        catalog.open()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_add_one_product(self):
        Product(self.driver).create(self.PRODUCT_NAME)

        catalog_page = CatalogPage(self.driver)
        product_widget = catalog_page.product_widget

        product_name = product_widget.get_product_name()
        self.assertEqual(self.PRODUCT_NAME, product_name)

        number_of_products = catalog_page.catalog_panel.get_number_of_products()
        self.assertEqual(1, number_of_products)

    def test_add_several_products(self):
        number_of_products = 100

        for i in xrange(number_of_products):
            product_name = str(i)
            Product(self.driver).create(product_name)
