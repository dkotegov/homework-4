import unittest
from selenium import webdriver

from pages.all_seller_products import AllSellerProductsPage
from pages.login import LoginPage
from pages.product import ProductPage
from pages.search import SearchPage


class SearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.search = SearchPage(driver=self.driver)
        self.search.open()

    def testInputAmount(self):
        """Поля "Цена от, ₽" и “до”
                        Запрет ввода в поля символов отличных от цифр в блоке с фильтрами
                        Запрет ввода в поля чисел больше, чем 10 знаков в блоке с фильтрами
        """
        resGood = self.search.enterAmount("1000")
        self.assertTupleEqual(("1 000", "1 000"), resGood, "Некорректный результат")
        self.search.clearAmount()
        resBad = self.search.enterAmount("incorrect")
        self.assertTupleEqual(("", ""), resBad, "Некорректный результат")
        self.search.clearAmount()
        resBad = self.search.enterAmount("10000000000000")
        self.assertTupleEqual(("1 000 000 000", "1 000 000 000"), resBad, "Некорректный результат")

    def testOpenProductPage(self):
        """Открытие страницы товара при нажатии на товар"""
        self.product = ProductPage(driver=self.driver)
        self.search.clickProduct()
        self.assertTrue(self.product.page_exist(),
                        "Не удалось открыть товар")

    def tearDown(self):
        self.driver.close()
