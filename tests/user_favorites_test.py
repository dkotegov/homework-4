from helpers import Test

from pages import UserFavoritesPage, RegistrationPage, SellerProductsPage, ProductPage


class UserFavoritesTest(Test):
    def setUp(self):
        super().setUp()
        self.favorites = UserFavoritesPage(driver=self.driver)
        self.products = SellerProductsPage(driver=self.driver)
        self.favorites.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testFavoriteProductOpen(self):
        """Карточка объявления. Открытие страницы объявления при нажатии в любое место карточки, кроме “сердечка”"""
        product = ProductPage(driver=self.driver)

        self.favorites.login.auth()
        self.products.open()

        self.products.product_card.like_product()
        self.favorites.open()

        product_id = self.favorites.favorite_products.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

        self.favorites.open()
        self.favorites.favorite_products.remove_like_product(0)

    def testFavoriteProductDelete(self):
        """Иконка “Сердечко” на карточке товара. При нажатии товар пропадает со страницы “Избранное”"""
        self.favorites.login.auth()
        self.products.open()

        self.products.product_card.like_product()
        self.favorites.open()

        before_remove = self.favorites.favorite_products.count_products()

        self.favorites.favorite_products.remove_like_product(0)
        self.favorites.open()

        after_remove = self.favorites.favorite_products.count_products()
        self.assertEqual(before_remove - 1, after_remove, "Товар остался в избранном")
