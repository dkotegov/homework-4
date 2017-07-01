# -*- coding: utf-8 -*-
import os
import random
import unittest
from PageObjects import *

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.ui import WebDriverWait

class MyTest(unittest.TestCase):
   USEREMAIL = os.environ['LOGIN']
   PASSWORD = os.environ['PASSWORD']
   USERNAME = u'Питаков Дмитрий'

   def setUp(self):
      browser = os.environ.get('BROWSER', 'FIREFOX')

      self.driver = Remote(
         command_executor = 'http://127.0.0.1:4444/wd/hub',
         desired_capabilities = DesiredCapabilities.CHROME
      )

      auth_page = AuthPage(self.driver)
      auth_page.open()

      auth_form = auth_page.form
      auth_form.open_form()
      auth_form.set_login(self.USEREMAIL)
      auth_form.set_password(self.PASSWORD)
      auth_form.submit()
      self.user_name = auth_page.top_menu.get_username()
    
      self.bugReportPage = BugReportPage(self.driver)
      self.bugReportPage.open()

   def tearDown(self):
      self.driver.quit()

   def test_obratnaya_svaz_button_rabotaiet(self):
      self.assertFalse(self.bugReportPage.obratnaya_svaz_form.is_displayed())
      self.bugReportPage.obratnaya_svaz_button.click()
      self.assertTrue(self.bugReportPage.obratnaya_svaz_form.is_displayed())

   def test_comment_number_on_page_with_articles(self):
      articles = self.bugReportPage.articles
      self.assertNotEqual(articles.get_articles_count(), 0)
      article_id = articles.get_article(1).get_id()
      articles_comments_count = articles.get_article(1).get_comments_count()
      commentsPage = CommentsPage(self.driver, article_id)
      commentsPage.open()
      self.assertEqual(commentsPage.comments.count_comments(), articles_comments_count)

   def test_comment_number_on_article_page(self): 
      articles = self.bugReportPage.articles
      count = articles.get_articles_count()
      article_number = random.randint(1, count)
      article_id = articles.get_article(article_number).get_id()
      commentsPage = CommentsPage(self.driver, article_id)
      commentsPage.open()
      self.assertEqual(commentsPage.number_comments_presented_for_user, commentsPage.comments.count_comments())

   def test_status_select(self):
      status = u'Новая'
      self.bugReportPage.statusSelect.set_status(status)
      articles = self.bugReportPage.articles
      count = articles.get_articles_count()
      self.assertNotEqual(count, 0)
      article_status = articles.get_article(1).get_article_info_status_text()
      self.assertEqual(u'Статус: ' + status, article_status)

   def test_search_by_author(self): 
      self.bugReportPage.search.set_query_text(self.USERNAME)
      self.bugReportPage.search.submit()
      articles = self.bugReportPage.articles
      count = articles.get_articles_count()
      self.assertGreater(count, 0)
      article_author = articles.get_article(random.randint(1, count)).get_article_author()
      self.assertEqual(article_author, self.USERNAME)

   def test_make_comment(self):
      text = 'test ' + str(random.randint(1, 1000000))
      articles = self.bugReportPage.articles
      self.assertNotEqual(articles.get_articles_count(), 0)
      article_id = articles.get_article(1).get_id()
      commentsPage = CommentsPage(self.driver, article_id)
      commentsPage.open()
      commentsCount = commentsPage.comments.count_comments()
      commentForm = commentsPage.comment_form
      commentForm.show_comment_form()
      commentForm.set_text(text)
      commentForm.submit()
      commentsPage = CommentsPage(self.driver, article_id)
      commentsPage.open()
      self.assertEqual(commentsCount + 1, commentsPage.comments.count_comments())
      commentsPage.comments.delete_comment()

   def test_link_to_bugreports_comments(self):
       articles = self.bugReportPage.articles
       article = articles.get_random_article()
       self.assertNotEqual(article, None) 
       article_id = article.get_id()
       article.click_on_link()
       commentsPage = CommentsPage(self.driver, article_id)
       self.assertEqual(self.driver.current_url, commentsPage.BASE_URL + commentsPage.PATH + "#comments")

   def test_toolbar_scrollup_not_shown_before_scrolling_down(self):
      self.assertFalse(self.bugReportPage.scroll_up_button.is_displayed_with_wait())
      

   def test_toolbar_scrollup_after_the_button_pushing_scroll_possition_on_pages_top(self):
      self.bugReportPage.scroll_down()
      self.assertTrue(self.bugReportPage.scroll_up_button.is_displayed_with_wait())
      self.bugReportPage.scroll_up_button.click()
      self.assertEqual(self.bugReportPage.scroll_position(), 0)
     
   
