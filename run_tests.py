# -*- coding: utf-8 -*-
import unittest

import sys

from tests.other.check_auth import CheckAuth
from tests.other.check_registration import CheckRegistration
from tests.other.navbar import Navbar
from tests.profile.check_profile import CheckProfile
from tests.resume.create import CreateResume
from tests.resume.create_experience import CreateExperience
from tests.resume.edit import EditResume
from tests.resume.list_resume import ListResume
from tests.other.chat_leftside import ChatLeftSide, ChatLeftSideWithCreate
from tests.other.chat_rightside import ChatRightSide
from tests.vacancy.check_recommendation import CheckRecommendations, CheckRecommendationsCreate
from tests.vacancy.check_search_mainpage import CheckSearch
from tests.resume.resume import Favorite
from tests.other.main_page import PopularCategory
from tests.vacancy.check_search_vacancypage import CheckSearchVacancyPage

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(CheckRegistration),
        # unittest.makeSuite(Navbar),
        # unittest.makeSuite(CheckAuth),
        # unittest.makeSuite(CheckProfile),
        # unittest.makeSuite(CreateResume),
        # unittest.makeSuite(EditResume),
        # unittest.makeSuite(ListResume),
        # unittest.makeSuite(CreateExperience),
        # unittest.makeSuite(Favorite),
        # unittest.makeSuite(PopularCategory),
        unittest.makeSuite(CheckSearchVacancyPage),
        unittest.makeSuite(ChatRightSide),
        unittest.makeSuite(ChatLeftSide),
        unittest.makeSuite(ChatLeftSideWithCreate),
        unittest.makeSuite(CheckSearch),
        unittest.makeSuite(CheckRecommendationsCreate),
        unittest.makeSuite(CheckRecommendations),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
