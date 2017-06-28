#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test1 import Test1

if __name__ == '__main__':
    tests = [Test1]
    tests = map(unittest.makeSuite, tests)
    suite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
