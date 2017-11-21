#!/usr/bin/env python2

import sys
import unittest
from tests.messages import MessagesTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MessagesTest)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
