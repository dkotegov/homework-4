# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages.auth_pages import AuthPage


class LoginTest(unittest.TestCase):
	USERNAME = u'Илья Раков'

	def setUp(self):
		browser = os.environ.get('BROWSER', 'CHROME')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

	def tearDown(self):
		self.driver.quit()

	def test(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		user_name = auth_page.login()
		self.assertEqual(self.USERNAME, user_name)
