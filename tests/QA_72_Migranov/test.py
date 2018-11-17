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

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        # Авторизация
        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        self.main_page = MainPage(self.driver)
        self.main_page.waitForVisible()
        self.main_page.redirectToQa()
        self.main_page.go_to_inbox()

    def tearDown(self):
        self.driver.quit()

    """
        № Теста:            1
        КЭ:                 Допустимый
        Количество писем:   Два письма
        Откуда:             Из списка писем
        Способ перемещения: Drag&drop
        Начальная папка:    Основная папка
        Целевая папка:      Пользовательская папка
    """
    
    def test_moving_several_letters(self):
        TARGET_DIR_NAME = 'Test'
        messages_number = 2

        sidebar = self.main_page.sidebar

        sidebar.delete_folder(TARGET_DIR_NAME)
        sidebar.create_new_dir()
        folder_create = self.main_page.folder_create
        folder_create.set_name(TARGET_DIR_NAME)
        folder_create.submit()

        letters = self.main_page.letters

        letters.drag_and_drop_several_messages(sidebar, messages_number, TARGET_DIR_NAME)
        
        sidebar.go_to_folder(TARGET_DIR_NAME)

        letters_in_target_expected = 2
        letters_in_target_actual = len(letters.get_letters())
        
        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )

        sidebar.delete_folder(TARGET_DIR_NAME)
        sidebar.clear_trash()

    
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
        SOURCE_DIR_NAME = 'Test_Rustam'
        TARGET_DIR_NAME = 'Отправленные'

        sidebar = self.main_page.sidebar

        # Создание source папки
        sidebar.create_new_dir()
        folder_create = self.main_page.folder_create
        folder_create.set_name(SOURCE_DIR_NAME)
        folder_create.submit()

        # Очистка target папки
        sidebar.clear_folder(TARGET_DIR_NAME)

        letters = self.main_page.letters

        # Перенос письма в source папку
        letters.move_letter_to_folder(SOURCE_DIR_NAME)

        # Переход в source папку
        sidebar.go_to_folder(SOURCE_DIR_NAME)

        # Перенос письма в target папку
        letters.move_letter_to_folder(TARGET_DIR_NAME)

        # Переход в target папку
        sidebar.go_to_folder(TARGET_DIR_NAME)

        letters_in_target_expected = 1
        letters_in_target_actual = len(letters.get_letters())
        
        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )

        sidebar.delete_folder(SOURCE_DIR_NAME)
        sidebar.clear_trash()    
    
    
    """
        № Теста:            3
        КЭ:                 Допустимый
        Количество писем:   Одно письмо
        Откуда:             Из просмотра
        Способ перемещения: "В архив"
        Начальная папка:    Основная папка
        Целевая папка:      Основная папка
    """
    
    def test_moving_letters_from_view_to_archive(self):
        LETTER_SUBJECT = 'Вход с нового устройства'
        TARGET_DIR_NAME = 'Архив'

        letters = self.main_page.letters
        topbar = self.main_page.topbar
        sidebar = self.main_page.sidebar

        sidebar.clear_folder(TARGET_DIR_NAME)
        letters.open_letter_by_subject(LETTER_SUBJECT)
        topbar.move_to_archive()
        sidebar.go_to_folder(TARGET_DIR_NAME)

        letters_in_target_expected = 1
        # try:
        #     letters_in_target_actual = len(letters.get_letters())
        # except TimeoutException as ex:
        #     print("Exception has been thrown. " + str(ex))

        letters_in_target_actual = len(letters.get_letters())
        
        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )

        sidebar.delete_folder(TARGET_DIR_NAME)
        sidebar.clear_trash()
    

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
        LETTER_SUBJECT = 'Вход с нового устройства'                                     
        TARGET_DIR_NAME = 'Test_Target_Folder'

        letters = self.main_page.letters
        topbar = self.main_page.topbar
        sidebar = self.main_page.sidebar

        sidebar.delete_folder(TARGET_DIR_NAME)

        letters.open_letter_by_subject(LETTER_SUBJECT)
        topbar.move_to_new_folder(TARGET_DIR_NAME)
        sidebar.click_to_inbox()
        letters.get_letters()

        sidebar.go_to_folder(TARGET_DIR_NAME)

        letters_in_target_expected = 1
        letters_in_target_actual = len(letters.get_letters())

        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )

        sidebar.delete_folder(TARGET_DIR_NAME)
        sidebar.clear_trash()
    


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
        TARGET_DIR_NAME = 'Входящие'

        sidebar = self.main_page.sidebar
        letters = self.main_page.letters

        letters_in_target_expected = len(letters.get_letters())
        letters.drag_and_drop_message(sidebar, TARGET_DIR_NAME)
        sidebar.go_to_folder(TARGET_DIR_NAME)
        letters_in_target_actual = len(letters.get_letters())
        
        self.assertEqual(
            letters_in_target_expected, 
            letters_in_target_actual, 
            'Letters in \"{}\": expected: {}, actual: {}'.format(TARGET_DIR_NAME, letters_in_target_expected, letters_in_target_actual)
        )

