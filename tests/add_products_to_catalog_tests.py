# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import CatalogPage
from tests.common import get_driver, Auth, Main, Shop, Catalog, Product


class AddProductsToCatalogTests(unittest.TestCase):
    PRODUCT_NAME = u'Товар'
    PRODUCT_PRICE = 100

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

    def test_add_product(self, name=PRODUCT_NAME, price=PRODUCT_PRICE, index=0):
        Product(self.driver).create(name, price)

        catalog_page = CatalogPage(self.driver)
        product_widget = catalog_page.product_widget

        product_name = product_widget.get_name()
        self.assertEqual(name, product_name)

        product_price = product_widget.get_price()
        self.assertEqual(price, product_price)

        actual_number_of_products = catalog_page.catalog_panel.get_number_of_products()
        expected_number_of_products = index + 1
        self.assertEqual(expected_number_of_products, actual_number_of_products)

    def test_add_several_products(self):
        number_of_products = 25

        for i in xrange(number_of_products):
            product_name = str(i)
            product_price = self.PRODUCT_PRICE + i
            self.test_add_product(product_name, product_price, i)
