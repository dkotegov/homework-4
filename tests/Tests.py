# -*- coding: utf-8 -*-
import os

import unittest
from PageObjects import *

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

class MyTest(unittest.TestCase):
   USEREMAIL = 'dvpitakov@gmail.com.local'
   PASSWORD = os.environ['PASSWORD']
   USERNAME = u'Дмитрий Питаков'
   TEXT_FOR_SEARCH = u'Дмитрий Питаков'

   def setUp(self):
      browser = os.environ.get('BROWSER', 'FIREFOX')

      self.driver = Remote(
         command_executor = 'http://127.0.0.1:4444/wd/hub',
         desired_capabilities = DesiredCapabilities.CHROME
      )

   def tearDown(self):
      self.driver.quit()

   def test_article(self):
      auth_page = AuthPage(self.driver)
      auth_page.open()

      auth_form = auth_page.form
      auth_form.open_form()
      auth_form.set_login(self.USEREMAIL)
      auth_form.set_password(self.PASSWORD)
      auth_form.submit()
      user_name = auth_page.top_menu.get_username()
      self.assertEqual(self.USERNAME, user_name)

      bugReportPage = BugReportPage(self.driver)
      bugReportPage.open()

      article = bugReportPage.article(1)
      print(article.get_topic_title_text())
      print(article.get_topic_info_source_text())
      print(article.get_topic_info_status_text())
      print(article.get_topic_author())


   #считывает автора новейшего поста запоминает id поста
   #вбивает в поиск фамилию и имая автора
   #ищет пост с тем же id
   def test_search(self):
      auth_page = AuthPage(self.driver)
      auth_page.open()

      auth_form = auth_page.form
      auth_form.open_form()
      auth_form.set_login(self.USEREMAIL)
      auth_form.set_password(self.PASSWORD)
      auth_form.submit()
      user_name = auth_page.top_menu.get_username()
      self.assertEqual(self.USERNAME, user_name)

      bugReportPage = BugReportPage(self.driver)
      bugReportPage.open()

      topic_title = article.get_topic_title_text()
      topic_source = article.get_topic_info_source_text()
      topic_status = article.get_topic_info_status_text()
      topic_author = article.get_topic_author()

      searchForm = bugReportPage.search
      searchForm.set_query_text(topic_author)
      seatchForm.submit()

      
      
        
