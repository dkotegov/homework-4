# -*- coding: utf-8 -*-
import unittest

import sys

from tests.other.navbar import Navbar
from tests.profile.check_profile import CheckProfile
from tests.vacancy.check_recommendation import CheckRecommendations
from tests.vacancy.check_search_mainpage import CheckSearch
from tests.resume.create import CreateResume

if __name__ == '__main__':
    suite = unittest.TestSuite((
    #    unittest.makeSuite(CheckProfile),
        unittest.makeSuite(CheckSearch),
        unittest.makeSuite(CheckRecommendations),
    #    unittest.makeSuite(CreateResume),
    #   unittest.makeSuite(Navbar)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
