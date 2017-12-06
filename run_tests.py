# -*- coding: utf-8 -*-

import sys
import unittest

from test.cases.VideosCase2 import VideosCase2

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(VideosCase2),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
