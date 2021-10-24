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

    def tearDown(self):
        self.driver.close()
