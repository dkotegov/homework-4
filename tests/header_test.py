from consts import TEST_USER
from helpers import Test

from pages import MainPage, SearchPage, CreateProductPage, UserMessagesPage, UserSettingsPage, \
    UserProductsPage, UserFavoritesPage, ReviewsPage, AchievementsPage


class HeaderTest(Test):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(driver=self.driver)
        self.main_page.open()

    def testClickLogo(self):
        """Проверка, что при нажатии на логотип открывается главная страница"""
        search_page = SearchPage(driver=self.driver)

        search_page.open()
        search_page.header.click_logo()

        url = self.driver.current_url
        self.assertTrue(self.main_page.is_compare_url(url), "Не открылась главная страница")

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку поиска открывается страница поиска"""
        search_page = SearchPage(driver=self.driver)

        self.main_page.header.click_search()

        url = self.driver.current_url
        self.assertTrue(search_page.is_compare_url(url), "Не открылась страница поиска")

    def testClickCreateNotAuth(self):
        """Проверка, что при нажатии на кнопку "Разместить объявление" открывается авторизация, без авторизации"""
        self.main_page.footer.click_create()
        self.assertTrue(self.main_page.login.is_opened(), "Не открылась авторизация")

    def testClickCreate(self):
        """Проверка, что при нажатии на кнопку "Разместить объявление" открывается страница создания товара"""
        create_product_page = CreateProductPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_create()

        url = self.driver.current_url
        self.assertTrue(create_product_page.is_compare_url(url), "Не открылась страница создания товара")

    def testClickSettings(self):
        """Проверка, что при нажатии на кнопку "Настройки" открывается страница настроек"""
        settings_page = UserSettingsPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_dropdown()
        self.main_page.header.click_settings()

        url = self.driver.current_url
        self.assertTrue(settings_page.is_compare_url(url), "Не открылась страница настроек")

    def testClickProducts(self):
        """Проверка, что при нажатии на кнопку "Мои объявления" открывается страница моих объявлений"""
        user_products_page = UserProductsPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_dropdown()
        self.main_page.header.click_products()

        url = self.driver.current_url
        self.assertTrue(user_products_page.is_compare_url(url), "Не открылась страница моих объявлений")

    def testClickMessages(self):
        """Проверка, что при нажатии на кнопку "Мои сообщения" открывается страница чатов"""
        messages_page = UserMessagesPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_dropdown()
        self.main_page.header.click_messages()

        url = self.driver.current_url
        self.assertTrue(messages_page.is_compare_url(url), "Не открылась страница чатов")

    def testClickFavorite(self):
        """Проверка, что при нажатии на кнопку "Избранное" открывается страница избранных товаров"""
        favorites_page = UserFavoritesPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_dropdown()
        self.main_page.header.click_favorites()

        url = self.driver.current_url
        self.assertTrue(favorites_page.is_compare_url(url), "Не открылась страница избранных товаров")

    def testClickAchievements(self):
        """Проверка, что при нажатии на кнопку "Достижения" открывается страница достижений"""
        achievements_page = AchievementsPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_dropdown()
        self.main_page.header.click_achievements()

        url = self.driver.current_url
        achievements_page.change_path(TEST_USER)
        self.assertTrue(achievements_page.is_compare_url(url), "Не открылась страница достижений")

    def testClickReviews(self):
        """Проверка, что при нажатии на кнопку "Отзывы" открывается страница отзывов"""
        reviews_page = ReviewsPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.header.click_dropdown()
        self.main_page.header.click_reviews()

        url = self.driver.current_url
        reviews_page.change_path(TEST_USER)
        self.assertTrue(reviews_page.is_compare_url(url), "Не открылась страница отзывов")
