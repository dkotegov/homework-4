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
        При пустой строке поиска на вкладке "Люди" отображается список "Возможно знакомых людей"
        """
        # self.sp.search_field.clear()
        self.assertEqual(self.sp.search_field.status(), u'Возможно, вы знакомы')

    def test_people_categories(self):
        """
        Список параметров поиска на вкладке "Люди" соответствует перечню: Пол, 
        Возраст, Место, Школа.
        """
        self.assertTrue(self.sp.categories.CheckExists(u'Пол'))
        self.assertTrue(self.sp.categories.CheckExists(u'Возраст'))
        self.assertTrue(self.sp.categories.CheckExists(u'Место'))
        self.assertTrue(self.sp.categories.CheckExists(u'Школа'))
        
    def test_empty_query_group_search(self):
        """
        При пустой строке поиска на вкладке "Группы" отображается список "Популярное"
        """
        self.sp.nav.goto_groups()
        self.assertEqual(self.sp.search_field.status(), u'Популярное')

    def test_group_categories(self):
        """
        Список параметров поиска на вкладке "Группы" соответствует перечню: Тип, Место.
        """
        self.sp.nav.goto_groups()        
        self.assertTrue(self.sp.categories.CheckExists(u'Тип'))
        self.assertTrue(self.sp.categories.CheckExists(u'Место'))
        
    def test_games_empty_request(self):
        """
        При пустой строке поиска на вкладке "Игры" отображается пустой результат, 
        список параметров поиска на вкладке "Игры" соответствует перечню: Тип
        """
        self.sp.nav.goto_games()        
        self.assertTrue(self.sp.search_result.is_empty())
        self.assertTrue(self.sp.categories.CheckExists(u'Тип'))

    def test_music_empty_request(self):
        """
        При пустой строке поиска на вкладке "Музыка" отображается пустой результат, 
        список параметров поиска на вкладке "Музыка" соответствует перечню: Категория.
        """
        self.sp.nav.goto_music()        
        self.assertTrue(self.sp.search_result.is_empty())
        self.assertTrue(self.sp.categories.CheckExists(u'Категория'))

    def test_movies_empty_request(self):
        """
        При пустой строке поиска на вкладке "Видео" отображается пустой результат, 
        список параметров поиска на вкладке "Видео" соответствует перечню: 
        Тип, Длительность, Дата загрузки
        """
        self.sp.nav.goto_movies()        
        self.assertTrue(self.sp.search_result.is_empty())
        self.assertTrue(self.sp.categories.CheckExists(u'Тип'))
        self.assertTrue(self.sp.categories.CheckExists(u'Длительность'))
        self.assertTrue(self.sp.categories.CheckExists(u'Дата загрузки'))

    def test_special_group_query(self):
        """
        Поиск по группам с запросом "ebay" выдает несколько результатов, 
        один из которых "eBay Россия"
        """
        self.sp.nav.goto_groups()
        self.sp.search_field.enter('ebay')
        self.assertTrue(self.sp.search_result.contains(u'eBay Россия'))
        
    def test_special_game_query(self):
        """
        Поиск по играм с запросом "uniwordcity" выдает 1 результат "Uniwordcity"
        """
        self.sp.nav.goto_games()
        self.sp.search_field.enter('Uniwordcity')
        self.assertTrue(self.sp.search_result.contains(u'Uniwordsity'))
        
    def test_special_music_query(self):
        """
        Поиск по музыке с запросом "Queen" по категории "Исполнитель" выдает группу "Queen"
        """
        self.sp.nav.goto_music()
        self.sp.categories.Set(u'Исполнители')        
        self.sp.search_field.enter('queen')
        self.assertEqual(self.sp.search_result.music_best_search(), u'Queen')
        
    def test_empty_results_on_stupid_query(self):
        """
        При поиске заведомо несуществующего запроса 
        (например, "жфмтишй3х3ерпшоьсщфиыПР№ОТЗМЛУТЛЭИфыщшоп" )
        цвет шрифта названия всех вкладок, кроме текущей, становится серым, 
        что символизирует об отсутствии результатов во вкладке
        (к элементам меню применется класс '__empty')
        """       
        self.sp.search_field.enter(u'жфмтишй3х3ерпшоьсщфиыПР№ОТЗМЛУТЛЭИфыщшоп')
        self.assertTrue(self.sp.nav.is_all_empty())
        
        