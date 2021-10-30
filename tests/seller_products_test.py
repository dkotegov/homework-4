from helpers import Test

from pages import SellerProductsPage, ProductPage


class SellerProductsTest(Test):
    def setUp(self):
        super().setUp()
        self.seller_products = SellerProductsPage(driver=self.driver)
        self.seller_products.open()

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)

        product_id = self.seller_products.product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")

    def testLikeProduct(self):
        """
            Лайк товара при нажатии кнопки "лайк",
            Снятие лайка с товара при нажатии кнопки "дизлайк"
        """
        self.seller_products.product_card.like_product()
        self.assertTrue(self.seller_products.login.is_opened(), "Не открыта авторизация")
        self.seller_products.login.click_close()

        self.seller_products.login.auth()

        index = self.seller_products.product_card.like_product()
        self.assertTrue(self.seller_products.product_card.check_like_product(), "Не удалось поставить лайк")

        self.seller_products.product_card.remove_like_product(index)
        self.assertFalse(self.seller_products.product_card.check_remove_like_product(index), "Не удалось убрать лайк")
