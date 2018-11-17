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

    SOURCE_DIR_NAME = 'Test_Rustam'
    TARGET_DIR_NAME = 'Отправленные'

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        self.main_page = MainPage(self.driver)
        self.sidebar = self.main_page.sidebar
        self.letters = self.main_page.letters
        self.folder_create = self.main_page.folder_create

        # Авторизация
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        # Переход к версии Почты для тестирования
        self.main_page.waitForVisible()
        self.main_page.redirectToQa()
        self.main_page.go_to_inbox()

    def tearDown(self):
        # Удаление папки и очистка корзины
        self.sidebar.delete_folder(self.SOURCE_DIR_NAME)
        self.sidebar.clear_trash()

        self.driver.quit()
    
    """
        № Теста:            2
        КЭ:                 Допустимый
        Количество писем:   Одно письмо
        Откуда:             Из списка писем
        Способ перемещения: ПКМ
        Начальная папка:    Пользовательская папка
        Целевая папка:      Основная папка
    """
    
    def test_moving_letters_by_right_mouse_button_click(self):
        # Удаление source папки, если она была создана до теста
        self.sidebar.delete_folder(self.SOURCE_DIR_NAME)

        # Создание source папки
        self.sidebar.create_new_dir()
        self.folder_create.set_name(self.SOURCE_DIR_NAME)
        self.folder_create.submit()

        # Очистка target папки
        self.sidebar.clear_folder(self.TARGET_DIR_NAME)

        # Перенос письма в source папку
        self.letters.move_letter_to_folder(self.SOURCE_DIR_NAME)

        # Переход в source папку
        self.sidebar.go_to_folder(self.SOURCE_DIR_NAME)

        # Перенос письма в target папку
        self.letters.move_letter_to_folder(self.TARGET_DIR_NAME)

        # Переход в target папку
        self.sidebar.go_to_folder(self.TARGET_DIR_NAME)

        letters_in_target_expected = 1
        letters_in_target_actual = len(self.letters.get_letters())
        
        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(self.TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )

        