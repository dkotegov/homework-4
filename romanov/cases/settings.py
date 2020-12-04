import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote
from romanov.steps.auth import Steps as AuthSteps
from romanov.steps.settings import Steps

from romanov.app.driver import connect

GOOD_UPDATE = "Данные успешно обновлены"
GOOD_UPDATE_AVATAR = "Аватар успешно обновлен"
GOOD_UPDATE_PASS = "Пароль успешно обновлен"
EMPTY = ""
ERR_IMG = "Ошибка отправки запроса"
ERR_PASS = "Пароль должен быть из шести и более символов"
EXIST_EMAIL = "Ошибка обработки запроса"
ERR_EMAIL = "Введите корректный email"
ERR_LOG = "Логин должен состоять из трех и более символов,\nи содержать только латинские буквы, цифры и подчеркивание"
EXIST_LOG = "Ошибка обработки запроса"


class SettingsTest(unittest.TestCase):
    def test_settings_upload_image(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_avatar('/testData/octopus.png')
        label = settings.find_success_modal()
        self.assertEqual(label, GOOD_UPDATE_AVATAR)

    def test_settings_upload_large_image(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_avatar('/testData/largeImage.jpg')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_IMG)

    def test_settings_change_pass(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_pass()
        label = settings.find_success_modal()
        self.assertEqual(label, GOOD_UPDATE_PASS)

    def test_settings_change_short_pass(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_pass('123')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_PASS)

    def test_settings_change_empty_pass(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_pass('')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_PASS)

    def test_settings_change_email(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_email('test123@test123.ru')
        label = settings.find_success_modal()
        self.assertEqual(label, GOOD_UPDATE)

    def test_settings_change_empty_email(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_email('')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_EMAIL)

    def test_settings_change_incorrect_email(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_email('test12@@@r.rt')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_EMAIL)

    def test_settings_change_exist_email(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_email('test@test.ru')
        label = settings.find_info_error()
        self.assertEqual(label, EXIST_EMAIL)

    def test_settings_change_login(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_login()
        label = settings.find_success_modal()
        self.assertEqual(label, GOOD_UPDATE)

    def test_settings_change_short_login(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_login('12')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_LOG)

    def test_settings_change_empty_login(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_login('')
        label = settings.find_info_error()
        self.assertEqual(label, ERR_LOG)

    def test_settings_change_exist_login(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_login('slava')
        label = settings.find_info_error()
        self.assertEqual(label, EXIST_LOG)

    def test_settings_change_desc(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        settings.change_desc('About me')
        label = settings.find_success_modal()
        self.assertEqual(label, GOOD_UPDATE)

    def test_settings_refresh_after_change(self):
        settings = Steps()
        AuthSteps.login_app(self)
        settings.open_settings()
        new_email = 'tes2t@tes2t.ru'
        new_desc = 'test'
        settings.change_data(email=new_email, desc=new_desc)
        settings.open_settings()
        email, desc, name = settings.get_data()
        self.assertEqual(email, new_email)
        self.assertEqual(desc, new_desc)
        self.assertEqual(name, connect.username)
