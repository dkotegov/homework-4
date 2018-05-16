# -*- coding: utf-8 -*-

import unittest
import sys
from tests import Tests
from tests_privacy import TestsPrivacy

if __name__ == '__main__':
    suite = unittest.TestSuite((unittest.makeSuite(TestsPrivacy)),)
    result = unittest.TextTestRunner().run(suite)
