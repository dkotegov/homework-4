# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages.auth_pages import AuthPage


class AddCommentTest(unittest.TestCase):
	def login(self):
		user_email = 'technopark34'
		password = os.environ['OK_PASSWORD']

		auth_page = AuthPage(self.driver)
		auth_page.open()

		auth_form = auth_page.form
		auth_form.set_login(user_email)
		auth_form.set_password(password)
		auth_form.submit()

	def setUp(self):
		browser = os.environ.get('BROWSER', 'CHROME')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

		self.login()

	def tearDown(self):
		self.driver.quit()

	def test(self):
		pass
