# -*- coding: utf-8 -*-
import unittest

import sys

from tests.profile.check_profile import CheckProfile

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CheckProfile)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
