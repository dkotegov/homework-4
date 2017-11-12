# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages.pages import UserPage


class CommentsTest(unittest.TestCase):
	TEST_COMMENT = 'Test comment'

	@classmethod
	def setUpClass(cls):
		browser = os.environ.get('BROWSER', 'CHROME')

		cls.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

		cls.user_page = UserPage(cls.driver)
		cls.user_page.login()

		cls.post = cls.user_page.post

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def test_add_comment(self):
		self.post.add_comment(self.TEST_COMMENT)
		comment = self.post.get_comment_text()

		self.assertEqual(comment, self.TEST_COMMENT)

	def test_delete_comment(self):
		self.post.add_comment(self.TEST_COMMENT)
		self.post.del_comment()

		comment = self.post.get_comment_text()

		self.assertEqual(comment, self.TEST_COMMENT)
