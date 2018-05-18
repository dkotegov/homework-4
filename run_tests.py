# -*- coding: utf-8 -*-

import unittest
import sys
from base_info_tests_pytonchik import Tests
from tests_privacy import TestsPrivacy
from test_base_settings import TestsBaseSettings

if __name__ == '__main__':
    suite = unittest.TestSuite((unittest.makeSuite(TestsBaseSettings)),)
    result = unittest.TextTestRunner().run(suite)
