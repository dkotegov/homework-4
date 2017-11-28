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

    # def test_empty_query_people_search(self):
    #     """
    #     People search with empty query
    #     """
    #     self.assertEqual(self.sp.search_field.status(), u'Возможно, вы знакомы')

    def test_people_categories(self):
        """
        Check category list on people search page
        """
        self.assertTrue(self.sp.categories.CheckExists(u'Пол'))
        self.assertTrue(self.sp.categories.CheckExists(u'Возраст'))
        self.assertTrue(self.sp.categories.CheckExists(u'Место'))
        self.assertTrue(self.sp.categories.CheckExists(u'Школа'))
        
        
