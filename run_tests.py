# -*- coding: utf-8 -*-

import unittest
import sys

from test.cases.MusicCase import MusicTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MusicTestCase),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
