from helpers import Test

from pages import UserProductsPage, MainPage, RegistrationPage, ProductPage


class UserProductsTest(Test):
    def setUp(self):
        super().setUp()
        self.user_products_page = UserProductsPage(driver=self.driver)

    def __auth__(self):
        main_page = MainPage(driver=self.driver)

        main_page.open()
        main_page.login.auth()
        self.user_products_page.open()

    def testRedirectToRegistrationPage(self):
        """Успешный редирект на страницу регистрации при переходе по ссылке https://ykoya.ru/user/ad
        неавторизованного пользователя """
        registration_page = RegistrationPage(driver=self.driver)

        self.user_products_page.open()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testRedirectToRegistrationPageLogOut(self):
        """Успешный редирект на страницу регистрации при выходе из профиля """
        registration_page = RegistrationPage(driver=self.driver)

        self.__auth__()
        self.user_products_page.login.logout()

        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def testClickProduct(self):
        """Проверка, что при нажатии на товар открывается страница товара"""
        product_page = ProductPage(driver=self.driver)

        self.__auth__()

        product_id = self.user_products_page.product_card.get_product_id()
        self.user_products_page.product_card.click_product(product_id)

        url = self.driver.current_url
        product_page.change_path(product_id)
        self.assertTrue(product_page.is_compare_url(url), "Не открылась страница товара")