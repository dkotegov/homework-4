from helpers import Test

from pages import MainPage, SearchPage, ProductPage


class MainTest(Test):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(driver=self.driver)
        self.main_page.open()

    def testClickSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии на кнопку "Найти" открывает страница поиска"""
        search_page = SearchPage(driver=self.driver)
        text = "test"

        self.main_page.search.input_search_value(text)
        self.main_page.search.click_search()

        search_page.wait_page()
        url = self.driver.current_url
        search_page.change_path(text)
        self.assertTrue(search_page.is_compare_url(url), "Не открылась страница поиска")

    def testEnterSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии "Enter" открывает страница поиска"""
        search_page = SearchPage(driver=self.driver)
        text = "test"

        self.main_page.search.input_search_value(text)
        self.main_page.search.enter_search()

        search_page.wait_page()
        url = self.driver.current_url
        search_page.change_path(text)
        self.assertTrue(search_page.is_compare_url(url), "Не открылась страница поиска")

    def testClickCategory(self):
        """Проверка, что при нажатии на категорию открывается страница поиска"""
        search_page = SearchPage(driver=self.driver)

        self.main_page.search.click_category()

        search_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(search_page.is_compare_url(url), "Не открылась страница поиска")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product_page = ProductPage(driver=self.driver)

        product_id = self.main_page.product_card.get_product_id()
        self.main_page.product_card.click_product(product_id)

        product_page.wait_page()
        url = self.driver.current_url
        product_page.change_path(product_id)
        self.assertTrue(product_page.is_compare_url(url), "Не открылась страница товара")

    def testLikeProductNotAuth(self):
        """Проверка, что без авторизации лайк поставить нельзя"""
        product_id = self.main_page.product_card.get_product_id()

        self.main_page.product_card.click_like_product(product_id)
        self.assertTrue(self.main_page.login.is_opened(), "Не открылась авторизация")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        self.main_page.login.auth()

        product_id = self.main_page.product_card.get_product_id()

        self.main_page.product_card.click_like_product(product_id)
        self.main_page.product_card.wait_liked(product_id)
        self.assertTrue(self.main_page.product_card.is_product_liked(product_id), "Не удалось поставить лайк")

        self.main_page.product_card.click_like_product(product_id)
        self.main_page.product_card.wait_not_liked(product_id)
        self.assertFalse(self.main_page.product_card.is_product_liked(product_id), "Не удалось убрать лайк")
