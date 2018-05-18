# -*- coding: utf-8 -*-

import unittest

import os

import time
from selenium.webdriver import DesiredCapabilities, Remote

from constants import profiles
from pages.auth_page import AuthPage
from pages.base_settings_page import BaseSettingsPage
from pages.main_page import MainPage


class TestsBaseSettings(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()



#     def test_name_surname(self):
#         name = "Name1"
#         surname = "Surname1"
#
#         auth_page = AuthPage(self.driver)
#         auth_page.open('')
#
#         auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)
#
#         base_settings_page = BaseSettingsPage(self.driver)
#         base_settings_page.open('/settings')
#         personal_data = base_settings_page.personal_data()
#         personal_data.name_surname(name, surname)
#         personal_data.save()
#         personal_data.close_save()
#
#         name_surname = base_settings_page.profile_get()
#         self.assertEqual(name + " " + surname, name_surname)
#         base_settings_page.profile()
#
#         main_page = MainPage(self.driver)
#         name_surname = main_page.my_name_surname()
#         self.assertEqual(name + " " + surname, name_surname)
#
#     def test_name_surname_error(self):
#         name = "Name_1"
#         surname = "Surname_1"
#         error = u"Пожалуйста, используйте только буквы."
#
#         auth_page = AuthPage(self.driver)
#         auth_page.open('')
#
#         auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)
#
#         base_settings_page = BaseSettingsPage(self.driver)
#         base_settings_page.open('/settings')
#         personal_data = base_settings_page.personal_data()
#         personal_data.name_surname(name, surname)
#         personal_data.save()
#
#         e1, e2 = personal_data.name_surname_error()
#
#         self.assertEqual(error, e1)
#         self.assertEqual(error, e2)
#
# # не выбирается день рождения
#     def test_birthday(self):
#         birthday = u"5 марта 1996 (22 года)"
#
#         auth_page = AuthPage(self.driver)
#         auth_page.open('')
#
#         auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)
#
#         base_settings_page = BaseSettingsPage(self.driver)
#         base_settings_page.open('/settings')
#         personal_data = base_settings_page.personal_data()
#
#
#         personal_data.birthday()
#         personal_data.save()
#         personal_data.close_save()
#
#         base_settings_page.profile()
#         main_page = MainPage(self.driver)
#         my_birthday = main_page.my_birthday()
#
#         self.assertEqual(birthday, my_birthday)

    def test_birthday_error(self):
        error = u"День вашего рождения указан некорректно."

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        personal_data = base_settings_page.personal_data()

        personal_data.birthday_error()
        personal_data.save()

        e = personal_data.get_birthday_error() # не успевает
        self.assertEqual(e, error)



    def test_phone_number(self):

        number = "9999977771"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK43, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        phone_number.ok_button2()     # если появилась кнопка подтвержить код, то номер телефона принят

    def test_phone_number_error(self):

        number = "999a997777"
        error = u"Ошибки:\n" + u"В номере неверное количество цифр"

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        phone_number = base_settings_page.phone_number()
        phone_number.set_number(number)
        phone_number.ok_button_click()
        e = phone_number.number_error()
        self.assertEqual(e, error)

    def test_email(self):

        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        email = base_settings_page.email()
        email.set_email("jsd@sda.asd")
        email.set_password(profiles.PROFILE_PASSWORD)
        email.save_button_click()

        base_settings_page.phone_number() # могу зайти в другое меню настроик, значит почта принята


    def test_email_error_password(self):

        error = u"Введите ваш пароль"
        auth_page = AuthPage(self.driver)
        auth_page.open('')

        auth_page.login(profiles.PROFILE_TECHNOPARK46, profiles.PROFILE_PASSWORD)

        base_settings_page = BaseSettingsPage(self.driver)
        base_settings_page.open('/settings')
        email = base_settings_page.email()
        email.set_email("jsd@sda.asd")
        email.set_password("")
        email.save_button_click()
        e = email.get_error_password()
        self.assertEqual(e, error)








