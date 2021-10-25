import time
import unittest
from selenium import webdriver
from pages.all_seller_products import AllSellerProductsPage
from pages.login import LoginPage
from pages.product import ProductPage


class AllSellerProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.all_seller_products = AllSellerProductsPage(driver=self.driver)
        self.all_seller_products.open()

    def testOpenProductPage(self):
        """Открытие страницы товара при нажатии на товар"""
        self.product = ProductPage(driver=self.driver)
        self.all_seller_products.clickProduct()
        self.assertTrue(self.product.page_exist(),
                        "Не удалось открыть товар")

    def testLikeNotAuth(self):
        """Для неавторизованного пользователя: Ошибка лайка товара при нажатии кнопку \"лайк\""""
        self.login = LoginPage(driver=self.driver)
        self.all_seller_products.likeProduct()
        self.assertEqual(
            self.login.get_title(),
            "Вход",
            "Не появляется панель логина")

    def testLikAuth(self):
        """ Лайк товара при нажатии кнопку \"лайк\"
            Снятие лайка с товара при нажатии кнопки \"дизлайк\"
        """
        self.login = LoginPage(driver=self.driver)
        self.login.auth()
        self.all_seller_products.open()
        index = self.all_seller_products.likeProduct()
        res = self.all_seller_products.checkLikeProduct(index)
        self.assertTrue(res,
                        "Не удалось поставить лайка")
        self.all_seller_products.removeLikeProduct(index)
        res = self.all_seller_products.checkRemovedLikeProduct(index)
        self.assertFalse(res,
                         "Не удалось убрать лайк")

    def tearDown(self):
        self.driver.close()
