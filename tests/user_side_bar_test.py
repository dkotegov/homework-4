from helpers import Test

from pages import ReviewsPage, UserAwaitReviewsPage, AchievementsPage, UserSettingsPage, \
    UserMessagesPage, UserFavoritesPage, UserProductsPage


class UserSideBarTest(Test):
    def setUp(self):
        super().setUp()
        self.settings = UserSettingsPage(driver=self.driver)
        self.settings.open()
        self.settings.login.auth()
        self.settings.open()

    def testClickSettings(self):
        """Кнопка “Настройки” в боковом меню. Переход на страницу Настройки при нажатии"""
        settings = UserSettingsPage(driver=self.driver)

        self.settings.side_bar.click_my_settings()

        url = self.driver.current_url
        self.assertTrue(settings.is_compare_url(url), "Не открылась страница настройки")

    def testClickMyProducts(self):
        """Кнопка “Мои объявления” в боковом меню. Переход на страницу Мои объявления при нажатии"""
        products = UserProductsPage(driver=self.driver)

        self.settings.side_bar.click_my_products()

        url = self.driver.current_url
        self.assertTrue(products.is_compare_url(url), "Не открылась страница объявлений")

    def testClickMessages(self):
        """Кнопка “Мои сообщения” в боковом меню. Переход на страницу Мои сообщения при нажатии"""
        messages = UserMessagesPage(driver=self.driver)

        self.settings.side_bar.click_my_messages()

        url = self.driver.current_url
        self.assertTrue(messages.is_compare_url(url), "Не открылась страница сообщений")

    def testClickFavorites(self):
        """Кнопка “Избранное” в боковом меню. Переход на страницу Избранное при нажатии"""
        favorites = UserFavoritesPage(driver=self.driver)

        self.settings.side_bar.click_my_favorites()

        url = self.driver.current_url
        self.assertTrue(favorites.is_compare_url(url), "Не открылась страница избранного")

    def testClickAchievements(self):
        """Кнопка “Достижения” в боковом меню. Переход на страницу Достижения при нажатии"""
        # TODO: брать из ENV
        achievements = AchievementsPage(driver=self.driver)
        user_id = "78"

        self.settings.side_bar.click_achievements()

        url = self.driver.current_url
        achievements.change_path(user_id)
        self.assertTrue(achievements.is_compare_url(url), "Не открылась страница достижений")

    def testClickReviews(self):
        """Кнопка “Отзывы” в боковом меню. Переход на страницу Отзывы при нажатии"""
        # TODO: брать из ENV
        reviews = ReviewsPage(driver=self.driver)
        user_id = "78"

        self.settings.side_bar.click_reviews()

        url = self.driver.current_url
        reviews.change_path(user_id)
        self.assertTrue(reviews.is_compare_url(url), "Не открылась страница отзывов")

    def testClickAwaitReviews(self):
        """Кнопка “Ожидает отзывы” в боковом меню. Переход на страницу ожидает отзывы при нажатии"""
        reviews = UserAwaitReviewsPage(driver=self.driver)

        self.settings.side_bar.click_my_review_awaits()

        url = self.driver.current_url
        self.assertTrue(reviews.is_compare_url(url), "Не открылась страница ожидающих отзывов")
