import unittest
from selenium import webdriver

from components import Header, SideBar
from pages import FavouritesPage, RegistrationPage, SellerProductsPage, ProductPage


class FavoritesTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.favourites_page = FavouritesPage(driver=self.driver)
        self.favourites_page.open()

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке неавторизированного пользователя"""
        self.favourites_page.open()
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testDropDownFavoritesButton(self):
        """Кнопка “Избранное” в выпадающем меню. Переход на страницу Избранное при нажатие"""
        self.favourites_page.login.auth()
        header = Header(driver=self.driver)
        header.click_dropdown()
        header.click_favorites()
        self.assertTrue(self.favourites_page.is_compare_url(self.driver.current_url),
                         "Не открылась страница избранного")

    def testSideBarFavoritesButton(self):
        """Кнопка “Избранное” в боковом меню на странице “Избранное”. Переход на страницу Избранное при нажатие."""
        self.favourites_page.login.auth()
        SideBar(driver=self.driver).click_my_favorites()
        self.assertTrue(self.favourites_page.is_compare_url(self.driver.current_url),
                         "Не открылась страница избранного")

    def testFavoriteProductOpen(self):
        """Карточка объявления. Открытие страницы объявления при нажатие в любое место карточки, кроме “сердечка”."""
        self.favourites_page.login.auth()
        products = SellerProductsPage(driver=self.driver)
        products.open()
        products.product_card.like_product()
        self.favourites_page.open()
        product = ProductPage(driver=self.driver) 
        product_id = self.favourites_page.product_card.click_product()
        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

    def testFavoriteProductDelete(self):
        """Иконка “Сердечко” на карточке товара. При нажатие товар пропадает со страницы “Избранное”."""
        self.favourites_page.login.auth()
        products = SellerProductsPage(driver=self.driver)
        products.open()
        products.product_card.like_product()
        self.favourites_page.open()
        before_remove = self.favourites_page.count_products()
        self.favourites_page.product_card.remove_like_product(0)
        self.favourites_page.open()
        self.assertEqual(before_remove - 1,
                        self.favourites_page.count_products(),
                         "Товар остался в избранном.")