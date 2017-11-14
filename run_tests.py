# -*- coding: utf-8 -*-

import unittest

from vp_check_list.comments_test import SimpleActionsWithCommentsTest

from vp_check_list.login_test import LoginTest

if __name__ == '__main__':
	suits = [
		unittest.TestSuite((
			unittest.makeSuite(LoginTest),
		)),
		unittest.TestSuite((
			unittest.makeSuite(SimpleActionsWithCommentsTest),
		))
	]

	for test_suite in suits:
		unittest.TextTestRunner().run(test_suite)
