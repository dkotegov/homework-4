from helpers import Test

from pages import ReviewsPage, AwaitReviewsPage, AchievementsPage, UserSettingsPage, \
    MessagesPage, FavoritesPage, UserProductsPage


class FooterTest(Test):
    def setUp(self):
        super().setUp()
        self.settings = UserSettingsPage(driver=self.driver)
        self.settings.login.auth()
        self.settings.open()

    def testSideBarFavoritesButton(self):
        """Кнопка “Избранное” в боковом меню. Переход на страницу Избранное при нажатие."""
        favorites = FavoritesPage(driver=self.driver)
        self.settings.side_bar.click_my_favorites()

        self.assertTrue(favorites.is_compare_url(self.driver.current_url),
                         "Не открылась страница избранного")

    def testSideBarMessagesButton(self):
        """Кнопка “Мои сообщения” в боковом меню. Переход на страницу Мои сообщения при нажатие"""
        messages = MessagesPage(driver=self.driver)
        self.settings.side_bar.click_my_messages()

        self.assertTrue(messages.is_compare_url(self.driver.current_url),
                         "Не открылась страница сообщений")

    def testSideBarSettingsButton(self):
        """Кнопка “Настройки” в боковом меню. Переход на страницу Настройки при нажатие."""
        settings = UserSettingsPage(driver=self.driver)
        self.settings.side_bar.click_my_settings()

        self.assertTrue(settings.is_compare_url(self.driver.current_url),
                         "Не открылась страница настройки")

    def testSideBarMyProductsButton(self):
        """Кнопка “Мои объявления” в боковом меню. Переход на страницу Мои объявления при нажатие."""
        products = UserProductsPage(driver=self.driver)
        self.settings.side_bar.click_my_products()

        self.assertTrue(products.is_compare_url(self.driver.current_url),
                         "Не открылась страница объявлений")

    def testSideBarMyMessagesButton(self):
        """Кнопка “Достижения” в боковом меню. Переход на страницу Достижения при нажатие."""
        achievements = AchievementsPage(driver=self.driver)
        self.settings.side_bar.click_my_achivements()

        self.assertTrue(achievements.is_compare_url(self.driver.current_url),
                         "Не открылась страница достижений")

    def testSideBarReviewsButton(self):
        """Кнопка “Отзывы” в боковом меню. Переход на страницу Отзывы при нажатие."""
        reviews = ReviewsPage(driver=self.driver)
        self.settings.side_bar.click_my_comments()

        self.assertTrue(reviews.is_compare_url(self.driver.current_url),
                         "Не открылась страница отзывов")

    def testSideBarAwaitReviewsButton(self):
        """Кнопка “Ожидает отзывы” в боковом меню. Переход на страницу Ожидает отзывы при нажатие."""
        reviews = AwaitReviewsPage(driver=self.driver)
        self.settings.side_bar.click_my_review_awaits()

        self.assertTrue(reviews.is_compare_url(self.driver.current_url),
                         "Не открылась страница ожидающих отзывов")