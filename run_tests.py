# -*- coding: utf-8 -*-

import unittest
import sys
from test_mikegus import Tests
from tests_privacy import TestsPrivacy
from test_johnkeats97 import TestsBaseSettings

if __name__ == '__main__':
    suite = unittest.TestSuite((unittest.makeSuite(TestsBaseSettings)),)
    result = unittest.TextTestRunner().run(suite)
