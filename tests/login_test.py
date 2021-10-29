import unittest
from selenium import webdriver

from pages.login import LoginPage
from pages.registration import RegistrationPage


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.login = LoginPage(driver=self.driver)
        self.login.open()

    def testCloseAuth(self):
        """Проверка, что при попап открывается и закрывается"""
        self.login.open_auth()
        self.assertTrue(self.login.is_opened(), "Закрыта авторизация")
        self.login.click_close()
        self.assertFalse(self.login.is_opened(), "Открыта авторизация")

        # TODO: не работает click_outside (он не закрывает попап)
        # self.login.open_auth()
        # self.assertTrue(self.login.is_opened(), "Закрыта авторизация")
        # self.login.click_outside()
        # self.assertFalse(self.login.is_opened(), "Открыта авторизация")

    # def __test_telephone__(self, test):
    #     self.login.clear_telephone_value()
    #     self.login.input_telephone_value(test)
    #     self.login.enter_submit()
    #     # TODO: не понятно как проверять ошибку. У нас стандартная браузерная
    #     self.assertFalse(self.login.is_logined(), "Залогинен")
    #
    # def testErrorTelephoneInput(self):
    #     # авторизация с пустым телефоном
    #     test1 = ""
    #     # авторизация с телефоном, где меньше 10
    #     test2 = "111111111"
    #
    #     self.login.open_auth()
    #
    #     self.__test_telephone__(test1)
    #     self.__test_telephone__(test2)
    #
    # def __test_password__(self, test):
    #     self.login.clear_password_value()
    #     self.login.input_password_value(test)
    #     self.login.enter_submit()
    #     # TODO: не понятно как проверять ошибку. У нас стандартная браузерная
    #     self.assertFalse(self.login.is_logined(), "Залогинен")
    #
    # def testErrorPasswordInput(self):
    #     # авторизация с пустым паролем
    #     test1 = ""
    #     # авторизация с телефоном, где меньше 10
    #     test2 = "Qwerty12"
    #
    #     self.login.open_auth()
    #
    #     self.__test_password__(test1)
    #     self.__test_password__(test2)

    def testClickRegistration(self):
        """Проверка, что при нажатии кнопки "Создайте аккаунт" открывается страница регистрации"""
        registration = RegistrationPage(driver=self.driver)

        self.login.open_auth()
        self.login.click_registration()

        url = self.driver.current_url
        self.assertTrue(registration.is_compare_url(url), "Некорректный урл")

    def __test_login__(self, telephone, password):
        self.login.clear_telephone_value()
        self.login.input_telephone_value(telephone)
        self.login.clear_password_value()
        self.login.input_password_value(password)

        self.login.enter_submit()
        self.assertFalse(self.login.is_logined(), "Залогинен")

    def testErrorLogin(self):
        """Проверка ошибочной авторизации"""
        # TODO: поменять когда добавим login в ENV

        # авторизация с неправильным телефоном
        telephone1 = "0000000000"
        password1 = "Qwerty123"

        # авторизация с неправильным паролем
        telephone2 = "4444444444"
        password2 = "Qwerty12"

        self.login.open_auth()

        self.__test_login__(telephone1, password1)
        self.__test_login__(telephone2, password2)

    def testSuccessLogin(self):
        """Проверка успешной авторизации"""
        # TODO: поменять когда добавим login в ENV
        telephone = "4444444444"
        password = "Qwerty123"

        self.login.open_auth()
        self.login.input_telephone_value(telephone)
        self.login.input_password_value(password)

        self.login.enter_submit()
        self.assertTrue(self.login.is_logined(), "Не залогинен")

    def tearDown(self):
        self.driver.close()
