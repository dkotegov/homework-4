# -*- coding: utf-8 -*-

import logging
import sys
import unittest

from tests import ABTests

log = logging.getLogger(__name__)

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ABTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        log.error('not successfulRes')
        sys.exit(not successfulRes)
