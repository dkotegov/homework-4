# -*- coding: utf-8 -*-

import sys
import unittest

from test.cases.VideosCase import VideosCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(VideosCase),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
