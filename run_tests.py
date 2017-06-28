#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from tests.test1 import Test1
from tests.test2 import Test2
from tests.test3 import Test3
from tests.test4 import Test4

if __name__ == '__main__':
    tests = [Test1, Test2, Test3, Test4]
    tests = map(unittest.makeSuite, tests)
    suite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
