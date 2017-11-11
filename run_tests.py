# -*- coding: utf-8 -*-

import sys
import unittest
from vp_check_list.test import ExampleTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ExampleTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
