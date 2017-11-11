# -*- coding: utf-8 -*-

import os

import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages import AuthPage


class AddCommentTest(unittest.TestCase):
	USERNAME = u'Илья Раков'
	USER_EMAIL = 'technopark34'
	PASSWORD = os.environ['OK_PASSWORD']

	def login(self):
		auth_page = AuthPage(self.driver)
		auth_page.open()

		auth_form = auth_page.form
		auth_form.set_login(self.USER_EMAIL)
		auth_form.set_password(self.PASSWORD)
		auth_form.submit()

	def setUp(self):
		browser = os.environ.get('BROWSER', 'CHROME')

		self.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

	def tearDown(self):
		self.driver.quit()

	def test(self):


		user_name = auth_page.top_menu.get_username()
		self.assertEqual(self.USERNAME, user_name)
