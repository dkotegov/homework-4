#!/usr/bin/env python3

import sys
import unittest
from cases.auth_case import AuthTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            unittest.makeSuite(AuthTest),
        )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
