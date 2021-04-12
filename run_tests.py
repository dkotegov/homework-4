# -*- coding: utf-8 -*-
import unittest

import sys

from tests.other.chat_leftside import ChatLeftSide
from tests.other.chat_rightside import ChatRightSide
from tests.other.navbar import Navbar
from tests.profile.check_profile import CheckProfile
from tests.vacancy.check_recommendation import CheckRecommendations
from tests.vacancy.check_search_mainpage import CheckSearch
from tests.resume.create import CreateResume
from tests.vacancy.check_search_vacancypage import CheckSearchVacancyPage

if __name__ == '__main__':
    suite = unittest.TestSuite((
    #    unittest.makeSuite(CheckProfile),
        #unittest.makeSuite(CheckSearchVacancyPage),
        unittest.makeSuite(ChatRightSide),
        # unittest.makeSuite(ChatLeftSide),

        # unittest.makeSuite(CheckSearch),
       #  unittest.makeSuite(CheckRecommendations),
    #    unittest.makeSuite(CreateResume),
    #   unittest.makeSuite(Navbar)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
