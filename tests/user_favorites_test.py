from helpers import Test

from pages import UserFavoritesPage, MainPage, RegistrationPage, SellerProductsPage, ProductPage


class UserFavoritesTest(Test):
    def setUp(self):
        super().setUp()
        self.favorites_page = UserFavoritesPage(driver=self.driver)

    def __auth__(self):
        main_page = MainPage(driver=self.driver)

        main_page.open()
        main_page.login.auth()

    def testRedirectToRegistrationPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration_page = RegistrationPage(driver=self.driver)

        self.favorites_page.open()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegistrationPageLogOut(self):
        """Открытие страницы регистрации при после выхода из профиля"""
        registration_page = RegistrationPage(driver=self.driver)

        self.__auth__()
        self.favorites_page.open()
        self.favorites_page.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testClickProduct(self):
        """Карточка объявления. Открытие страницы объявления при нажатии в любое место карточки, кроме “сердечка”"""
        product_page = ProductPage(driver=self.driver)
        seller_products_page = SellerProductsPage(driver=self.driver)

        self.__auth__()
        seller_products_page.open()

        product_id = self.favorites_page.product_card.get_product_id()
        seller_products_page.product_card.click_like_product(product_id)

        self.favorites_page.open()

        self.favorites_page.product_card.click_product(product_id)

        url = self.driver.current_url
        product_page.change_path(product_id)
        self.assertTrue(product_page.is_compare_url(url), "Не открылась страница товара")

        seller_products_page.open()
        seller_products_page.product_card.click_like_product(product_id)

    def testFavoriteProductDelete(self):
        """Иконка “Сердечко” на карточке товара. При нажатии товар пропадает со страницы “Избранное”"""
        seller_products_page = SellerProductsPage(driver=self.driver)

        self.__auth__()
        seller_products_page.open()

        product_id = seller_products_page.product_card.get_product_id()
        seller_products_page.product_card.click_like_product(product_id)

        self.favorites_page.open()

        before_remove_product = self.favorites_page.product_card.count_products()
        self.favorites_page.product_card.click_like_product(product_id)

        after_remove_product = self.favorites_page.product_card.count_products()
        self.assertEqual(before_remove_product - 1, after_remove_product, "Товар остался в избранном")
