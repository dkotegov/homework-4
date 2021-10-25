import time
import unittest
from selenium import webdriver

from pages.login import LoginPage
from pages.user_products import UserProductsPage
from pages.registration import RegistrationPage
from pages.product import ProductPage


class UserProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver')
        self.user_products_page = UserProductsPage(driver=self.driver)

    def testRedirectToRegPage(self):
        """Успешный редирект на страницу регистрации при переходе по ссылке https://ykoya.ru/user/ad
        неавторизованного пользователя """
        self.user_products_page.open()
        self.reg = RegistrationPage(driver=self.driver)
        self.assertEqual(self.reg.get_title(),
                         "Регистрация",
                         "Не открылась страница регистрации")

    def testRedirectToRegPageLogOut(self):
        """Успешный редирект на страницу регистрации при выходе из профиля """
        self.login = LoginPage(driver=self.driver)
        self.login.open()
        self.login.auth()
        self.user_products_page.open()
        self.login.logout()
        self.reg = RegistrationPage(driver=self.driver)
        self.assertEqual(self.reg.get_title(),
                         "Регистрация",
                         "Не открылась страница регистрации")

    def tearDown(self):
        self.driver.close()
