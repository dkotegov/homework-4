# -*- coding: utf-8 -*-

import sys
import unittest

from vp_check_list.comments_test import CommentsTest

from vp_check_list.login_test import LoginTest

if __name__ == '__main__':
	login_suite = unittest.TestSuite((
		# unittest.makeSuite(LoginTest),
	))

	comments_suite = unittest.TestSuite((
		unittest.makeSuite(CommentsTest),
	))

	login_result = unittest.TextTestRunner().run(login_suite)
	comments_result = unittest.TextTestRunner().run(comments_suite)

	sys.exit(not (login_result.wasSuccessful() and comments_result.wasSuccessful()))
