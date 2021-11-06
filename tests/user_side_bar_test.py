from consts import TEST_USER
from helpers import Test

from pages import ReviewsPage, UserAwaitReviewsPage, AchievementsPage, UserSettingsPage, \
    UserMessagesPage, UserFavoritesPage, UserProductsPage, MainPage


class UserSideBarTest(Test):
    def setUp(self):
        super().setUp()
        self.settings_page = UserSettingsPage(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        main_page.open()
        main_page.login.auth()
        self.settings_page.open()

    def testClickSettings(self):
        """Кнопка “Настройки” в боковом меню. Переход на страницу Настройки при нажатии"""
        products_page = UserProductsPage(driver=self.driver)

        products_page.open()
        products_page.side_bar.click_settings()

        url = self.driver.current_url
        self.assertTrue(self.settings_page.is_compare_url(url), "Не открылась страница настройки")

    def testClickMyProducts(self):
        """Кнопка “Мои объявления” в боковом меню. Переход на страницу Мои объявления при нажатии"""
        user_products_page = UserProductsPage(driver=self.driver)

        self.settings_page.side_bar.click_products()

        url = self.driver.current_url
        self.assertTrue(user_products_page.is_compare_url(url), "Не открылась страница объявлений")

    def testClickMessages(self):
        """Кнопка “Мои сообщения” в боковом меню. Переход на страницу Мои сообщения при нажатии"""
        messages_page = UserMessagesPage(driver=self.driver)

        self.settings_page.side_bar.click_messages()

        url = self.driver.current_url
        self.assertTrue(messages_page.is_compare_url(url), "Не открылась страница сообщений")

    def testClickFavorites(self):
        """Кнопка “Избранное” в боковом меню. Переход на страницу Избранное при нажатии"""
        favorites_page = UserFavoritesPage(driver=self.driver)

        self.settings_page.side_bar.click_favorites()

        url = self.driver.current_url
        self.assertTrue(favorites_page.is_compare_url(url), "Не открылась страница избранного")

    def testClickAchievements(self):
        """Кнопка “Достижения” в боковом меню. Переход на страницу Достижения при нажатии"""
        achievements_page = AchievementsPage(driver=self.driver)

        self.settings_page.side_bar.click_achievements()

        url = self.driver.current_url
        achievements_page.change_path(TEST_USER)
        self.assertTrue(achievements_page.is_compare_url(url), "Не открылась страница достижений")

    def testClickReviews(self):
        """Кнопка “Отзывы” в боковом меню. Переход на страницу Отзывы при нажатии"""
        reviews_page = ReviewsPage(driver=self.driver)

        self.settings_page.side_bar.click_reviews()

        url = self.driver.current_url
        reviews_page.change_path(TEST_USER)
        self.assertTrue(reviews_page.is_compare_url(url), "Не открылась страница отзывов")

    def testClickAwaitReviews(self):
        """Кнопка “Ожидает отзывы” в боковом меню. Переход на страницу ожидает отзывы при нажатии"""
        await_review_page = UserAwaitReviewsPage(driver=self.driver)

        self.settings_page.side_bar.click_review_awaits()

        url = self.driver.current_url
        self.assertTrue(await_review_page.is_compare_url(url), "Не открылась страница ожидающих отзывов")
