# -*- coding: utf-8 -*-

import unittest

from test_prokopchuk.run_test import vf_tests

if __name__ == '__main__':

    vf_suite = unittest.TestSuite(
        vf_tests()
    )

    result = unittest.TextTestRunner().run(vf_suite)
