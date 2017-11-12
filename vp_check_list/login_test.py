# -*- coding: utf-8 -*-

import os
import unittest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages.auth_pages import AuthPage


class LoginTest(unittest.TestCase):
	USERNAME = u'Илья Раков'
	USER_EMAIL = 'technopark34'
	PASSWORD = os.environ['OK_PASSWORD']

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

		auth_form = auth_page.form

		user_name = auth_form.login()
		self.assertEqual(self.USERNAME, user_name)
