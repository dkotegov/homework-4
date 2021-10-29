import unittest
from selenium import webdriver

from pages.footer import Footer
from pages.login import LoginPage
from pages.search import SearchPage
from pages.main import MainPage
from pages.registration import RegistrationPage


class FooterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.login = LoginPage(driver=self.driver)
        self.footer = Footer(driver=self.driver)
        self.footer.open()

    def testClickLogo(self):
        """Проверка, что при нажатии на логотип открывается главная страница"""
        main = MainPage(driver=self.driver)

        self.footer.click_logo()

        url = self.driver.current_url
        self.assertTrue(main.is_compare_url(url), "Некорректный урл")

    def testClickCreate(self):
        """Проверка, что при нажатии на кнопку "Разместить объявление" открывается страница создания товара"""
        self.footer.click_create()
        self.assertTrue(self.login.is_opened(), "Не открыта авторизация")
        self.login.click_close()

        self.login.auth()

        self.footer.click_create()

        url = self.driver.current_url
        # TODO: переписать на CreateProductPage
        self.assertTrue(url == "https://ykoya.ru/product/create", "Некорректный урл")

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку "Поиск" открывается страница поиска"""
        search = SearchPage(driver=self.driver)

        self.footer.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickSettings(self):
        """Проверка, что при нажатии на кнопку "Настройки" открывается страница настроек"""
        self.login.auth()

        self.footer.click_settings()

        url = self.driver.current_url
        # TODO: переписать на SettingsPage
        self.assertTrue(url == "https://ykoya.ru/user/profile", "Некорректный урл")

    def testClickAd(self):
        """Проверка, что при нажатии на кнопку "Мои объявления" открывается страница моих объявлений"""
        self.login.auth()

        self.footer.click_ad()

        url = self.driver.current_url
        # TODO: переписать на AdPage
        self.assertTrue(url == "https://ykoya.ru/user/ad", "Некорректный урл")

    def testClickChats(self):
        """Проверка, что при нажатии на кнопку "Мои сообщения" открывается страница чатов"""
        self.login.auth()

        self.footer.click_chats()

        url = self.driver.current_url
        # TODO: переписать на ChatsPage
        self.assertTrue(url == "https://ykoya.ru/user/chats", "Некорректный урл")

    def testClickFavorite(self):
        """Проверка, что при нажатии на кнопку "Избранное" открывается страница избранных товаров"""
        self.login.auth()

        self.footer.click_favorites()

        url = self.driver.current_url
        # TODO: переписать на FavoritePage
        self.assertTrue(url == "https://ykoya.ru/user/favorite", "Некорректный урл")

    def testClickRegistration(self):
        """Проверка, что при нажатии на кнопку "Регистрация" открывается страница регистрации"""
        registration = RegistrationPage(driver=self.driver)

        self.footer.click_registration()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Некорректный урл")

    def testClickAuth(self):
        """Проверка, что при нажатии на кнопку "Авторизация" открывается попап авторизации"""

        self.footer.click_auth()
        self.assertTrue(self.login.is_opened(), "Закрыта авторизация")

    def tearDown(self):
        self.driver.close()
