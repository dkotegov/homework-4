#!/usr/bin/env python2

import sys
import unittest
from tests.mail import MailTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MailTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
