import unittest
from selenium import webdriver

from pages.seller_products import SellerProductsPage
from pages.product_card import ProductCard
from pages.login import LoginPage
from pages.product import ProductPage


class SellerProductsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.seller_products = SellerProductsPage(driver=self.driver)
        self.seller_products.open()

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_id = product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Некорректный урл")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        login = LoginPage(driver=self.driver)
        product_card = ProductCard(driver=self.driver)

        product_card.like_product()
        self.assertTrue(login.is_opened(), "Не открыта авторизация")
        login.click_close()

        login.auth()

        index = product_card.like_product()
        self.assertTrue(product_card.check_like_product(index), "Не удалось поставить лайк")

        product_card.remove_like_product(index)
        self.assertFalse(product_card.check_remove_like_product(index), "Не удалось убрать лайк")

    def tearDown(self):
        self.driver.close()
