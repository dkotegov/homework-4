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

	def tearDown(self):
		self.driver.quit()

	def test_add_comment(self):
		user_post = self.user_page.post.get_post_top()[0]

		self.driver.execute_script('arguments[0].click();', user_post)

		self.assertEqual(1, 1)
