# -*- coding: utf-8 -*-

import unittest
import sys
from test_suites.questions_test import QuestionsTests
import logging

log = logging.getLogger(__name__)

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(QuestionsTests))

    print(suite)

    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        log.error('not successfulRes')
        sys.exit(not successfulRes)
