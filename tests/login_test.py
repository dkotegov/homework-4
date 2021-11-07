import os

from helpers import Test

from pages import MainPage, RegistrationPage


class LoginTest(Test):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(driver=self.driver)
        self.main_page.open()

    def testCloseAuth(self):
        """Проверка, что при попап открывается и закрывается"""
        self.main_page.login.open_auth()
        self.main_page.login.click_close()
        self.assertFalse(self.main_page.login.is_opened(), "Не закрылась авторизация")

        self.main_page.login.open_auth()
        self.main_page.login.click_outside()
        self.assertFalse(self.main_page.login.is_opened(), "Не закрылась авторизация")

    def __test_telephone__(self, test):
        self.main_page.login.input_telephone_value(test)

        self.main_page.login.enter_submit()
        self.assertTrue(self.main_page.login.is_error_telephone(), "Нет ошибки")

    def testErrorTelephoneInput(self):
        # авторизация с пустым телефоном
        test1 = ""
        # авторизация с телефоном, где меньше 10
        test2 = "111111111"

        self.main_page.login.open_auth()

        self.__test_telephone__(test1)
        self.__test_telephone__(test2)

    def __test_password__(self, test):
        self.main_page.login.input_password_value(test)

        self.main_page.login.enter_submit()
        self.assertTrue(self.main_page.login.is_error_password(), "Нет ошибки")

    def testErrorPasswordInput(self):
        # авторизация с пустым паролем
        test1 = ""
        # авторизация с телефоном, где меньше 10
        test2 = "Qwerty12"

        self.main_page.login.open_auth()

        self.__test_password__(test1)
        self.__test_password__(test2)

    def testClickRegistration(self):
        """Проверка, что при нажатии кнопки "Создайте аккаунт" открывается страница регистрации"""
        registration_page = RegistrationPage(driver=self.driver)

        self.main_page.login.open_auth()
        self.main_page.login.click_registration()

        registration_page.wait_page()
        url = self.driver.current_url
        self.assertTrue(registration_page.is_compare_url(url), "Не открылась страница регистрации")

    def __test_login__(self, telephone, password):
        self.main_page.login.input_telephone_value(telephone)
        self.main_page.login.input_password_value(password)

        self.main_page.login.enter_submit()
        self.assertTrue(self.main_page.login.is_error_form(), "Пользователь авторизовался")

    def testErrorLogin(self):
        """Проверка ошибочной авторизации"""
        # авторизация с неправильным телефоном
        telephone1 = "0000000000"
        password1 = os.environ.get("PASSWORD")

        # авторизация с неправильным паролем
        telephone2 = os.environ.get("LOGIN")
        password2 = os.environ.get("PASSWORD") + "1"

        self.main_page.login.open_auth()

        self.__test_login__(telephone1, password1)
        self.__test_login__(telephone2, password2)

    def testSuccessLogin(self):
        """Проверка успешной авторизации"""
        telephone = os.environ.get("LOGIN")
        password = os.environ.get("PASSWORD")

        self.main_page.login.open_auth()
        self.main_page.login.input_telephone_value(telephone)
        self.main_page.login.input_password_value(password)

        self.main_page.login.enter_submit()
        self.assertTrue(self.main_page.login.is_logined(), "Пользователь не авторизовался")
