import os

from helpers import Test

from pages import MainPage, SearchPage, CreateProductPage, UserChats, UserSettingsPage, \
    UserProductsPage, UserFavoritesPage, ReviewsPage, AchievementsPage


class HeaderTest(Test):
    def setUp(self):
        super().setUp()
        self.main = MainPage(driver=self.driver)
        self.main.open()

    def testClickLogo(self):
        """Проверка, что при нажатии на логотип открывается главная страница"""
        main = MainPage(driver=self.driver)

        self.main.header.click_logo()

        url = self.driver.current_url
        self.assertTrue(main.is_compare_url(url),  "Некорректный урл")

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку поиска открывается страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.header.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickCreate(self):
        """Проверка, что при нажатии на кнопку "Разместить объявление" открывается страница создания товара"""
        create_product = CreateProductPage(driver=self.driver)

        self.main.header.click_create()
        self.assertTrue(self.main.login.is_opened(), "Не открыта авторизация")
        self.main.login.click_close()

        self.main.login.auth()

        self.main.header.click_create()

        url = self.driver.current_url
        self.assertTrue(create_product.is_compare_url(url), "Некорректный урл")

    def testClickSettings(self):
        """Проверка, что при нажатии на кнопку "Настройки" открывается страница настроек"""
        settings = UserSettingsPage(driver=self.driver)

        self.main.login.auth()

        self.main.header.click_dropdown()
        self.assertTrue(self.main.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.main.header.click_settings()

        url = self.driver.current_url
        self.assertTrue(settings.is_compare_url(url), "Некорректный урл")

    def testClickAd(self):
        """Проверка, что при нажатии на кнопку "Мои объявления" открывается страница моих объявлений"""
        ad = UserProductsPage(driver=self.driver)

        self.main.login.auth()

        self.main.header.click_dropdown()
        self.assertTrue(self.main.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.main.header.click_ad()

        url = self.driver.current_url
        self.assertTrue(ad.is_compare_url(url), "Некорректный урл")

    def testClickChats(self):
        """Проверка, что при нажатии на кнопку "Мои сообщения" открывается страница чатов"""
        chats = UserChats(driver=self.driver)

        self.main.login.auth()

        self.main.header.click_dropdown()
        self.assertTrue(self.main.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.main.header.click_chats()

        url = self.driver.current_url
        self.assertTrue(chats.is_compare_url(url), "Некорректный урл")

    def testClickFavorite(self):
        """Проверка, что при нажатии на кнопку "Избранное" открывается страница избранных товаров"""
        favorites = UserFavoritesPage(driver=self.driver)

        self.main.login.auth()

        self.main.header.click_dropdown()
        self.assertTrue(self.main.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.main.header.click_favorites()

        url = self.driver.current_url
        self.assertTrue(favorites.is_compare_url(url), "Некорректный урл")

    def testClickAchievements(self):
        """Проверка, что при нажатии на кнопку "Достижения" открывается страница достижений"""
        achievements = AchievementsPage(driver=self.driver)
        user_id = os.environ.get("USER_ID")

        self.main.login.auth()

        self.main.header.click_dropdown()
        self.assertTrue(self.main.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.main.header.click_achievements()

        url = self.driver.current_url
        achievements.change_path(user_id)
        self.assertTrue(achievements.is_compare_url(url), "Некорректный урл")

    def testClickReviews(self):
        """Проверка, что при нажатии на кнопку "Отзывы" открывается страница отзывов"""
        reviews = ReviewsPage(driver=self.driver)
        user_id = os.environ.get("USER_ID")

        self.main.login.auth()

        self.main.header.click_dropdown()
        self.assertTrue(self.main.header.is_opened_dropdown(), "Не открыт дропдаун")

        self.main.header.click_reviews()

        url = self.driver.current_url
        reviews.change_path(user_id)
        self.assertTrue(reviews.is_compare_url(url), "Некорректный урл")
