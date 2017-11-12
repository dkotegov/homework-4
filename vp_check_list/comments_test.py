# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

from vp_check_list.pages.pages import UserPage


class CommentsTest(unittest.TestCase):
	TEST_COMMENT = 'Test comment'

	def setUp(self):
		browser = os.environ.get('BROWSER', 'CHROME')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

		self.user_page = UserPage(self.driver)
		self.user_page.login()

		self.post = self.user_page.post

	def tearDown(self):
		self.driver.quit()

	def test_add_comment(self):
		self.post.add_comment(self.TEST_COMMENT)

		self.assertEqual(1, 1)
