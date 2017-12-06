#!/usr/bin/env python2

import sys
import unittest

from tests.messages import MessagesTest
from tests.discussions import DiscussionsTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MessagesTest),
        unittest.makeSuite(DiscussionsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
