#!/usr/bin/env python2

import unittest

from tests_orel.tests import tests_orel

if __name__ == '__main__':

    for test_suite in tests_orel:
        unittest.TextTestRunner().run(test_suite)
