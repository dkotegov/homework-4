from tests.helpers.default_test import DefaultTest

from pages.product import ProductPage
from pages.seller_products import SellerProductsPage
from pages.login import LoginPage
from pages.user_chats import UserChats


class ProductTest(DefaultTest):
    def setUp(self):
        super().setUp()
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

        self.assertEqual(
            seller_products.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerImg(self):
        """Успешный редирект на страницу всех объявлений при нажатии на фото"""
        seller_products = SellerProductsPage(driver=self.driver)

        self.product.click_on_seller_img()

        self.assertEqual(
            seller_products.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerRate(self):
        """Успешный редирект на страницу всех объявлений при нажатии на оценку"""
        seller_products = SellerProductsPage(driver=self.driver)

        self.product.click_on_seller_rate()

        self.assertEqual(
            seller_products.get_title(),
            "Все объявления",
            "Ошибка редиректа на страницу всех объявлений")

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
