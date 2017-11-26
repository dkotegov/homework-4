#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest

from as_check_list.tests.test_suite import as_tests


if __name__ == '__main__':
    suite = unittest.TestSuite(as_tests())
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
