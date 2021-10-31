from helpers import Test

from pages import UserProductsPage, RegistrationPage, ProductPage


class UserProductsTest(Test):
    def setUp(self):
        super().setUp()
        self.user_products = UserProductsPage(driver=self.driver)
        self.user_products.open()

    def testRedirectToRegPage(self):
        """Успешный редирект на страницу регистрации при переходе по ссылке https://ykoya.ru/user/ad
        неавторизованного пользователя """
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegPageLogOut(self):
        """Успешный редирект на страницу регистрации при выходе из профиля """
        registration = RegistrationPage(driver=self.driver)

        self.user_products.login.auth()
        self.user_products.open()
        self.user_products.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product = ProductPage(driver=self.driver)

        self.user_products.login.auth()
        self.user_products.open()

        product_id = self.user_products.product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")
