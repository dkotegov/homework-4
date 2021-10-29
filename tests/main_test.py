import unittest
from selenium import webdriver

from pages.main import MainPage
from pages.product_card import ProductCard
from pages.search import SearchPage
from pages.product import ProductPage
from pages.login import LoginPage


class MainTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.main = MainPage(driver=self.driver)
        self.product_card = ProductCard(driver=self.driver)
        self.main.open()

    def testClickSearch(self):
        """Проверка, что при нажатии на кнопку "Найти" открывает страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.click_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии на кнопку "Найти" открывает страница поиска"""
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.input_search_value(text)
        self.main.click_search()

        url = self.driver.current_url
        search.change_path(text)
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testEnterSearch(self):
        """Проверка, что в поиске при нажатии "Enter" открывает страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.enter_search()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testEnterSearchWithParam(self):
        """Проверка, что при введенных данных в поиск и нажатии "Enter" открывает страница поиска"""
        search = SearchPage(driver=self.driver)
        text = "test"

        self.main.input_search_value(text)
        self.main.enter_search()

        url = self.driver.current_url
        search.change_path(text)
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickCategory(self):
        """Проверка, что при нажатии на категорию открывается страница поиска"""
        search = SearchPage(driver=self.driver)

        self.main.click_category()

        url = self.driver.current_url
        self.assertTrue(search.is_compare_url(url), "Некорректный урл")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)

        product_id = self.product_card.click_product()
        product.change_path(product_id)

        url = self.driver.current_url
        self.assertTrue(product.is_compare_url(url), "Некорректный урл")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        login = LoginPage(driver=self.driver)

        self.product_card.like_product()
        self.assertTrue(login.is_opened(), "Не открыта авторизация")
        login.click_close()

        login.auth()

        index = self.product_card.like_product()
        self.assertTrue(self.product_card.check_like_product(index), "Не удалось поставить лайка")

        self.product_card.remove_like_product(index)
        self.assertFalse(self.product_card.check_remove_like_product(index), "Не удалось убрать лайк")

    def tearDown(self):
        self.driver.close()
