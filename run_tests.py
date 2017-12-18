#!/usr/bin/env python2

# LOGIN=technopark17 PASSWORD=testQA1 python run_tests.py

# import sys
import unittest

from tests_rogachev.tests import tests_rogachev

if __name__ == '__main__':

    for test_suite in tests_rogachev:
        unittest.TextTestRunner().run(test_suite)
