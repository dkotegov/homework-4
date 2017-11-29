# -*- coding: utf-8 -*-

import sys
import unittest
from tests.tests import SearchTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(SearchTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
