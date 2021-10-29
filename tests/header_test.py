import unittest
from selenium import webdriver

from pages.header import Header
from pages.login import LoginPage
from pages.search import SearchPage
from pages.main import MainPage


class HeaderTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.login = LoginPage(driver=self.driver)
        self.header = Header(driver=self.driver)
        self.header.open()

    def testClickLogo(self):
        """Проверка, что при нажатии на логотип открывается главная страница"""
        main = MainPage(driver=self.driver)

        self.header.click_logo()

        url = self.driver.current_url
        self.assertTrue(main.is_compare_url(url),  "Некорректный урл")

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку поиска открывается страница поиска"""
        search = SearchPage(driver=self.driver)

        self.header.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickCreate(self):
        """Проверка, что при нажатии на кнопку "Разместить объявление" открывается страница создания товара"""
        self.header.click_create()
        self.assertTrue(self.login.is_opened(), "Не открыта авторизация")
        self.login.click_close()

        self.login.auth()

        self.header.click_create()

        url = self.driver.current_url
        # TODO: переписать на CreateProductPage
        self.assertTrue(url == "https://ykoya.ru/product/create", "Некорректный урл")

    def testClickSettings(self):
        """Проверка, что при нажатии на кнопку "Настройки" открывается страница настроек"""
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_settings()

        url = self.driver.current_url
        # TODO: переписать на SettingsPage
        self.assertTrue(url == "https://ykoya.ru/user/profile", "Некорректный урл")

    def testClickAd(self):
        """Проверка, что при нажатии на кнопку "Мои объявления" открывается страница моих объявлений"""
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_ad()

        url = self.driver.current_url
        # TODO: переписать на AdPage
        self.assertTrue(url == "https://ykoya.ru/user/ad", "Некорректный урл")

    def testClickChats(self):
        """Проверка, что при нажатии на кнопку "Мои сообщения" открывается страница чатов"""
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_chats()

        url = self.driver.current_url
        # TODO: переписать на ChatsPage
        self.assertTrue(url == "https://ykoya.ru/user/chats", "Некорректный урл")

    def testClickFavorite(self):
        """Проверка, что при нажатии на кнопку "Избранное" открывается страница избранных товаров"""
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_favorites()

        url = self.driver.current_url
        # TODO: переписать на FavoritePage
        self.assertTrue(url == "https://ykoya.ru/user/favorite", "Некорректный урл")

    def testClickAchievements(self):
        """Проверка, что при нажатии на кнопку "Достижения" открывается страница достижений"""
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_achievements()

        url = self.driver.current_url
        # TODO: переписать на AchievementsPage
        self.assertTrue(url == "https://ykoya.ru/user/78/achievements", "Некорректный урл")

    def testClickReviews(self):
        """Проверка, что при нажатии на кнопку "Отзывы" открывается страница отзывов"""
        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_reviews()

        url = self.driver.current_url
        # TODO: переписать на ReviewsPage
        self.assertTrue(url == "https://ykoya.ru/user/78/reviews", "Некорректный урл")

    def tearDown(self):
        self.driver.close()
