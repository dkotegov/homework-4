#!/usr/bin/env python3

import sys
import unittest
from cases.auth_case import AuthTest
from cases.profile_case import ProfileTest

if __name__ == '__main__':
    suite = unittest.TestSuite(
        (
            # unittest.makeSuite(AuthTest),
            unittest.makeSuite(ProfileTest),
        )
    )

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
