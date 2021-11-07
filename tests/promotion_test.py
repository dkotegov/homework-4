from consts import TEST_PRODUCT
from helpers import Test

from pages import PromotionPage, ProductPage, MainPage


class PromotionTest(Test):
    def setUp(self):
        super().setUp()
        self.promote = PromotionPage(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        main_page.open()
        main_page.login.auth()

    def __open_page__(self):
        self.promote.send_state(TEST_PRODUCT)
        self.promote.refresh()

    def testErrorSubmit(self):
        """Проверка перехода без выбора тарифа"""
        self.__open_page__()

        self.promote.form.enter_purchase()

        self.assertTrue(self.promote.form.get_purchase_error(), "Выберите какой-нибудь тариф")

    def testBaseTariffChecked(self):
        """Проверка выбора тарифа базового"""
        self.__open_page__()

        self.promote.form.enter_base_tariff()

        self.assertTrue(self.promote.form.is_base_checked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Нет ошибки")

    def testImprovedTariffChecked(self):
        """Проверка выбора тарифа улучшенного"""
        self.__open_page__()

        self.promote.form.enter_improved_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_checked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Нет ошибки")

    def testAdvancedTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.__open_page__()

        self.promote.form.enter_advanced_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_checked(), "Нет ошибки")

    def testNoTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.__open_page__()

        self.promote.form.enter_no_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Нет ошибки")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Нет ошибки")

    def testNoTariffRedirect(self):
        """Проверка, что при выборе без продвижения редиректит на страницу товара"""
        product = ProductPage(driver=self.driver)

        self.__open_page__()

        self.promote.form.enter_no_tariff()
        self.promote.form.enter_purchase()

        product.wait_page()
        url = self.driver.current_url
        product.change_path(TEST_PRODUCT)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница продукта")

