#!/usr/bin/env python3

import sys
import unittest
from cases.base_case import BaseTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(BaseTest),
        )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
