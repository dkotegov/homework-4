#!/usr/bin/env python2

import sys
import unittest
from tests.test_auth import TestAuth


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TestAuth),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
