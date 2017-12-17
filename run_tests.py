#!/usr/bin/env python2

import unittest

from tests_orel.run_tests import run_tests_orel
from tests_butorin.run_tests import run_tests_butorin

if __name__ == '__main__':

    for test_suite in run_tests_orel:
        unittest.TextTestRunner().run(test_suite)

    for test_suite in run_tests_butorin:
        unittest.TextTestRunner().run(test_suite)
