import unittest
from selenium import webdriver

from pages.header import Header
from pages.login import LoginPage
from pages.search import SearchPage
from pages.main import MainPage
from pages.user_settings import UserSettingsPage
from pages.user_products import UserProductsPage
from pages.user_chats import UserChats
from pages.user_favorites import UserFavoritesPage
from pages.achievements import AchievementsPage
from pages.reviews import ReviewsPage
from pages.create_product import CreateProductPage


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
        create_product = CreateProductPage(driver=self.driver)

        self.header.click_create()
        self.assertTrue(self.login.is_opened(), "Не открыта авторизация")
        self.login.click_close()

        self.login.auth()

        self.header.click_create()

        url = self.driver.current_url
        self.assertTrue(create_product.is_compare_url(url), "Некорректный урл")

    def testClickSettings(self):
        """Проверка, что при нажатии на кнопку "Настройки" открывается страница настроек"""
        settings = UserSettingsPage(driver=self.driver)

        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_settings()

        url = self.driver.current_url
        self.assertTrue(settings.is_compare_url(url), "Некорректный урл")

    def testClickAd(self):
        """Проверка, что при нажатии на кнопку "Мои объявления" открывается страница моих объявлений"""
        ad = UserProductsPage(driver=self.driver)

        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_ad()

        url = self.driver.current_url
        self.assertTrue(ad.is_compare_url(url), "Некорректный урл")

    def testClickChats(self):
        """Проверка, что при нажатии на кнопку "Мои сообщения" открывается страница чатов"""
        chats = UserChats(driver=self.driver)

        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_chats()

        url = self.driver.current_url
        self.assertTrue(chats.is_compare_url(url), "Некорректный урл")

    def testClickFavorite(self):
        """Проверка, что при нажатии на кнопку "Избранное" открывается страница избранных товаров"""
        favorites = UserFavoritesPage(driver=self.driver)

        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_favorites()

        url = self.driver.current_url
        self.assertTrue(favorites.is_compare_url(url), "Некорректный урл")

    def testClickAchievements(self):
        """Проверка, что при нажатии на кнопку "Достижения" открывается страница достижений"""
        achievements = AchievementsPage(driver=self.driver)

        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_achievements()

        url = self.driver.current_url
        # TODO: брать из ENV
        achievements.change_path("78")
        self.assertTrue(achievements.is_compare_url(url), "Некорректный урл")

    def testClickReviews(self):
        """Проверка, что при нажатии на кнопку "Отзывы" открывается страница отзывов"""
        reviews = ReviewsPage(driver=self.driver)

        self.login.auth()

        self.header.click_dropdown()
        self.assertTrue(self.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.header.click_reviews()

        url = self.driver.current_url
        # TODO: брать из ENV
        reviews.change_path("78")
        self.assertTrue(reviews.is_compare_url(url), "Некорректный урл")

    def tearDown(self):
        self.driver.close()
