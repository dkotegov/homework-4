# -*- coding: utf-8 -*-
import unittest

from PageObjects.page_objects import ShopMarketPage
from tests.common import getDriver, Auth, Main, Shop


class ProductTests(unittest.TestCase):
    PRODUCT_NAME = u'Товар'
    PRODUCT_PRICE = '100'
    PRODUCT_ABOUT = u'Описание товара'

    def setUp(self):
        self.driver = getDriver()

        Auth(self.driver).sign_in()
        Main(self.driver).open_groups_page()
        Shop(self.driver).create()

    def tearDown(self):
        Shop(self.driver).remove()
        self.driver.quit()

    def test_create_product(self):
        shop_market_page = ShopMarketPage(self.driver)
        product_popup = shop_market_page.product_popup

        product_popup.open_popup()
        product_popup.waiting_product_catalog()
        product_popup.set_product_name(self.PRODUCT_NAME)
        product_popup.set_product_price(self.PRODUCT_PRICE)
        product_popup.set_product_about(self.PRODUCT_ABOUT)
        product_popup.submit()
        product_popup.waiting_until_close()
