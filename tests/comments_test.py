import unittest
from selenium import webdriver

from pages.login import LoginPage
from pages.registration import RegistrationPage
from pages.comments import CommentsPage
from pages.side_bar import SideBarPage
from pages.all_seller_products import AllSellerProductsPage
from pages.product import ProductPage


class UserProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.comments_page = CommentsPage(driver=self.driver)

    def testRedirectToRegPage(self):
        """Открытие страницы регистрации при переходе по ссылке неавторизированного пользователя"""
        self.comments_page.open()
        self.reg = RegistrationPage(driver=self.driver)
        self.assertEqual(self.reg.get_title(),
                         "Регистрация",
                         "Не открылась страница регистрации")