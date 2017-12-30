# -*- coding: utf-8 -*-

import unittest

from test_prokopchuk.group_test import GroupsTest


def vf_tests():
    return [
        unittest.TestSuite((
            unittest.makeSuite(GroupsTest),
        )),
    ]
