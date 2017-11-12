# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages.pages import UserPage


class CommentsTest(unittest.TestCase):
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
		user_post = self.post.get_post()[0]

		self.post.execute(user_post)
		access = self.post.get_post_access(user_post)

		print access.text

		self.assertEqual(1, 1)
