# -*- coding: utf-8 -*-

import unittest

from vp_check_list.tests.combine_actions_comments_test import CombineActionsCommentsTest
from vp_check_list.tests.errors_tests import ErrorsCommentsTest
from vp_check_list.tests.login_test import LoginTest
from vp_check_list.tests.simple_actions_with_comments import SimpleActionsWithCommentsTest
from vp_check_list.tests.simple_add_delete_comments_test import SimpleAddDeleteCommentsTest
from vp_check_list.tests.xss_test import XssTest


def vp_tests():
	return [
		unittest.TestSuite((
			unittest.makeSuite(LoginTest),
		)),
		unittest.TestSuite((
			unittest.makeSuite(SimpleAddDeleteCommentsTest),
			unittest.makeSuite(SimpleActionsWithCommentsTest),
		)),
		unittest.TestSuite((
			unittest.makeSuite(CombineActionsCommentsTest),
		)),
		unittest.TestSuite((
			unittest.makeSuite(ErrorsCommentsTest),
			unittest.makeSuite(XssTest),
		)),
	]
