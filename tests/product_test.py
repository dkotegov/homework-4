import unittest
from selenium import webdriver

from pages.edit_product import ProductEditPage
from pages.product import ProductPage
from pages.product_card import ProductCard
from pages.seller_products import SellerProductsPage
from components.login import LoginPage
from pages.user_chats import UserChats
from pages.user_products import UserProductsPage


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
        seller_products = SellerProductsPage(driver=self.driver)

        self.product.click_on_seller_name()
        url = self.driver.current_url
        self.assertTrue(seller_products.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerImg(self):
        """Успешный редирект на страницу всех объявлений при нажатии на фото"""
        seller_products = SellerProductsPage(driver=self.driver)

        self.product.click_on_seller_img()
        url = self.driver.current_url
        self.assertTrue(seller_products.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerRate(self):
        """Успешный редирект на страницу всех объявлений при нажатии на оценку"""
        seller_products = SellerProductsPage(driver=self.driver)

        self.product.click_on_seller_rate()

        url = self.driver.current_url

        self.assertTrue(seller_products.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testFailToShowPhoneNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к телефону при нажатии на кнопку "Показать номер\""""
        login = LoginPage(driver=self.driver)

        self.product.click_phone()

        self.assertTrue(login.is_opened(), "Не появляется панель логина")

    def tesToShowPhoneAuth(self):
        """Проверить изменение текста на кнопке "Показать номер" на номер телефона при нажатии на кнопку "Показать
        номер" у автора с действительным номером телефона """
        login = LoginPage(driver=self.driver)

        login.auth()

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
        login = LoginPage(driver=self.driver)

        login.auth()

        self.product.change_path("103")
        self.product.open()
        self.product.click_phone()

        self.assertEqual(
            self.product.get_phone(),
            "Нет телефона",
            "Появилась не надпись \"Нет телефона\"")

    def testFailToRedirectMasNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к телефону при нажатии на кнопку "Показать номер\""""
        login = LoginPage(driver=self.driver)

        self.product.click_massage()

        self.assertTrue(login.is_opened(), "Не появляется панель логина")

    def testToRedirectMasAuth(self):
        """Успешный редирект на страницу переписки при нажатии на кнопку \"Написать сообщение\""""
        login = LoginPage(driver=self.driver)
        message = UserChats(driver=self.driver)

        login.auth()

        self.product.click_massage()

        self.assertNotEqual(
            message.get_title(),
            "",
            "Не появляется страница диалога")

    def testToRedirectEdit(self):
        """Успешный редирект на страницу редактирования при нажатии кнопки \"Редактировать\""""
        login = LoginPage(driver=self.driver)
        edit_page = ProductEditPage(driver=self.driver)
        login.auth()
        user_products_page = UserProductsPage(driver=self.driver)
        user_products_page.open()
        product_card = ProductCard(driver=self.driver)
        product_card.click_product()
        edit_page.change_path(self.driver.current_url.split('/')[-1])
        self.product.click_edit()
        url = self.driver.current_url
        self.assertTrue(edit_page.is_compare_url(url), "Ошибка редиректа на страницу редактирования")

    def tearDown(self):
        self.driver.close()
