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

		UserPage(self.driver).login()

	def tearDown(self):
		self.driver.quit()

	def add_comment_test(self):
		pass
