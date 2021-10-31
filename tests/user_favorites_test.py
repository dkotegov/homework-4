from helpers import Test

from pages import FavoritesPage, RegistrationPage, SellerProductsPage, ProductPage


class UserFavoritesTest(Test):
    def setUp(self):
        super().setUp()
        self.favourites_page = FavoritesPage(driver=self.driver)
        self.products = SellerProductsPage(driver=self.driver)
        self.favourites_page.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке не авторизированного пользователя"""
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testFavoriteProductOpen(self):
        """Карточка объявления. Открытие страницы объявления при нажатии в любое место карточки, кроме “сердечка”"""
        product = ProductPage(driver=self.driver)

        self.favourites_page.login.auth()
        self.products.open()

        self.products.product_card.like_product()
        self.favourites_page.open()

        product_id = self.favourites_page.product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

        self.favourites_page.open()
        self.favourites_page.product_card.remove_like_product(0)

    def testFavoriteProductDelete(self):
        """Иконка “Сердечко” на карточке товара. При нажатии товар пропадает со страницы “Избранное”"""
        self.favourites_page.login.auth()
        self.products.open()

        self.products.product_card.like_product()
        self.favourites_page.open()

        before_remove = self.favourites_page.count_products()

        self.favourites_page.product_card.remove_like_product(0)
        self.favourites_page.open()
        self.assertEqual(before_remove - 1, self.favourites_page.count_products(), "Товар остался в избранном")
