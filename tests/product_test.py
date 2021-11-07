from consts import VK_ERROR_PRODUCT
from helpers import Test

from pages import ProductPage, ProductEditPage, SellerProductsPage, UserProductsPage, UserMessagesPage


class ProductTest(Test):
    def setUp(self):
        super().setUp()
        self.product_page = ProductPage(driver=self.driver)
        self.seller_products_page = SellerProductsPage(driver=self.driver)
        self.product_page.open()

    def __auth__(self):
        self.product_page.login.auth()
        self.product_page.open()

    def testFirstImgEqualPreview(self):
        """Проверить, что при открытии страницы первая картинка слайдера совпадает с превью товара"""
        slider_image = self.product_page.photos.selected_img_src_from_slider()
        preview_img = self.product_page.photos.preview_img_src()
        self.assertEqual(
            slider_image,
            preview_img,
            "Первая картинка слайдера не совпадает с превью товара")

    def testChangePreview(self):
        """Проверить, что по нажатию на картинку из слайдера изменяется превью товара"""
        self.product_page.photos.click_different_preview()
        slider_image = self.product_page.photos.selected_img_src_from_slider()
        preview_img = self.product_page.photos.preview_img_src()
        self.assertEqual(
            slider_image,
            preview_img,
            "Выбранная картинка слайдера не совпадает с превью товара")

    def testRedirectToAdsByClickSellerName(self):
        """Успешный редирект на страницу всех объявлений при нажатии на имя"""

        self.product_page.info_card.click_on_seller_name()

        self.seller_products_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(self.seller_products_page.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testRedirectToAdsByClickSellerImg(self):
        """Успешный редирект на страницу всех объявлений при нажатии на фото"""

        self.product_page.info_card.click_on_seller_img()

        self.seller_products_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(self.seller_products_page.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testRedirectToAdsByClickSellerRate(self):
        """Успешный редирект на страницу всех объявлений при нажатии на оценку"""

        self.product_page.info_card.click_on_seller_rate()

        self.seller_products_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(self.seller_products_page.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testFailToShowPhoneNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к телефону при нажатии на кнопку "Показать номер\""""
        self.product_page.info_card.click_phone()
        self.assertTrue(self.product_page.login.is_opened(), "Не появляется панель логина")

    def testToShowPhoneAuth(self):
        """Проверить изменение текста на кнопке "Показать номер" на номер телефона при нажатии на кнопку "Показать
        номер" у автора с действительным номером телефона """
        tel_expected = "+71234567890"
        self.__auth__()
        self.product_page.info_card.click_phone()
        tel_current = self.product_page.info_card.get_phone()
        self.assertEqual(
            tel_current,
            tel_expected,
            "Появился не номер телефона")

    def testFailToShowPhoneAuthVK(self):
        """Ошибка данных, при нажатии на кнопку "Показать номер" автора зарегистрированного с помощью ВК, без номера
        телефона """
        self.product_page.change_path(VK_ERROR_PRODUCT)
        self.__auth__()
        self.product_page.info_card.click_phone()
        self.assertEqual(
            self.product_page.info_card.get_phone(),
            "Нет телефона",
            "Появилась не надпись \"Нет телефона\"")

    def testFailToChatNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к переписке при нажатии на кнопку "Написать сообщение\""""
        self.product_page.info_card.click_message()
        self.assertTrue(self.product_page.login.is_opened(), "Не появляется панель логина")

    def testRedirectToMsgByClickWriteMsgBtn(self):
        """Успешный редирект на страницу переписки при нажатии на кнопку \"Написать сообщение\""""
        message = UserMessagesPage(driver=self.driver)
        self.__auth__()
        self.product_page.info_card.click_message()
        self.assertTrue(message.page_exist(), "Не появляется страница диалога")

    def testToRedirectEdit(self):
        """Успешный редирект на страницу редактирования при нажатии кнопки \"Редактировать\""""
        edit_page = ProductEditPage(driver=self.driver)
        user_products_page = UserProductsPage(driver=self.driver)
        self.__auth__()
        user_products_page.open()

        product_id = user_products_page.product_card.get_product_id()

        user_products_page.product_card.click_product(product_id)
        edit_page.change_path(product_id)
        self.product_page.info_card.click_edit()

        edit_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(edit_page.is_compare_url(url), "Ошибка редиректа на страницу редактирования")
