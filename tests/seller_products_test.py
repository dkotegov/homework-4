from consts import TEST_USER
from helpers import Test

from pages import SellerProductsPage, ProductPage


class SellerProductsTest(Test):
    def setUp(self):
        super().setUp()
        self.seller_products_page = SellerProductsPage(driver=self.driver)
        self.seller_products_page.change_path(TEST_USER)
        self.seller_products_page.open()

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product_page = ProductPage(driver=self.driver)

        product_id = self.seller_products_page.product_card.get_product_id()
        self.seller_products_page.product_card.click_product(product_id)

        url = self.driver.current_url
        product_page.change_path(product_id)
        self.assertTrue(product_page.is_compare_url(url), "Не открылась страница товара")

    def testLikeProductNotAuth(self):
        """Проверка, что без авторизации лайк поставить нельзя"""
        product_id = self.seller_products_page.product_card.get_product_id()

        self.seller_products_page.product_card.click_like_product(product_id)
        self.assertTrue(self.seller_products_page.login.is_opened(), "Не открылась авторизация")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        product_id = self.seller_products_page.product_card.get_product_id()
        self.seller_products_page.login.auth()

        self.seller_products_page.product_card.click_like_product(product_id)
        self.assertTrue(self.seller_products_page.product_card.is_product_liked(product_id), "Не удалось поставить лайк")

        self.seller_products_page.product_card.click_like_product(product_id)
        self.assertFalse(self.seller_products_page.product_card.is_product_liked(product_id), "Не удалось убрать лайк")
