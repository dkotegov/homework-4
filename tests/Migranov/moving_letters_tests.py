# -*- coding: utf-8 -*-

import unittest
import os
from selenium import webdriver

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.common.exceptions import TimeoutException


class TestMovingLettersInFolders(unittest.TestCase):
    USEREMAIL = 'ttexnopark@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    USER_DIR_NAME = 'Test_Rustam'
    SPAM = 'Спам'
    ARCHIVE = 'Архив'
    INBOX = 'Входящие'
    SENT = 'Отправленные'

    WHOM = USEREMAIL
    SUBJECT = "Testing Move Letters"
    MESSAGE_TEXT = "Some letter"

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)   # Авторизация
        auth_page.form.authorize(self.USEREMAIL, self.PASSWORD)

        self.main_page = MainPage(self.driver)
        self.sidebar = self.main_page.sidebar
        self.letters = self.main_page.letters
        self.folder_create = self.main_page.folder_create
        self.write_letter = self.main_page.write_letter
        self.topbar = self.main_page.topbar

    def tearDown(self):
        self.sidebar.go_to_folder(self.SENT)
        self.letters.remove_letters_by_subject(self.sidebar, self.SUBJECT)
        self.sidebar.clear_trash()
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
        letters_number = 2

        # отправленные нами во время теста письма
        # иногда могут не приходить на наш ящик (нужно обновить страницу)
        # (видимо баг в почте)
        for i in range(letters_number):
            self.sidebar.write_and_send_letter(
                self.WHOM, self.SUBJECT, self.MESSAGE_TEXT)

        self.letters.drag_and_drop_letters(
            self.sidebar, self.SUBJECT, letters_number, self.USER_DIR_NAME)

        self.sidebar.go_to_folder(self.USER_DIR_NAME)

        our_letters_in_target_expected = letters_number
        our_letters_in_target_actual = len(
            self.letters.get_letters_by_subject(self.SUBJECT))
        self.assertEqual(
            our_letters_in_target_expected,
            our_letters_in_target_actual,
            'Letters in \"{}\": expected: {}, actual: {}'.format(
                self.USER_DIR_NAME,
                our_letters_in_target_expected,
                our_letters_in_target_actual)
        )

        self.letters.remove_letters_by_subject(self.sidebar, self.SUBJECT)

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
        self.sidebar.write_and_send_letter(
            self.WHOM, self.SUBJECT, self.MESSAGE_TEXT)

        self.letters.move_letter_by_subject_to_folder(
            self.SUBJECT, self.USER_DIR_NAME)
        self.sidebar.go_to_folder(self.USER_DIR_NAME)
        self.letters.move_letter_by_subject_to_folder(self.SUBJECT, self.SPAM)
        self.sidebar.go_to_folder(self.SPAM)

        our_letters_in_target_expected = 1
        our_letters_in_target_actual = len(
            self.letters.get_letters_by_subject(self.SUBJECT))

        self.assertEqual(
            our_letters_in_target_expected,
            our_letters_in_target_actual,
            'Letters in \"{}\": expected: {}, actual: {}'.format(
                self.SPAM,
                our_letters_in_target_expected,
                our_letters_in_target_actual)
        )

        self.letters.remove_letters_by_subject(self.sidebar, self.SUBJECT)

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
        self.sidebar.write_and_send_letter(
            self.WHOM, self.SUBJECT, self.MESSAGE_TEXT)

        self.letters.open_letter_by_subject(self.SUBJECT)
        self.topbar.move_to_archive()
        self.sidebar.go_to_folder(self.ARCHIVE)

        our_letters_in_target_expected = 1
        our_letters_in_target_actual = len(
            self.letters.get_letters_by_subject(self.SUBJECT))

        self.assertEqual(
            our_letters_in_target_expected,
            our_letters_in_target_actual,
            'Letters in \"{}\": expected: {}, actual: {}'.format(
                self.ARCHIVE,
                our_letters_in_target_expected,
                our_letters_in_target_actual)
        )

        self.letters.remove_letters_by_subject(self.sidebar, self.SUBJECT)

    """
        № Теста:            4
        КЭ:                 Недопустимый
        Количество писем:   Одно письмо
        Откуда:             Из списка
        Способ перемещения: Drag&drop
        Начальная папка:    Основная папка
        Целевая папка:      Основная папка
    """

    def test_moving_letters_to_the_same_folder(self):
        letters_number = 1

        self.sidebar.write_and_send_letter(
            self.WHOM, self.SUBJECT, self.MESSAGE_TEXT)

        our_letters_in_target_expected = len(
            self.letters.get_letters_by_subject(self.SUBJECT))
        self.letters.drag_and_drop_letters(
            self.sidebar, self.SUBJECT, letters_number, self.INBOX)
        self.sidebar.go_to_folder(self.INBOX)
        our_letters_in_target_actual = len(
            self.letters.get_letters_by_subject(self.SUBJECT))

        self.assertEqual(
            our_letters_in_target_expected,
            our_letters_in_target_actual,
            'Letters in \"{}\": expected: {}, actual: {}'.format(
                self.INBOX,
                our_letters_in_target_expected,
                our_letters_in_target_actual)
        )

        self.topbar.delete()
