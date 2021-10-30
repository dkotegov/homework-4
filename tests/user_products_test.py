from helpers import Test

from pages import UserProductsPage, UserChats, RegistrationPage, ProductPage


class UserProductsTest(Test):
    def setUp(self):
        super().setUp()
        self.user_products_page = UserProductsPage(driver=self.driver)
        self.user_products_page.open()

    def testRedirectToRegPage(self):
        """Успешный редирект на страницу регистрации при переходе по ссылке https://ykoya.ru/user/ad
        неавторизованного пользователя """
        registration = RegistrationPage(driver=self.driver)

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegPageLogOut(self):
        """Успешный редирект на страницу регистрации при выходе из профиля """
        registration = RegistrationPage(driver=self.driver)

        self.user_products_page.login.auth()
        self.user_products_page.open()
        self.user_products_page.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectFromFooterToUserProducts(self):
        """Успешный редирект на страницу "Мои объявления" при нажатии кнопки в нижнем меню сайта “Мои объявления”"""
        self.user_products_page.login.auth()

        self.user_products_page.footer.click_ad()

        url = self.driver.current_url
        self.assertTrue(self.user_products_page.is_compare_url(url), "Не открылась страница Мои объявления")

    def testRedirectFromSettingsToUserProducts(self):
        """Успешный редирект на страницу "Мои объявления" при нажатии кнопки в боковом меню “Мои объявления”"""
        self.user_products_page.login.auth()

        self.user_products_page.settings_card.click_ad()

        url = self.driver.current_url
        self.assertTrue(self.user_products_page.is_compare_url(url), "Не открылась страница Мои объявления")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        self.user_products_page.login.auth()
        self.user_products_page.open()

        product = ProductPage(driver=self.driver)

        product_id = self.user_products_page.product_card.click_product()

        url = self.driver.current_url
        product.change_path(product_id)
        self.assertTrue(product.is_compare_url(url), "Не открылась страница товара")
