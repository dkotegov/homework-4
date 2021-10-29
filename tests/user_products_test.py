import unittest
from selenium import webdriver

from pages.user_products import UserProductsPage
from pages.login import LoginPage
from pages.user_chats import UserChats
from pages.registration import RegistrationPage
from pages.footer import Footer
from pages.product import ProductPage
from pages.product_card import ProductCard


class UserProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.user_products_page = UserProductsPage(driver=self.driver)
        self.login = LoginPage(driver=self.driver)

    def testRedirectToRegPage(self):
        """Успешный редирект на страницу регистрации при переходе по ссылке https://ykoya.ru/user/ad
        неавторизованного пользователя """
        registration = RegistrationPage(driver=self.driver)

        self.user_products_page.open()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegPageLogOut(self):
        """Успешный редирект на страницу регистрации при выходе из профиля """
        registration = RegistrationPage(driver=self.driver)

        self.login.open()
        self.login.auth()
        self.user_products_page.open()
        self.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectFromFooterToUserProducts(self):
        """Успешный редирект на страницу "Мои объявления" при нажатии кнопки в нижнем меню сайта “Мои объявления”"""
        footer = Footer(driver=self.driver)

        self.login.open()
        self.login.auth()

        footer.click_ad()

        url = self.driver.current_url
        self.assertTrue(self.user_products_page.is_compare_url(url), "Не открылась страница Мои объявления")

    def testRedirectFromSettingsToUserProducts(self):
        """Успешный редирект на страницу "Мои объявления" при нажатии кнопки в боковом меню “Мои объявления”"""
        self.login.open()
        self.login.auth()

        chats = UserChats(driver=self.driver)
        chats.open()
        chats.click_my_products()

        url = self.driver.current_url
        self.assertTrue(self.user_products_page.is_compare_url(url), "Не открылась страница Мои объявления")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        self.login.open()
        self.login.auth()
        self.user_products_page.open()

        product = ProductPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_id = product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

    def tearDown(self):
        self.driver.close()
