# -*- coding: utf-8 -*-
import unittest

import sys

from tests.profile.check_profile import CheckProfile
from tests.vacancy.check_search_mainpage import CheckSearch

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CheckProfile),
        unittest.makeSuite(CheckSearch)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
