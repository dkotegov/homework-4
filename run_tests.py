# -*- coding: utf-8 -*-

import logging
import sys
import unittest
from test_suites.search_test import SearchTests
from test_suites.notification_test import NotificationTests
from test_suites.category_test import CategoryTests
from test_suites.leaders_test import LeaderTests

log = logging.getLogger(__name__)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(SearchTests))
    suite.addTest(unittest.makeSuite(NotificationTests))
    suite.addTest(unittest.makeSuite(CategoryTests))
    suite.addTest(unittest.makeSuite(LeaderTests))

    print(suite)

    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        log.error('not successfulRes')
        sys.exit(not successfulRes)
