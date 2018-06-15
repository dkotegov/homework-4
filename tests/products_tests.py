# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import CatalogPage
from tests.common import get_driver, Auth, Main, Shop, Catalog, Product


class ProductsTests(unittest.TestCase):
    PRODUCT_NAME = u'Товар'
    PRODUCT_OUT_OF_STOCK = u'Нет в наличии'
    PRODUCT_PRICE = 100

    def setUp(self):
        self.driver = get_driver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        self.shop = Shop(self.driver)
        self.shop.create()

        self.catalog = Catalog(self.driver)
        self.catalog.create()
        self.catalog.open()

    def tearDown(self):
        self.shop.remove()
        self.driver.quit()

    def test_add_product(self, name=PRODUCT_NAME, price=PRODUCT_PRICE, index=0):
        product = Product(self.driver)
        product.create(name, price)

        product_name = product.get_name()
        self.assertEqual(name, product_name)

        product_price = product.get_price()
        self.assertEqual(price, product_price)

        actual_number_of_products = self.catalog.get_number_of_products()
        expected_number_of_products = index + 1
        self.assertEqual(expected_number_of_products, actual_number_of_products)

    def test_add_several_products(self):
        NUMBER_OF_PRODUCTS = 10
        for i in xrange(NUMBER_OF_PRODUCTS):
            product_name = str(i)
            product_price = self.PRODUCT_PRICE + i
            self.test_add_product(product_name, product_price, i)

    def test_add_remove_one_product(self):
        number_of_products = self.catalog.get_number_of_products()
        self.assertEqual(0, number_of_products)

        product = Product(self.driver)
        product.create()

        number_of_products = self.catalog.get_number_of_products()
        self.assertEqual(1, number_of_products)

        product.remove()

        number_of_products = self.catalog.get_number_of_products()
        self.assertEqual(0, number_of_products)

    def test_mark_product_as_out_of_stock_and_return_on_sale(self):
        product = Product(self.driver)
        product.create(self.PRODUCT_NAME, self.PRODUCT_PRICE)

        product_price = product.get_price()
        self.assertEqual(self.PRODUCT_PRICE, product_price)

        product.mark_as_out_of_stock()

        product_price_text = product.get_price_text()
        self.assertEqual(self.PRODUCT_OUT_OF_STOCK, product_price_text)

        product.return_on_sale()

        product_price = product.get_price()
        self.assertEqual(self.PRODUCT_PRICE, product_price)

    def test_pin_unpin_product(self):
        NAMES = {
            0: '0',
            1: '1',
            2: '2',
            3: '3',
        }

        Product(self.driver).create(NAMES[0])

        catalog_page = CatalogPage(self.driver)
        first_product_widget_on_panel = catalog_page.product_widget

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(NAMES[0], first_product_name_on_panel)

        pined_product = Product(self.driver)
        pined_product.create(NAMES[1])
        pined_product.pin()

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(NAMES[1], first_product_name_on_panel)

        Product(self.driver).create(NAMES[2])

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(NAMES[1], first_product_name_on_panel)

        pined_product.unpin()

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(NAMES[1], first_product_name_on_panel)

        Product(self.driver).create(NAMES[3])

        first_product_name_on_panel = first_product_widget_on_panel.get_name()
        self.assertEqual(NAMES[3], first_product_name_on_panel)
