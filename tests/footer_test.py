from helpers import Test

from pages import MainPage, SearchPage, RegistrationPage, CreateProductPage, UserMessagesPage, UserSettingsPage, \
    UserProductsPage, UserFavoritesPage


class FooterTest(Test):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(driver=self.driver)
        self.main_page.open()

    def testClickCreate(self):
        """Проверка, что при нажатии на кнопку "Разместить объявление" открывается страница создания товара"""
        create_product_page = CreateProductPage(driver=self.driver)

        self.main_page.footer.click_create()
        self.assertTrue(self.main_page.login.is_opened(), "Не открылась авторизация")
        self.main_page.login.click_close()

        self.main_page.login.auth()
        self.main_page.footer.click_create()

        url = self.driver.current_url
        self.assertTrue(create_product_page.is_compare_url(url), "Не открылась страница создания товара")

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку "Поиск" открывается страница поиска"""
        search_page = SearchPage(driver=self.driver)

        self.main_page.footer.click_search()

        url = self.driver.current_url
        self.assertTrue(search_page.is_compare_url(url), "Не открылась страница поиска")

    def testClickSettings(self):
        """Проверка, что при нажатии на кнопку "Настройки" открывается страница настроек"""
        settings_page = UserSettingsPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.footer.click_settings()

        url = self.driver.current_url
        self.assertTrue(settings_page.is_compare_url(url), "Не открылась страница настроек")

    def testClickProducts(self):
        """Проверка, что при нажатии на кнопку "Мои объявления" открывается страница моих объявлений"""
        user_products_page = UserProductsPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.footer.click_products()

        url = self.driver.current_url
        self.assertTrue(user_products_page.is_compare_url(url), "Не открылась страница моих объявлений")

    def testClickMessages(self):
        """Проверка, что при нажатии на кнопку "Мои сообщения" открывается страница чатов"""
        messages_page = UserMessagesPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.footer.click_messages()

        url = self.driver.current_url
        self.assertTrue(messages_page.is_compare_url(url), "Не открылась страница чатов")

    def testClickFavorite(self):
        """Проверка, что при нажатии на кнопку "Избранное" открывается страница избранных товаров"""
        favorites_page = UserFavoritesPage(driver=self.driver)

        self.main_page.login.auth()
        self.main_page.footer.click_favorites()

        url = self.driver.current_url
        self.assertTrue(favorites_page.is_compare_url(url), "Не открылась страница избранных товаров")

    def testClickRegistration(self):
        """Проверка, что при нажатии на кнопку "Регистрация" открывается страница регистрации"""
        registration_page = RegistrationPage(driver=self.driver)

        self.main_page.footer.click_registration()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testClickAuth(self):
        """Проверка, что при нажатии на кнопку "Авторизация" открывается попап авторизации"""
        self.main_page.footer.click_auth()

        self.assertTrue(self.main_page.login.is_opened(), "Не открылась авторизация")
