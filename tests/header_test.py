import unittest
from selenium import webdriver

from pages.header import HeaderPage
from pages.login import LoginPage
from pages.search import SearchPage
from pages.main import MainPage


class HeaderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.login = LoginPage(driver=self.driver)
        self.header = HeaderPage(driver=self.driver)
        self.header.open()

    def testClickLogo(self):
        main = MainPage(driver=self.driver)

        self.header.click_logo()

        url = self.driver.current_url
        self.assertTrue(main.is_compare_url(url),  "Некорректный урл")

    def testClickSearch(self):
        search = SearchPage(driver=self.driver)

        self.header.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickCreate(self):
        self.login.auth()

        self.header.click_create()

        url = self.driver.current_url
        # TODO: переписать на CreateProductPage
        self.assertTrue(url == "https://ykoya.ru/product/create", "Некорректный урл")

    def testClickSettings(self):
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_settings()

        url = self.driver.current_url
        # TODO: переписать на SettingsPage
        self.assertTrue(url == "https://ykoya.ru/user/profile", "Некорректный урл")

    def testClickAd(self):
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_ad()

        url = self.driver.current_url
        # TODO: переписать на AdPage
        self.assertTrue(url == "https://ykoya.ru/user/ad", "Некорректный урл")

    def testClickChats(self):
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_chats()

        url = self.driver.current_url
        # TODO: переписать на ChatsPage
        self.assertTrue(url == "https://ykoya.ru/user/chats", "Некорректный урл")

    def testClickFavorite(self):
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_favorites()

        url = self.driver.current_url
        # TODO: переписать на FavoritePage
        self.assertTrue(url == "https://ykoya.ru/user/favorite", "Некорректный урл")

    def testClickAchievements(self):
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_achievements()

        url = self.driver.current_url
        # TODO: переписать на AchievementsPage
        self.assertTrue(url == "https://ykoya.ru/user/78/achievements", "Некорректный урл")

    def testClickReviews(self):
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_reviews()

        url = self.driver.current_url
        # TODO: переписать на ReviewsPage
        self.assertTrue(url == "https://ykoya.ru/user/78/reviews", "Некорректный урл")

    def tearDown(self):
        self.driver.close()
