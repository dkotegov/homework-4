from helpers import Test

from pages import MainPage, SearchPage, ProductPage


class MainTest(Test):
    def setUp(self):
        super().setUp()
        self.main = MainPage(driver=self.driver)
        self.main.open()

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку "Найти" открывает страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.search.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Не открылась страница поиска")

    def testClickSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии на кнопку "Найти" открывает страница поиска"""
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.search.input_search_value(text)
        self.main.search.click_search()

        url = self.driver.current_url
        search.change_path(text)
        self.assertTrue(search.is_compare_url(url), "Не открылась страница поиска")

    def testEnterSearch(self):
        """Проверка, что в поиске при нажатии "Enter" открывает страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.search.enter_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Не открылась страница поиска")

    def testEnterSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии "Enter" открывает страница поиска"""
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.search.input_search_value(text)
        self.main.search.enter_search()

        url = self.driver.current_url
        search.change_path(text)
        self.assertTrue(search.is_compare_url(url), "Не открылась страница поиска")

    def testClickCategory(self):
        """Проверка, что при нажатии на категорию открывается страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.search.click_category()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Не открылась страница поиска")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)

        product_id = self.main.product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        self.main.product_card.like_product()
        self.assertTrue(self.main.login.is_opened(), "Не открылась авторизация")
        self.main.login.click_close()

        self.main.login.auth()

        index = self.main.product_card.like_product()
        self.assertTrue(self.main.product_card.check_like_product(), "Не удалось поставить лайк")

        self.main.product_card.remove_like_product(index)
        self.assertFalse(self.main.product_card.check_remove_like_product(index), "Не удалось убрать лайк")
