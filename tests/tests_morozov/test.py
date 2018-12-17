# -*- coding: utf-8 -*-
import unittest
import os

from tests.pages.auth_page import AuthPage
from tests.pages.main_page import MainPage

from selenium.webdriver import DesiredCapabilities, Remote

class TestSearchingLetters(unittest.TestCase):
    USEREMAIL = 'park_tech@mail.ru'
    PASSWORD = os.environ['PASSWORD']

    # Кликнуть по поиску, кликнуть по дате, кликнуть по 10 числу
    # Кликнуть по поиску, кликнуть по дате, кликнуть по +-3 дня, кликнуть по фильтру, выбрать 10 число
    # кликнуть по дате, выбрать 2019, выбрать 10 число
    # кликнуть по дате, выбрать 2017, выбрать 10 число
    # кликнуть по дате, кликнуть по фильтру, кликнуть по +-1день, кликнуть по +-1 день, проверить фильтр
    # кликнуть по дате, кликнуть по фильтру, кликнуть по строке поиска, клинуть по "папки"
    # кликнуть по дате, кликнуть по фильтру, кликнуть по строке поиска, клинуть по "вложения"
    # кликнуть по дате, кликнуть по фильтру, кликнуть по строке поиска, клинуть по "закладки"
    # кликнуть по дате, кликнуть по фильтру, кликнуть по строке поиска, клинуть по "папки", кликнуть по "входящие".
    # зафиксировать результат, закрыть оба фильтра и кликнуть в обратном порядке, сравнть результат
    def setUp(self):
        print(os.environ['PASSWORD'])
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
        КЭ:                     Допустимый
        Ключ поиска:            Дата
        Фильтры поиска:         Date(2018.12.09)
        Целевая папка:          все
        Ожидаемый результат:    8 писем
    """

    # def test_find_by_date_simple(self):
    #     search_key = '40bd001563085fc35165329ea1ff5c5ecbdbbeef'
    #     letters_in_target_expected = 8
    #
    #     searchbar = self.main_page.searchbar
    #     searchbar.waitForVisible()
    #     searchbar.search_by_date('2018_12_09')
    #     #searchbar.make_search(search_key)
    #
    #     letters_in_target_actual = searchbar.has_letters()
    #
    #     self.assertEqual(
    #         letters_in_target_expected,
    #         letters_in_target_actual,
    #         'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                2
        КЭ:                     Допустимый
        Ключ поиска:            Дата +-7 дней
        Фильтры поиска:         Date(2018.12.07)
        Целевая папка:          все
        Ожидаемый результат:    16 писем
    """

    def test_find_by_date_with_interval(self):
        letters_in_target_expected = 16

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date_pm('2018_12_07', '7')

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                3
        КЭ:                     Отрицательный
        Ключ поиска:            нет
        Фильтры поиска:         Date(2018.12.31)
        Целевая папка:          все
        Ожидаемый результат:    0 писем
    """

    def test_find_by_date_from_future(self):
        letters_in_target_expected = 0

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date('2018_12_31')

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                4
        КЭ:                     Допустимый
        Ключ поиска:            нет
        Фильтры поиска:         Date(2018.12.15)
        Целевая папка:          отправленные
        Ожидаемый результат:    6 писем
    """

    def test_find_by_date_and_folder(self):
        letters_in_target_expected = 6

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date('2018_12_15')
        searchbar.search_in_folder('Отправленные')

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                5
        КЭ:                     Допустимый
        Ключ поиска:            нет
        Фильтры поиска:         Date(2018.12.14), с вложениями
        Целевая папка:          нет
        Ожидаемый результат:    2 писем
    """

    def test_find_by_date_and_with_attach(self):
        letters_in_target_expected = 2

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date('2018_12_14')
        searchbar.search_with_icon(searchbar.ICON_ATTACH)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
        № Теста:                6
        КЭ:                     Допустимый
        Ключ поиска:            нет
        Фильтры поиска:         Date(2018.12.14), закладки
        Целевая папка:          нет
        Ожидаемый результат:    1 писем
    """

    def test_find_by_date_and_with_attach(self):
        letters_in_target_expected = 1

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date('2018_12_14')
        searchbar.search_with_icon(searchbar.ICON_FLAGGED)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

    """
            № Теста:                7
            КЭ:                     Допустимый
            Ключ поиска:            нет
            Фильтры поиска:         Date(2018.12.17), непрочитанные / непрочитанные, Date(2018.12.17)
            Целевая папка:          нет
            Ожидаемый результат:    6 писем
        """

    def test_transitive_of_filters(self):

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date('2018_12_17')
        searchbar.search_with_icon(searchbar.ICON_UNREAD)
        letters_in_target_actual_1 = searchbar.has_letters()
        self.driver.get(self.driver.current_url)
        searchbar.waitForVisibleAfterReload()
        searchbar.change_pm('1')
        letters_in_target_actual_2 = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_actual_1,
            letters_in_target_actual_2,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_actual_1, letters_in_target_actual_2))

    """
        № Теста:                8
        КЭ:                     Допустимый
        Ключ поиска:            нет
        Фильтры поиска:         Date(2018.12.17), закладки, непрочитанные, с вложениями
        Целевая папка:          нет
        Ожидаемый результат:    1 писем
    """

    def test_find_by_many_filters(self):
        letters_in_target_expected = 1

        searchbar = self.main_page.searchbar
        searchbar.waitForVisible()
        searchbar.search_by_date('2018_12_17')
        searchbar.search_with_icon(searchbar.ICON_UNREAD)
        searchbar.search_with_icon(searchbar.ICON_FLAGGED)
        searchbar.search_with_icon(searchbar.ICON_ATTACH)

        letters_in_target_actual = searchbar.has_letters()

        self.assertEqual(
            letters_in_target_expected,
            letters_in_target_actual,
            'Letters: expected: {}, actual: {}'.format(letters_in_target_expected, letters_in_target_actual))

