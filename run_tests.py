# -*- coding: utf-8 -*-

import sys
import unittest
from tests.common_blocks_test import *

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CommonBlocksTestCase)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
