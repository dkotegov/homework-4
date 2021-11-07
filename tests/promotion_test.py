from helpers import Test

from pages import PromotionPage, ProductPage, CreateProductPage

import time


class PromotionTest(Test):
    def setUp(self):
        super().setUp()
        self.promote = PromotionPage(driver=self.driver)
        self.promote.open()
        self.promote.login.auth()
        self.createProduct()

    def createProduct(self):
        """Создание продукта для того, чтобы попасть на страницу продвижения"""
        #     Мы используем яндекс апи для карт и оно работает иногда не стабильно, из-за чего тест может падать
        create_product = CreateProductPage(driver=self.driver)
        create_product.open()

        name = "aaa"
        price = "111"
        description = "aaaaaaaaaaaaaaaaaaaaaaa"
        address = "Сант-Петербург, Россия"

        create_product.form.input_name_value(name)
        create_product.form.input_price_value(price)
        create_product.form.input_description_value(description)
        create_product.form.upload_photo("./assets/test.jpg")
        create_product.form.input_address_value(address)
        create_product.form.enter_address()

        create_product.form.enter_submit()
        time.sleep(1)

    def testErrorSubmit(self):
        """Проверка перехода без выбора тарифа"""

        self.promote.form.enter_purchase()

        self.assertTrue(self.promote.form.get_purchase_error(), "Выберите какой-нибудь тариф")

    def testBaseTariffChecked(self):
        """Проверка выбора тарифа базового"""
        self.promote.form.enter_base_tariff()

        self.assertTrue(self.promote.form.is_base_checked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Нет ошибки")

    def testImprovedTariffChecked(self):
        """Проверка выбора тарифа улучшенного"""
        self.promote.form.enter_improved_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_checked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Нет ошибки")

    def testAdvancedTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.promote.form.enter_advanced_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_checked(), "Нет ошибки")

    def testNoTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.promote.form.enter_no_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Нет ошибки")

    def testNoTariffRedirect(self):
        """Проверка, что при выборе без продвижения редиректит на страницу товара"""
        product = ProductPage(driver=self.driver)

        self.promote.form.enter_no_tariff()
        self.promote.form.enter_purchase()

        product.wait_page()
        url = self.driver.current_url
        product_id = self.driver.current_url.split('/')[-1]
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница продукта")

