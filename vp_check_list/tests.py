# -*- coding: utf-8 -*-

import unittest

from vp_check_list.combine_actions_comments_test import CombineActionsCommentsTest
from vp_check_list.simple_actions_with_comments import SimpleActionsWithCommentsTest
from vp_check_list.simple_add_delete_comments_test import SimpleAddDeleteCommentsTest

from vp_check_list.login_test import LoginTest


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
	]
