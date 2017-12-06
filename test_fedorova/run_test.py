# -*- coding: utf-8 -*-

import unittest

from group_test import GroupTest

def vf_tests():
	return [
	    unittest.TestSuite((
		unittest.makeSuite(GroupTest),
	    )),
	]

