import unittest
from selenium import webdriver
from pages.all_seller_products import AllSellerProductsPage
from pages.login import LoginPage
from pages.massage import MassagePage
from pages.product import ProductPage


class ProductTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.product = ProductPage(driver=self.driver)
        self.product.open()

    def testFirstImgSrcEqualPreview(self):
        """Проверить, что при открытии страницы первая картинка слайдера совпадает с превью товара"""
        self.assertEqual(
            self.product.selected_img_src_from_slider(),
            self.product.preview_img_src(),
            "Первая картинка слайдера не совпадает с превью товара")

    def testChangePreview(self):
        """Проверить, что по нажатию на картинку из слайдера изменяется превью товара"""
        self.product.click_different_preview()
        self.assertEqual(
            self.product.selected_img_src_from_slider(),
            self.product.preview_img_src(),
            "Выбранная картинка слайдера не совпадает с превью товара")

    def testOpenAllItemsBySellerName(self):
        """Успешный редирект на страницу всех объявлений при нажатии на имя"""
        self.all_items = AllSellerProductsPage(driver=self.driver)
        self.product.click_on_seller_name()
        self.assertEqual(
            self.all_items.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerImg(self):
        """Успешный редирект на страницу всех объявлений при нажатии на фото"""
        self.all_items = AllSellerProductsPage(driver=self.driver)
        self.product.click_on_seller_img()
        self.assertEqual(
            self.all_items.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerRate(self):
        """Успешный редирект на страницу всех объявлений при нажатии на оценку"""
        self.all_items = AllSellerProductsPage(driver=self.driver)
        self.product.click_on_seller_rate()
        self.assertEqual(
            self.all_items.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testFailToShowPhoneNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к телефону при нажатии на кнопку "Показать номер\""""
        self.login = LoginPage(driver=self.driver)
        self.product.click_phone()
        self.assertEqual(
            self.login.get_title(),
            "Вход",
            "Не появляется панель логина")

    def tesToShowPhoneAuth(self):
        """Проверить изменение текста на кнопке "Показать номер" на номер телефона при нажатии на кнопку "Показать
        номер" у автора с действительным номером телефона """
        self.login = LoginPage(driver=self.driver)
        self.login.auth()
        self.product.open()
        self.product.click_phone()
        self.assertRegex(
            self.product.get_phone(),
            r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{"
            r"4}|\d{3}[-\.\s]??\d{4}))",
            "Появился не номер телефона")

    def testFailToShowPhoneAuthVK(self):
        """Ошибка данных, при нажатии на кнопку "Показать номер" автора  зарегистрированного с помощью ВК, без номера
        телефона """
        self.login = LoginPage(driver=self.driver)
        self.login.auth()
        self.product.changePath("product/103")
        self.product.open()
        self.product.click_phone()
        self.assertEqual(
            self.product.get_phone(),
            "Нет телефона",
            "Появилась не надпись \"Нет телефона\"")

    def testFailToRedirectMasNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к телефону при нажатии на кнопку "Показать номер\""""
        self.login = LoginPage(driver=self.driver)
        self.product.click_massage()
        self.assertEqual(
            self.login.get_title(),
            "Вход",
            "Не появляется панель логина")

    def testToRedirectMasAuth(self):
        """Успешный редирект на страницу переписки при нажатии на кнопку \"Написать сообщение\""""
        self.login = LoginPage(driver=self.driver)
        self.login.auth()
        self.product.click_massage()
        self.massage = MassagePage(driver=self.driver)
        self.assertNotEqual(
            self.massage.get_title(),
            "",
            "Не появляется страница диалога")

    def tearDown(self):
        self.driver.close()
