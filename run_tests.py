#!/usr/bin/env python2

import sys
import unittest
from tests.git import GitTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(GitTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
