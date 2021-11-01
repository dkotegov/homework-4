import os

from helpers import Test
from pages import MainPage

from pages.user_settings import UserSettingsPage


class SettingsTest(Test):
    def setUp(self):
        super().setUp()
        self.main_page = MainPage(driver=self.driver)
        self.main_page.open()
        self.main_page.login.auth()
        self.settings = UserSettingsPage(driver=self.driver)
        self.settings.open()

    def __test_name__(self, test):
        self.settings.form.clear_name_value()
        self.settings.form.input_name_value(test)
        self.settings.form.enter_info_submit()
        self.assertTrue(self.settings.form.is_error_name(), "Нет ошибки")

    def testErrorNameInput(self):
        """Проверка сохранения с неправильными данными имени"""
        # сохранение с пустым именем
        test1 = ""
        # сохранение с именем, где больше 30 символов
        test2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        self.settings.form.enter_info_edit()
        self.__test_name__(test1)
        self.__test_name__(test2)

    def __test_surname__(self, test):
        self.settings.form.clear_surname_value()
        self.settings.form.input_surname_value(test)
        self.settings.form.enter_info_submit()
        self.assertTrue(self.settings.form.is_error_surname(), "Нет ошибки")

    def testErrorSurnameInput(self):
        """Проверка сохранения с неправильными данными фамилии"""
        # сохранение с пустой фамилией
        test1 = ""
        # сохранение с фамилией, где больше 30 символов
        test2 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

        self.settings.form.enter_info_edit()
        self.__test_surname__(test1)
        self.__test_surname__(test2)

    def __test_email__(self, test):
        self.settings.form.clear_email_value()
        self.settings.form.input_email_value(test)
        self.settings.form.enter_info_submit()
        self.assertTrue(self.settings.form.is_error_email(), "Нет ошибки")

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

        self.settings.form.enter_info_edit()
        self.__test_email__(test1)
        self.__test_email__(test2)
        self.__test_email__(test3)
        self.__test_email__(test4)

    def __test_password__(self, test):
        old_password = os.environ.get("PASSWORD")
        self.settings.pwd_form.clear_password_value()
        self.settings.pwd_form.input_password_value(test)

        self.settings.pwd_form.clear_old_password_value()
        self.settings.pwd_form.input_old_password_value(old_password)
        self.settings.pwd_form.enter_pwd_submit()
        self.assertTrue(self.settings.pwd_form.is_error_password(), "Нет ошибки")

    def testErrorPasswordInput(self):
        """Проверка сохранения с неправильными данными пароля"""
        # сохранение с паролем, где меньше 6 символов
        test2 = "11111"
        # сохранение с паролем, где нет хотя бы одной цифры
        test3 = "qwerty"
        # сохранение с паролем, где нет хотя бы одной буквы в нижнем регистре
        test4 = "qwerty1"
        # сохранение с паролем, где нет хотя бы одной буквы в верхнем регистре
        test5 = "QWERTY1"
        # сохранение с паролем, где больше 30 символов
        test6 = "Qwerty1111111111111111111111111111111"

        self.__test_password__(test2)
        self.__test_password__(test3)
        self.__test_password__(test4)
        self.__test_password__(test5)
        self.__test_password__(test6)

    def __test__confirm_password__(self, test, confirm_test):
        old_password = os.environ.get("PASSWORD")

        self.settings.pwd_form.clear_password_value()
        self.settings.pwd_form.input_password_value(test)
        self.settings.pwd_form.clear_confirm_password_value()
        self.settings.pwd_form.input_confirm_password_value(confirm_test)

        self.settings.pwd_form.clear_old_password_value()
        self.settings.pwd_form.input_old_password_value(old_password)
        self.settings.pwd_form.enter_pwd_submit()
        self.assertTrue(self.settings.pwd_form.is_error_confirm_password(), "Нет ошибки")

    def testErrorConfirmPasswordInput(self):
        """Проверка сохранения с неправильными данными пароля и подтверждения пароля"""
        # сохранение, когда пароль и подтверждение пароля не совпадает
        test_password = "Qwerty12"
        test_confirm_password = "Qwerty11"

        self.__test__confirm_password__(test_password, test_confirm_password)

    def testChangeTheme(self):
        """Проверка смены темы"""
        theme_0 = self.settings.theme_form.get_theme()
        if theme_0 == "dark":
            self.settings.theme_form.change_theme_light()
        else:
            self.settings.theme_form.change_theme_dark()

        theme_1 = self.settings.theme_form.get_theme()
        self.assertNotEqual(theme_0, theme_1, "Одинаковые темы")

        if theme_1 == "dark":
            self.settings.theme_form.change_theme_light()
        else:
            self.settings.theme_form.change_theme_dark()

        theme_2 = self.settings.theme_form.get_theme()
        self.assertEqual(theme_0, theme_2, "Разные темы")
        self.assertNotEqual(theme_1, theme_2, "Одинаковые темы")

    def __test__change_password__(self, old, new, confirm):
        self.settings.pwd_form.clear_password_value()
        self.settings.pwd_form.input_password_value(new)
        self.settings.pwd_form.clear_confirm_password_value()
        self.settings.pwd_form.input_confirm_password_value(confirm)
        self.settings.pwd_form.clear_old_password_value()
        self.settings.pwd_form.input_old_password_value(old)

        self.assertEqual(self.settings.pwd_form.get_pwd_change_error(), '', "Нет ошибки")

        self.settings.pwd_form.clear_password_value()
        self.settings.pwd_form.input_password_value(old)
        self.settings.pwd_form.clear_confirm_password_value()
        self.settings.pwd_form.input_confirm_password_value(old)
        self.settings.pwd_form.clear_old_password_value()
        self.settings.pwd_form.input_old_password_value(new)

        self.assertEqual(self.settings.pwd_form.get_pwd_change_error(), '', "Нет ошибки")

    def testPasswordChange(self):
        """Проверка успешной смены пароля"""
        old_pwd = os.environ.get("PASSWORD")
        new_pwd = "Qwertyyy12344"
        conf_pwd = "Qwertyyy12344"

        self.__test__change_password__(old_pwd, new_pwd, conf_pwd)
