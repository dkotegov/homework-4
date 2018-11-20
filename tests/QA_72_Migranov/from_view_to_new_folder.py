# -*- coding: utf-8 -*-

import unittest
import os
import time
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.common.exceptions import TimeoutException

class TestMovingLettersInFolders(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    LETTER_SUBJECT = 'Вход с нового устройства'                                     
    TARGET_DIR_NAME = 'Test_Rustam'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.main_page = MainPage(self.driver)
        self.sidebar = self.main_page.sidebar
        self.letters = self.main_page.letters
        self.topbar = self.main_page.topbar

        # Авторизация
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        self.main_page.waitForVisible()
        self.main_page.redirectToQa()
        self.main_page.go_to_inbox()

    def tearDown(self):
        self.sidebar.delete_folder(self.TARGET_DIR_NAME)
        self.sidebar.clear_trash()

        self.driver.quit()

    """
        № Теста:            4
        КЭ:                 Допустимый
        Количество писем:   Одно письмо
        Откуда:             Из просмотра
        Способ перемещения: "В папку"
        Начальная папка:    Основная папка
        Целевая папка:      Новая папка
    """
    
    def test_moving_letters_from_view_to_new_folder(self):
        self.sidebar.delete_folder(self.TARGET_DIR_NAME)
        self.letters.open_letter_by_subject(self.LETTER_SUBJECT)
        self.topbar.move_to_new_folder(self.TARGET_DIR_NAME)
        self.sidebar.go_to_folder(self.TARGET_DIR_NAME)

        letters_in_target_expected = 1
        letters_in_target_actual = len(self.letters.get_letters())

        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(self.TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )