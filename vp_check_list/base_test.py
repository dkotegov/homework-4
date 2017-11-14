# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from vp_check_list.pages.user_page import UserPage


class BaseTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		browser = \
			os.environ.get('BROWSER', 'CHROME')

		cls.driver = Remote(
			command_executor='http://127.0.0.1:4444/wd/hub',
			desired_capabilities=getattr(DesiredCapabilities, browser).copy()
		)

		cls.user_page = UserPage(cls.driver)
		cls.user_page.login()

		cls.user_avatar = cls.user_page.avatar

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
