# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from vp_check_list.tests.base_test import BaseTest


class XssTest(BaseTest):
	TEST_XSS_COMMENT = '<script>alert("xss");</script>'

	def test_add_xss_comment(self):
		self.user_avatar.open_avatar()
		avatar_footer = self.user_avatar.comments

		avatar_footer.add_comment_to_avatar(self.TEST_XSS_COMMENT)
		try:
			WebDriverWait(self.driver, 10, 0.1).until(self.__alert_check__)
			self.assertTrue(True)
		except TimeoutException:
			self.assertTrue(False)

	def __alert_check__(self, driver):
		try:
			driver.switch_to_alert()
			return True
		except NoAlertPresentException:
			return False
