#!/usr/bin/env python2

import unittest

from tests_orel.tests import tests_orel
from tests_butorin.photos_test import butorin_tests

if __name__ == '__main__':

    # for test_suite in tests_orel:
    #     unittest.TextTestRunner().run(test_suite)

    for test_suite in butorin_tests:
        unittest.TextTestRunner().run(test_suite)

    for test_suite in butorin_tests:
        unittest.TextTestRunner().run(test_suite)
