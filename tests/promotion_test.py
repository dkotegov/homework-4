import unittest
from selenium import webdriver

from pages.promotion import PromotionPage
from pages.product import ProductPage


class PromotionTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.create = PromotionPage(driver=self.driver)
        self.create.open()

    def testErrorSubmit(self):
        """Проверка перехода без выбора тарифа"""

        self.create.enter_purchase()

        self.assertTrue(self.create.get_purchase_error(), "Выберите какой-нибудь тариф")

    def testBaseTariffChecked(self):
        """Проверка выбора тарифа базового"""
        self.create.enter_base_tariff()

        self.assertTrue(self.create.is_base_checked(), "Нет ошибки")
        self.assertTrue(self.create.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.create.is_advanced_unchecked(), "Нет ошибки")

    def testImprovedTariffChecked(self):
        """Проверка выбора тарифа улучшенного"""
        self.create.enter_improved_tariff()

        self.assertTrue(self.create.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.create.is_improved_checked(), "Нет ошибки")
        self.assertTrue(self.create.is_advanced_unchecked(), "Нет ошибки")

    def testAdvancedTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.create.enter_advanced_tariff()

        self.assertTrue(self.create.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.create.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.create.is_advanced_checked(), "Нет ошибки")

    def testNoTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.create.enter_no_tariff()

        self.assertTrue(self.create.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.create.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.create.is_advanced_unchecked(), "Нет ошибки")

    def testNoTariffRedirect(self):
        """Проверка, что при выборе без продвижения редиректит на страницу товара"""
        product_id = "1"

        self.create.enter_no_tariff()

        product = ProductPage(driver=self.driver)
        self.create.enter_purchase()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница продукта")

    def tearDown(self):
        self.driver.close()
