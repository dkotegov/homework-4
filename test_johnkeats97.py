# -*- coding: utf-8 -*-

import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from pages.auth_page import AuthPage
from pages.base_settings_page import BaseSettingsPage
from pages.main_page import MainPage

from constants import profiles
from constants import name_surname
from constants import birthday
from constants import phone


class TestsBaseSettings(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', profiles.BROWSER)

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()



    def test_name_surname_letters(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()

        personal_data.set_name_surname_all(name_surname.NAME_LETTERS, name_surname.SURNAME_LETTERS)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_LETTERS + " " + name_surname.SURNAME_LETTERS, new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_LETTERS + " " + name_surname.SURNAME_LETTERS, new_name_surname)


    def test_name_surname_letters_small(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK42, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname_all(name_surname.NAME_LETTERS_SMALL, name_surname.SURNAME_LETTERS_SMALL)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_LETTERS_SMALL + " " + name_surname.SURNAME_LETTERS_SMALL, new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_LETTERS_SMALL + " " + name_surname.SURNAME_LETTERS_SMALL, new_name_surname)


    def test_name_surname_letters_capital(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname_all(name_surname.NAME_LETTERS_CAPITAL, name_surname.SURNAME_LETTERS_CAPITAL)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_LETTERS_CAPITAL + " " + name_surname.SURNAME_LETTERS_CAPITAL, new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_LETTERS_CAPITAL + " " + name_surname.SURNAME_LETTERS_CAPITAL, new_name_surname)

    def test_name_surname_digits(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK11, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname_all(name_surname.NAME_DIGITS, name_surname.SURNAME_DIGITS)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_DIGITS + " " + name_surname.SURNAME_DIGITS, new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_DIGITS + " " + name_surname.SURNAME_DIGITS, new_name_surname)

    def test_name_surname_letters_digits(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK12, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname_all(name_surname.NAME_LETTERS_DIGITS, name_surname.SURNAME_LETTERS_DIGITS)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_LETTERS_DIGITS + " " + name_surname.SURNAME_LETTERS_DIGITS, new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_LETTERS_DIGITS + " " + name_surname.SURNAME_LETTERS_DIGITS, new_name_surname)

    def test_name_surname_error_symbols(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname(name_surname.NAME_ERROR_SYMBOLS, name_surname.SURNAME_ERROR_SYMBOLS)

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(name_surname.ERROR_SYMBOLS, e1)
        self.assertEqual(name_surname.ERROR_SYMBOLS, e2)

    def test_name_surname_long_ok(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK13, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.name_surname_send_keys(name_surname.NAME_LETTERS * 100, name_surname.SURNAME_LETTERS * 100)
        personal_data.save()
        personal_data.close_save()

        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(41, len(new_name_surname))

    def test_name_surname_long_error(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname(name_surname.NAME_LETTERS * 100, name_surname.SURNAME_LETTERS * 100)

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(name_surname.ERROR_LONG, e1)
        self.assertEqual(name_surname.ERROR_LONG, e2)

    def test_name_surname_error_void(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname(name_surname.NAME_VOID, name_surname.SURNAME_VOID)

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(name_surname.ERROR_NAME_VOID, e1)
        self.assertEqual(name_surname.ERROR_SURNAME_VOID, e2)

    def test_name_surname_error_space(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname(name_surname.NAME_SPACE * 10, name_surname.SURNAME_SPACE * 10)

        e1, e2 = personal_data.name_surname_error()

        self.assertEqual(name_surname.ERROR_NAME_VOID, e1)
        self.assertEqual(name_surname.ERROR_SURNAME_VOID, e2)

    def test_name_surname_long_space(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK19, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname_all(name_surname.NAME_SPACE_LONG, name_surname.SURNAME_SPACE_LONG)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_SPACE_LONG.strip() + " " + name_surname.SURNAME_SPACE_LONG.strip(), new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_SPACE_LONG.strip() + " " + name_surname.SURNAME_SPACE_LONG.strip(), new_name_surname)

    def test_name_surname_space(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK14, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.set_name_surname_all(name_surname.NAME_SPACE_LETTERS, name_surname.SURNAME_SPACE_LETTERS)

        new_name_surname = base_settings_page.profile_get()
        self.assertEqual(name_surname.NAME_SPACE_LETTERS + " " + name_surname.SURNAME_SPACE_LETTERS, new_name_surname)
        base_settings_page.profile()

        main_page = MainPage(self.driver)
        new_name_surname = main_page.my_name_surname()
        self.assertEqual(name_surname.NAME_SPACE_LETTERS + " " + name_surname.SURNAME_SPACE_LETTERS, new_name_surname)


    def test_birthday(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()

        personal_data.birthday()
        personal_data.save()
        personal_data.close_save()

        base_settings_page.profile()
        main_page = MainPage(self.driver)
        my_birthday = main_page.my_birthday()

        self.assertEqual(birthday.BIRTHDAY, my_birthday)

    def test_birthday_error_29(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()

        personal_data.birthday_error_29()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, birthday.ERROR_BIRTNDAY)


    def test_birthday_error_void(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        personal_data = base_settings_page.personal_data()

        personal_data.birthday_error_void_day()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, birthday.ERROR_BIRTNDAY)

        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.birthday_error_void_month()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, birthday.ERROR_BIRTNDAY)

        base_settings_page.open()
        personal_data = base_settings_page.personal_data()
        personal_data.birthday_error_void_year()
        personal_data.save()

        e = personal_data.get_birthday_error()
        self.assertEqual(e, birthday.ERROR_BIRTNDAY)


    def test_phone_number_error_symbol(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        phone_number = base_settings_page.phone_number()
        phone_number.set_number_all(phone.NUMBER_ERROR_SYMBOL)
        e = phone_number.number_error()
        self.assertEqual(e, phone.NUMBER_ERROR)

    def test_phone_number_error_small(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        phone_number = base_settings_page.phone_number()
        phone_number.set_number_all(phone.NUMBER_ERROR_SMALL)
        e = phone_number.number_error()
        self.assertEqual(e, phone.NUMBER_ERROR)

    def test_phone_number_error_long(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        phone_number = base_settings_page.phone_number()
        phone_number.set_number_all(phone.NUMBER_ERROR_LONG)
        e = phone_number.number_error()
        self.assertEqual(e, phone.NUMBER_ERROR)

    def test_phone_number_error_void(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        phone_number = base_settings_page.phone_number()
        phone_number.set_number_all(phone.NUMBER_VOID)
        e = phone_number.number_error()
        self.assertEqual(e, phone.ERROR_VOID)

    def test_phone_number_error_space(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        phone_number = base_settings_page.phone_number()
        phone_number.set_number_all(phone.NUMBER_SPACE)
        e = phone_number.number_error()
        self.assertEqual(e, phone.ERROR_VOID)

    def test_phone_number(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_page.login(profiles.PROFILE_TECHNOPARK49, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open()
        phone_number = base_settings_page.phone_number()
        phone_number.set_number_all(phone.NUMBER)
        phone_number.ok_button2()






