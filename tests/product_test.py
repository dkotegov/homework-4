from helpers import Test

from pages import ProductPage, ProductEditPage, SellerProductsPage, UserChats, UserProductsPage


class ProductTest(Test):
    def setUp(self):
        super().setUp()
        self.product = ProductPage(driver=self.driver)
        self.product.open()

    def testFirstImgSrcEqualPreview(self):
        """Проверить, что при открытии страницы первая картинка слайдера совпадает с превью товара"""
        self.assertEqual(
            self.product.photos.selected_img_src_from_slider(),
            self.product.photos.preview_img_src(),
            "Первая картинка слайдера не совпадает с превью товара")

    def testChangePreview(self):
        """Проверить, что по нажатию на картинку из слайдера изменяется превью товара"""
        self.product.photos.click_different_preview()
        self.assertEqual(
            self.product.photos.selected_img_src_from_slider(),
            self.product.photos.preview_img_src(),
            "Выбранная картинка слайдера не совпадает с превью товара")

    def testOpenAllItemsBySellerName(self):
        """Успешный редирект на страницу всех объявлений при нажатии на имя"""
        seller_products = SellerProductsPage(driver=self.driver)
        self.product.info_card.click_on_seller_name()
        url = self.driver.current_url
        self.assertTrue(seller_products.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerImg(self):
        """Успешный редирект на страницу всех объявлений при нажатии на фото"""
        seller_products = SellerProductsPage(driver=self.driver)
        self.product.info_card.click_on_seller_img()
        url = self.driver.current_url
        self.assertTrue(seller_products.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testOpenAllItemsBySellerRate(self):
        """Успешный редирект на страницу всех объявлений при нажатии на оценку"""
        seller_products = SellerProductsPage(driver=self.driver)
        self.product.info_card.click_on_seller_rate()
        url = self.driver.current_url
        self.assertTrue(seller_products.is_compare_url(url), "Ошибка редиректа на страницу всех объявлений")

    def testFailToShowPhoneNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к телефону при нажатии на кнопку "Показать номер\""""
        self.product.info_card.click_phone()
        self.assertTrue(self.product.login.is_opened(), "Не появляется панель логина")

    def tesToShowPhoneAuth(self):
        """Проверить изменение текста на кнопке "Показать номер" на номер телефона при нажатии на кнопку "Показать
        номер" у автора с действительным номером телефона """
        self.product.login.auth()
        self.product.open()
        self.product.info_card.click_phone()
        self.assertRegex(
            self.product.info_card.get_phone(),
            r"((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{"
            r"4}|\d{3}[-\.\s]??\d{4}))",
            "Появился не номер телефона")

    def testFailToShowPhoneAuthVK(self):
        """Ошибка данных, при нажатии на кнопку "Показать номер" автора  зарегистрированного с помощью ВК, без номера
        телефона """
        self.product.login.auth()
        self.product.change_path("103")
        self.product.open()
        self.product.info_card.click_phone()
        self.assertEqual(
            self.product.info_card.get_phone(),
            "Нет телефона",
            "Появилась не надпись \"Нет телефона\"")

    def testFailToRedirectMasNotAuth(self):
        """Для неавторизованного пользователя: Ошибка доступа к переписки при нажатии на кнопку "Написать сообщение\""""
        self.product.info_card.click_message()
        self.assertTrue(self.product.login.is_opened(), "Не появляется панель логина")

    def testToRedirectMasAuth(self):
        """Успешный редирект на страницу переписки при нажатии на кнопку \"Написать сообщение\""""
        self.product.login.auth()
        message = UserChats(driver=self.driver)
        self.product.info_card.click_message()
        self.assertNotEqual(
            message.get_title(),
            "",
            "Не появляется страница диалога")

    def testToRedirectEdit(self):
        """Успешный редирект на страницу редактирования при нажатии кнопки \"Редактировать\""""
        self.product.login.auth()
        edit_page = ProductEditPage(driver=self.driver)
        user_products_page = UserProductsPage(driver=self.driver)
        user_products_page.open()
        user_products_page.product_card.click_product()
        edit_page.change_path(self.driver.current_url.split('/')[-1])
        self.product.info_card.click_edit()
        url = self.driver.current_url
        self.assertTrue(edit_page.is_compare_url(url), "Ошибка редиректа на страницу редактирования")

