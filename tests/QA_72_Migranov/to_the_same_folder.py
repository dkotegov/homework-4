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

    TARGET_DIR_NAME = 'Входящие'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.main_page = MainPage(self.driver)
        self.sidebar = self.main_page.sidebar
        self.letters = self.main_page.letters

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
        self.driver.quit()

    """
        № Теста:            5
        КЭ:                 Недопустимый
        Количество писем:   Одно письмо
        Откуда:             Из списка
        Способ перемещения: Drag&drop
        Начальная папка:    Основная папка
        Целевая папка:      Основная папка
    """
    def test_moving_letters_to_the_same_folder(self):
        letters_in_target_expected = len(self.letters.get_letters())
        self.letters.drag_and_drop_message(self.sidebar, self.TARGET_DIR_NAME)
        self.sidebar.go_to_folder(self.TARGET_DIR_NAME)
        letters_in_target_actual = len(self.letters.get_letters())
        
        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(self.TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )