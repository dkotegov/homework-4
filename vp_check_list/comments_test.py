# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote

from vp_check_list.pages.pages import UserPage


class CommentsTest(unittest.TestCase):
	TEST_COMMENT = 'Test comment'
	TEST_COMMENT_DELETE = 'Test delete comment'

	@classmethod
	def setUpClass(cls):
		browser = os.environ.get('BROWSER', 'CHROME')

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

	def test_add_comment(self):
		avatar = self.user_avatar.get_avatar()
		self.user_avatar.open_avatar(avatar)
		avatar_footer = self.user_avatar.get_avatar_footer()

		self.user_avatar.add_comment_to_avatar(avatar_footer, self.TEST_COMMENT)

		comment = self.user_avatar.get_last_comment_text(avatar_footer)
		self.assertEqual(comment, self.TEST_COMMENT)
