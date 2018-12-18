# -*- coding: utf-8 -*-
import unittest
import os

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage
from selenium.webdriver import DesiredCapabilities, Remote


class TestSearchLetters(unittest.TestCase):
    USEREMAIL = 'park_tech@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    def setUp(self):
        browser = os.environ.get('BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        auth_page = AuthPage(self.driver)
        auth_page.open()
        auth_form = auth_page.form
        auth_form.set_login(self.USEREMAIL)
        auth_form.set_password(self.PASSWORD)
        auth_form.submit()

        self.main_page = MainPage(self.driver)
        self.main_page.waitForVisible()

    def tearDown(self):
        self.driver.quit()

    """
        № Теста:                1
        Ключ поиска:            40bd001563085fc35165329ea1ff5c5ecbdbbeef
        Фильтры поиска:         нет
        Целевая папка:          все
        Ожидаемый результат:    2
    """

    def test_find_by_date_simple(self):
        search_key = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'
        letters_in_target_expected = 2

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.make_search(search_key)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                2
        Ключ поиска:            40bd001563085fc35165329ea1ff5c5ecbdbbeef
        Фильтры поиска:         -
        Целевая папка:          Непрочитанные
        Ожидаемый результат:    1 письмо
    """

    def test_find_unread_by_key(self):
        letters_in_target_expected = 1
        search_key = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.make_search(search_key)
        searchbar.search_with_icon(searchbar.ICON_UNREAD)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                3
        Ключ поиска:            40bd001563085fc35165329ea1ff5c5ecbdbbeef
        Фильтры поиска:         С флажком
        Целевая папка:          -
        Ожидаемый результат:    1 письмо
    """

    def test_find_flagged_by_key(self):
        letters_in_target_expected = 1
        search_key = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.make_search(search_key)
        searchbar.search_with_icon(searchbar.ICON_FLAGGED)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                4
        Ключ поиска:            123
        Фильтры поиска:         C вложениями
        Целевая папка:          все
        Ожидаемый результат:    2 письма
    """

    def test_find_attached(self):
        letters_in_target_expected = 2
        search_key = '123'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.make_search(search_key)
        searchbar.search_with_icon(searchbar.ICON_ATTACH)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                5
        Ключ поиска:            mvideo
        Фильтры поиска:         Заказы
        Целевая папка:          все
        Ожидаемый результат:    2 письма
    """

    def test_find_orders(self):
        letters_in_target_expected = 2
        search_key = 'mvideo'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.search_with_icon_first_time()
        searchbar.search_with_icon(searchbar.ICON_ORDERS)
        searchbar.make_active_search(search_key)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                6
        Ключ поиска:            fin
        Фильтры поиска:         финансы
        Целевая папка:          все
        Ожидаемый результат:    0 писем
    """

    def test_find_finance(self):
        letters_in_target_expected = 0
        search_key = 'fin'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.search_with_icon_first_time()
        searchbar.search_with_icon(searchbar.ICON_FINANCE)
        searchbar.make_active_search(search_key)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                7
        Ключ поиска:            kllk
        Фильтры поиска:         регистрации
        Целевая папка:          все
        Ожидаемый результат:    1 письмо
    """

    def test_find_regs(self):
        letters_in_target_expected = 1
        search_key = 'kllk'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.search_with_icon_first_time()
        searchbar.search_with_icon(searchbar.ICON_REGISTRATION)
        searchbar.make_active_search(search_key)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                8
        Ключ поиска:            travel
        Фильтры поиска:         Путешествия
        Целевая папка:          все
        Ожидаемый результат:    0 писем
    """

    def test_find_travels(self):
        letters_in_target_expected = 0
        search_key = 'travel'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.search_with_icon_first_time()
        searchbar.search_with_icon(searchbar.ICON_TRAVEL)
        searchbar.make_active_search(search_key)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                9
        Ключ поиска:            fis
        Фильтры поиска:         Штрафы
        Целевая папка:          все
        Ожидаемый результат:    0 писем
    """

    def test_find_fees(self):
        letters_in_target_expected = 0
        search_key = 'fis'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.search_with_icon_first_time()
        searchbar.search_with_icon(searchbar.ICON_FEES)
        searchbar.make_active_search(search_key)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                10
        Ключ поиска 1:          fwd
        Ключ поиска 2:          verify
        Фильтры поиска:         -
        Целевая папка:          все
        Ожидаемый результат:    1 письмо
    """

    def test_find_by_two_keys(self):
        letters_in_target_expected = 1
        search_key_1 = 'fwd'
        search_key_2 = 'verify'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.make_search(search_key_1)
        searchbar.make_active_search(search_key_2)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                11
        Ключ поиска:            tech
        Фильтры поиска:         Непрочитанные, с вложениями
        Целевая папка:          все
        Ожидаемый результат:    3 письма
    """

    def test_find_by_two_icons(self):
        letters_in_target_expected = 3
        search_key = 'tech'

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.make_search(search_key)
        searchbar.search_with_icon(searchbar.ICON_UNREAD)
        searchbar.search_with_icon(searchbar.ICON_ATTACH)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                12
        Ключ поиска:            -
        Фильтры поиска:         Непрочитанные, с вложениями, с флажком
        Целевая папка:          все
        Ожидаемый результат:    2 письма
    """

    def test_find_by_three_icons(self):
        letters_in_target_expected = 2

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()

        searchbar.search_with_icon_first_time()
        searchbar.search_with_icon(searchbar.ICON_UNREAD)
        searchbar.search_with_icon(searchbar.ICON_FLAGGED)
        searchbar.search_with_icon(searchbar.ICON_ATTACH)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))
