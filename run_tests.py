# -*- coding: utf-8 -*-
from tests.Tests import CheckListTests

import sys
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CheckListTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())