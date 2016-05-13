#!/usr/bin/env python2

import sys
import unittest

from CreateResumePageTest import CreateResumePageTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreateResumePageTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
