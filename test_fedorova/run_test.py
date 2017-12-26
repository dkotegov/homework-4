# -*- coding: utf-8 -*-

import unittest

from group_test import GroupTest
from test_groupcreate import TestsWithGroupCreate

def vf_tests():
	return [
            unittest.makeSuite(GroupTest),
            unittest.makeSuite(TestsWithGroupCreate)
	]

