from urllib.parse import urlparse

from consts import TEST_PRODUCT
from helpers import Test

from pages import PromotionPage, ProductPage, MainPage

# Для продвижения мы используем ЮMoney, поэтому не можем протестировать его работу
# Мы тестируем страницу без самого продвижения


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

        self.promote.form.enter_submit()

        self.assertTrue(self.promote.form.is_submit_error(), "Нет ошибки выбора тарифа")

    def testBaseTariffChecked(self):
        """Проверка выбора тарифа базового"""
        self.__open_page__()

        self.promote.form.enter_advanced_tariff()
        self.promote.form.enter_base_tariff()

        self.assertTrue(self.promote.form.is_base_checked(), "Нет выделения тарифа")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Есть выделение тарифа")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Есть выделение тарифа")

    def testImprovedTariffChecked(self):
        """Проверка выбора тарифа улучшенного"""
        self.__open_page__()

        self.promote.form.enter_base_tariff()
        self.promote.form.enter_improved_tariff()

        self.assertTrue(self.promote.form.is_improved_checked(), "Нет выделения тарифа")
        self.assertTrue(self.promote.form.is_base_unchecked(), "Есть выделение тарифа")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Есть выделение тарифа")

    def testAdvancedTariffChecked(self):
        """Проверка выбора тарифа продвинутого"""
        self.__open_page__()

        self.promote.form.enter_improved_tariff()
        self.promote.form.enter_advanced_tariff()

        self.assertTrue(self.promote.form.is_advanced_checked(), "Нет выделения тарифа")
        self.assertTrue(self.promote.form.is_base_unchecked(), "Есть выделение тарифа")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Есть выделение тарифа")

    def testNoTariffChecked(self):
        """Проверка без выбора тарифа"""
        self.__open_page__()

        self.promote.form.enter_base_tariff()
        self.promote.form.enter_no_tariff()

        self.assertTrue(self.promote.form.is_base_unchecked(), "Есть выделение тарифа")
        self.assertTrue(self.promote.form.is_improved_unchecked(), "Есть выделение тарифа")
        self.assertTrue(self.promote.form.is_advanced_unchecked(), "Есть выделение тарифа")

    def testNoTariffRedirect(self):
        """Проверка, что при выборе без продвижения редиректит на страницу товара"""
        product = ProductPage(driver=self.driver)

        self.__open_page__()

        self.promote.form.enter_no_tariff()
        self.promote.form.enter_submit()

        product.wait_page()
        url = self.driver.current_url
        product.change_path(TEST_PRODUCT)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница продукта")

    def testTariffRedirect(self):
        """Проверка, что при выборе продвижения редиректит на страницу юmoney"""
        money_domain = "yoomoney.ru"

        self.__open_page__()

        self.promote.form.enter_base_tariff()
        self.promote.form.enter_submit()

        url = self.driver.current_url
        domain = urlparse(url).netloc
        self.assertEqual(domain, money_domain, "Не открылась страница оплаты")

