import time
import unittest
from selenium import webdriver

from pages.registration import RegistrationPage


class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.registration = RegistrationPage(driver=self.driver)
        self.registration.open()

    def __test_name__(self, test):
        self.registration.clear_name_value()
        self.registration.input_name_value(test)
        self.registration.enter_submit()
        self.assertTrue(self.registration.is_error_name(), "Нет ошибки")

    def testErrorNameInput(self):
        """Проверка регистрации с неправильными данными имени"""
        # регистрация с пустым именем
        test1 = ""
        # регистрация с именем, где больше 30 символов
        test2 = "1111111111111111111111111111111"

        self.__test_name__(test1)
        self.__test_name__(test2)

    def __test_surname__(self, test):
        self.registration.clear_surname_value()
        self.registration.input_surname_value(test)
        self.registration.enter_submit()
        self.assertTrue(self.registration.is_error_surname(), "Нет ошибки")

    def testErrorSurnameInput(self):
        """Проверка регистрации с неправильными данными фамилии"""
        # регистрация с пустой фамилией
        test1 = ""
        # регистрация с фамилией, где больше 30 символов
        test2 = "1111111111111111111111111111111"

        self.__test_surname__(test1)
        self.__test_surname__(test2)

    def __test_telephone__(self, test):
        self.registration.clear_telephone_value()
        self.registration.input_telephone_value(test)
        self.registration.enter_submit()
        self.assertTrue(self.registration.is_error_telephone(), "Нет ошибки")

    def testErrorTelephoneInput(self):
        """Проверка регистрации с неправильными данными телефона"""
        # регистрация с пустым телефоном
        test1 = ""
        # регистрация с телефоном, где меньше 10
        test2 = "111111111"

        self.__test_telephone__(test1)
        self.__test_telephone__(test2)

    def __test_password__(self, test):
        self.registration.clear_password_value()
        self.registration.input_password_value(test)
        self.registration.enter_submit()
        self.assertTrue(self.registration.is_error_password(), "Нет ошибки")

    def testErrorPasswordInput(self):
        """Проверка регистрации с неправильными данными пароля"""
        # регистрация с пустым паролем
        test1 = ""
        # регистрация с паролем, где меньше 6 символов
        test2 = "11111"
        # регистрация с паролем, где нет хотя бы одной цифры
        test3 = "qwerty"
        # регистрация с паролем, где нет хотя бы одной буквы в нижнем регистре
        test4 = "qwerty1"
        # регистрация с паролем, где нет хотя бы одной буквы в верхнем регистре
        test5 = "QWERTY1"
        # регистрация с паролем, где больше 30 символов
        test6 = "Qwerty1111111111111111111111111111111"

        self.__test_password__(test1)
        self.__test_password__(test2)
        self.__test_password__(test3)
        self.__test_password__(test4)
        self.__test_password__(test5)
        self.__test_password__(test6)

    def __test__confirm_password__(self, test, confirm_test):
        self.registration.clear_password_value()
        self.registration.input_password_value(test)
        self.registration.clear_confirm_password_value()
        self.registration.input_confirm_password_value(confirm_test)

        self.registration.enter_submit()
        self.assertTrue(self.registration.is_error_confirm_password(), "Нет ошибки")

    def testErrorConfirmPasswordInput(self):
        """Проверка регистрации с неправильными данными пароля и подтверждения пароля"""
        # регистрация, когда пароль и подтверждение пароля не совпадает
        test_password = "Qwerty12"
        test_confirm_password = "Qwerty11"

        self.__test__confirm_password__(test_password, test_confirm_password)

    def __test_email__(self, test):
        self.registration.clear_email_value()
        self.registration.input_email_value(test)
        self.registration.enter_submit()
        self.assertTrue(self.registration.is_error_email(), "Нет ошибки")

    def testErrorEmailInput(self):
        """Проверка регистрации с неправильными данными почты"""
        # регистрация, когда в почте нет знака @
        test1 = "test.ru"
        # регистрация, когда в почте нет символов до знака @
        test2 = "@test.ru"
        # регистрация, когда в почте нет символов после знака @
        test3 = "test@.ru"
        # регистрация, когда в почте нет .domen
        test4 = "test@test"

        self.__test_email__(test1)
        self.__test_email__(test2)
        self.__test_email__(test3)
        self.__test_email__(test4)

    def testErrorRegistrationExistTelephone(self):
        """Проверка ошибочной регистрации"""
        name = "name"
        surname = "surname"
        # TODO: поменять когда добавим login в ENV
        telephone = "4444444444"
        password = "Qwerty12"
        confirm_password = "Qwerty12"

        self.registration.input_name_value(name)
        self.registration.input_surname_value(surname)
        self.registration.input_telephone_value(telephone)
        self.registration.input_password_value(password)
        self.registration.input_confirm_password_value(confirm_password)
        self.registration.enter_submit()
        text = self.registration.get_registration_error()
        self.assertEqual(text, "Пользователь уже существует", "Нет ошибки")

    def tearDown(self):
        self.driver.close()
