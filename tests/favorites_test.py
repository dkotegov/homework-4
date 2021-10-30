import unittest
from selenium import webdriver

from pages.login import LoginPage
# from pages.header import HeaderPage
from pages.favorites import FavouritesPage
from pages.registration import RegistrationPage
from pages.side_bar import SideBarPage
from pages.all_seller_products import AllSellerProductsPage
from pages.product import ProductPage


class UserProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.favourites_page = FavouritesPage(driver=self.driver)

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке неавторизированного пользователя"""
        self.favourites_page.open()
        self.reg = RegistrationPage(driver=self.driver)
        self.assertEqual(self.reg.get_title(),
                         "Регистрация",
                         "Не открылась страница регистрации")

    # def testDropDownFavoritesButton(self):
    #     """Кнопка “Избранное” в выпадающем меню. Переход на страницу Избранное при нажатие"""
    #     self.login = LoginPage(driver=self.driver)
    #     self.login.open()
    #     self.login.auth()
    #     self.header = HeaderPage(driver=self.driver)
    #     self.header.click_favorites()
    #     self.assertEqual(self.favourites_page.get_title(),
    #                      "Избранное",
    #                      "Не открылась страница избранного")

    # def testSideBarFavoritesButton(self):
    #     """Кнопка “Избранное” в боковом меню на странице “Избранное”. Переход на страницу Избранное при нажатие."""
    #     self.login = LoginPage(driver=self.driver)
    #     self.login.open()
    #     self.login.auth()
    #     self.favourites_page.open()
    #     SideBarPage(driver=self.driver).click_my_favorites()
    #     self.assertEqual(self.favourites_page.get_title(),
    #                      "Избранное",
    #                      "Не открылась страница избранного")

    # def testFavoriteProductOpen(self):
    #     """Карточка объявления. Открытие страницы объявления при нажатие в любое место карточки, кроме “сердечка”."""
    #     self.login = LoginPage(driver=self.driver)
    #     self.login.open()
    #     self.login.auth()
    #     AllSellerProductsPage(driver=self.driver).likeProduct()
    #     self.favourites_page.open()
    #     product_card_title = self.favourites_page.get_product_title(0)
    #     self.favourites_page.click_product()
    #     self.product = ProductPage(driver=self.driver)
    #     self.assertEqual(product_card_title,
    #                      self.product.get_title(),
    #                      "Не открылась страница избранного")

    def testFavoriteProductDelete(self):
        """Иконка “Сердечко” на карточке товара. При нажатие товар пропадает со страницы “Избранное”."""
        self.login = LoginPage(driver=self.driver)
        self.login.open()
        self.login.auth()
        AllSellerProductsPage(driver=self.driver).likeProduct()
        self.favourites_page.open()
        before_remove = self.favourites_page.get_product_title(0)
        self.favourites_page.remove_like(0)
        self.assertEqual(before_remove,
                        self.favourites_page.get_product_title(0),
                         "Товар остался в избранном.")