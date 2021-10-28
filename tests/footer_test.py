import unittest
from selenium import webdriver

from pages.footer import FooterPage
from pages.login import LoginPage
from pages.search import SearchPage
from pages.main import MainPage
from pages.registration import RegistrationPage


class FooterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.login = LoginPage(driver=self.driver)
        self.footer = FooterPage(driver=self.driver)
        self.footer.open()

    def testClickLogo(self):
        main = MainPage(driver=self.driver)

        self.footer.click_logo()

        url = self.driver.current_url
        self.assertTrue(main.is_compare_url(url), "Некорректный урл")

    def testClickCreate(self):
        self.login.auth()

        self.footer.click_create()

        url = self.driver.current_url
        # TODO: переписать на CreateProductPage
        self.assertTrue(url == "https://ykoya.ru/product/create", "Некорректный урл")

    def testClickSearch(self):
        search = SearchPage(driver=self.driver)

        self.footer.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickSettings(self):
        self.login.auth()

        self.footer.click_settings()

        url = self.driver.current_url
        # TODO: переписать на SettingsPage
        self.assertTrue(url == "https://ykoya.ru/user/profile", "Некорректный урл")

    def testClickAd(self):
        self.login.auth()

        self.footer.click_ad()

        url = self.driver.current_url
        # TODO: переписать на AdPage
        self.assertTrue(url == "https://ykoya.ru/user/ad", "Некорректный урл")

    def testClickChats(self):
        self.login.auth()

        self.footer.click_chats()

        url = self.driver.current_url
        # TODO: переписать на ChatsPage
        self.assertTrue(url == "https://ykoya.ru/user/chats", "Некорректный урл")

    def testClickFavorite(self):
        self.login.auth()

        self.footer.click_favorites()

        url = self.driver.current_url
        # TODO: переписать на FavoritePage
        self.assertTrue(url == "https://ykoya.ru/user/favorite", "Некорректный урл")

    def testClickRegistration(self):
        registration = RegistrationPage(driver=self.driver)

        self.footer.click_registration()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Некорректный урл")

    def tearDown(self):
        self.driver.close()
