#!/usr/bin/env python2

import sys
import unittest
from tests.topics import TopicsTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TopicsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
