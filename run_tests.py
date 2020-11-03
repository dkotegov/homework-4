# -*- coding: utf-8 -*-

import logging
import sys
import unittest
from test_suites.search_test import SearchTests
from test_suites.notification_test import NotificationTests

log = logging.getLogger(__name__)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SearchTests))
    suite.addTest(unittest.makeSuite(NotificationTests))

    print(suite)

    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        log.error('not successfulRes')
        sys.exit(not successfulRes)
