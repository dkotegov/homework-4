# -*- coding: utf-8 -*-
from tests.AskTests import AskTests

import sys
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AskTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())

