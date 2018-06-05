# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import CatalogPage
from tests.common import get_driver, Auth, Main, Shop, Catalog, Product


class ProductsTests(unittest.TestCase):
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
        number_of_products = 10

        for i in xrange(number_of_products):
            product_name = str(i)
            product_price = self.PRODUCT_PRICE + i
            self.test_add_product(product_name, product_price, i)

    def test_add_remove_one_product(self):
        catalog_page = CatalogPage(self.driver)
        number_of_products = catalog_page.catalog_panel.get_number_of_products()
        self.assertEqual(0, number_of_products)

        product = Product(self.driver)
        product.create()

        number_of_products = catalog_page.catalog_panel.get_number_of_products()
        self.assertEqual(1, number_of_products)

        product.remove()

        number_of_products = catalog_page.catalog_panel.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_mark_product_as_out_of_stock_and_return_on_sale(self):
        product = Product(self.driver)
        product.create(self.PRODUCT_NAME, self.PRODUCT_PRICE)

        catalog_page = CatalogPage(self.driver)
        product_widget = catalog_page.product_widget

        product_price = product_widget.get_price()
        self.assertEqual(self.PRODUCT_PRICE, product_price)

        product.mark_as_out_of_stock()

        expected_price_text = u'Нет в наличии'
        product_price_text = product_widget.get_price_text()
        self.assertEqual(expected_price_text, product_price_text)

        product.return_on_sale()

        product_price = product_widget.get_price()
        self.assertEqual(self.PRODUCT_PRICE, product_price)

    def test_pin_unpin_product(self):
        name_of_zero_product = '0'
        name_of_first_product = '1'
        name_of_second_product = '2'
        name_of_third_product = '3'

        Product(self.driver).create(name_of_zero_product)

        catalog_page = CatalogPage(self.driver)
        first_product_widget_on_panel = catalog_page.product_widget

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(name_of_zero_product, first_product_name_on_panel)

        pined_product = Product(self.driver)
        pined_product.create(name_of_first_product)
        pined_product.pin()

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(name_of_first_product, first_product_name_on_panel)

        Product(self.driver).create(name_of_second_product)

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(name_of_first_product, first_product_name_on_panel)

        pined_product.unpin()

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(name_of_first_product, first_product_name_on_panel)

        Product(self.driver).create(name_of_third_product)

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(name_of_third_product, first_product_name_on_panel)
