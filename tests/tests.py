# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from .pages import AuthPage, SearchPage

USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

WAIT_TIME = 10

class BaseTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )
        self.driver.implicitly_wait(WAIT_TIME)
        self.login()

    def tearDown(self):
        self.driver.quit()

    def login(self):
        auth_page = AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.set_login(USERNAME)
        auth_form.set_password(PASSWORD)
        auth_form.submit()


class SearchTests(BaseTest):
    def setUp(self):
        super(SearchTests,self).setUp()
        self.sp = SearchPage(self.driver)
        self.sp.open()

    def test_empty_query_people_search(self):
        """
        People search with empty query
        """
        # self.sp.search_field.clear()
        self.assertEqual(self.sp.search_field.status(), u'Возможно, вы знакомы')

    def test_people_categories(self):
        """
        Check category list on people search page
        """
        self.assertTrue(self.sp.categories.CheckExists(u'Пол'))
        self.assertTrue(self.sp.categories.CheckExists(u'Возраст'))
        self.assertTrue(self.sp.categories.CheckExists(u'Место'))
        self.assertTrue(self.sp.categories.CheckExists(u'Школа'))
        
    def test_empty_query_group_search(self):
        """
        Group search with empty query
        """
        self.sp.nav.goto_groups()
        self.assertEqual(self.sp.search_field.status(), u'Популярное')

    def test_group_categories(self):
        """
        Check category list on group search page
        """
        self.sp.nav.goto_groups()        
        self.assertTrue(self.sp.categories.CheckExists(u'Тип'))
        self.assertTrue(self.sp.categories.CheckExists(u'Место'))
        
    def test_games_empty_request(self):
        self.sp.nav.goto_games()        
        self.assertTrue(self.sp.search_result.is_empty())
        self.assertTrue(self.sp.categories.CheckExists(u'Тип'))

    def test_music_empty_request(self):
        self.sp.nav.goto_music()        
        self.assertTrue(self.sp.search_result.is_empty())
        self.assertTrue(self.sp.categories.CheckExists(u'Категория'))

    def test_movies_empty_request(self):
        self.sp.nav.goto_movies()        
        self.assertTrue(self.sp.search_result.is_empty())
        self.assertTrue(self.sp.categories.CheckExists(u'Тип'))
        self.assertTrue(self.sp.categories.CheckExists(u'Длительность'))
        self.assertTrue(self.sp.categories.CheckExists(u'Дата загрузки'))

    def test_special_group_query(self):
        self.sp.nav.goto_groups()
        self.sp.search_field.enter('ebay')
        self.assertTrue(self.sp.search_result.contains(u'eBay Россия'))
        
    def test_special_game_query(self):
        self.sp.nav.goto_games()
        self.sp.search_field.enter('Uniwordcity')
        self.assertTrue(self.sp.search_result.contains(u'Uniwordsity'))
        
    def test_special_music_query(self):
        self.sp.nav.goto_music()
        self.sp.categories.Set(u'Исполнители')        
        self.sp.search_field.enter('queen')
        self.assertEqual(self.sp.search_result.music_best_search(), u'Queen')
        
    def test_empty_results_on_stupid_query(self):       
        self.sp.search_field.enter(u'жфмтишй3х3ерпшоьсщфиыПР№ОТЗМЛУТЛЭИфыщшоп')
        self.assertTrue(self.sp.nav.is_all_empty())
        
        