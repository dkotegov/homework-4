#!/usr/bin/env python2

import sys
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite((
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
