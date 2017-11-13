# -*- coding: utf-8 -*-

import os
import unittest

from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support.wait import WebDriverWait

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

		cls.post = cls.user_page.post

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def add_comment_test(self):
		pass

	@unittest.skip("get not work")
	def test_add_comment(self):
		user_avatar = self.post.get_avatar()
		self.post.open_avatar(user_avatar)

		WebDriverWait(user_avatar, 10, 0.1).until(
			lambda d: d.find_element_by_xpath('//div[@class="ucard-v __xxxs __h"]')
		)

		self.post.add_comment_avatar(user_avatar, self.TEST_COMMENT)

		comment = self.post.get_comment_text()
		print comment

		self.assertEqual(comment, self.TEST_COMMENT)

	@unittest.skip("get not work")
	def test_delete_comment(self):
		self.post.open_post()

		self.post.add_comment(self.TEST_COMMENT_DELETE)
		self.post.del_comment()

		comment = self.post.get_comment_text()
		self.assertEqual(comment, self.TEST_COMMENT)
