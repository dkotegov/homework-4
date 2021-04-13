# -*- coding: utf-8 -*-
import unittest

import sys

from tests.resume.create_experience import CreateExperience
from tests.resume.edit import EditResume
from tests.resume.list_resume import ListResume
from tests.other.chat_leftside import ChatLeftSide
from tests.other.chat_rightside import ChatRightSide
from tests.vacancy.check_recommendation import CheckRecommendations
from tests.vacancy.check_search_mainpage import CheckSearch
from tests.resume.resume import Favorite
from tests.other.main_page import PopularCategory

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CheckRegistration),
        unittest.makeSuite(CheckAuth),
        unittest.makeSuite(CheckProfile),
        unittest.makeSuite(CheckSearch),
        unittest.makeSuite(CreateResume),
        unittest.makeSuite(EditResume),
        unittest.makeSuite(Navbar),
        unittest.makeSuite(CreateExperience),
        unittest.makeSuite(ListResume),
        unittest.makeSuite(Favorite),
        unittest.makeSuite(PopularCategory),
        unittest.makeSuite(CheckSearchVacancyPage),
        unittest.makeSuite(ChatRightSide),
        unittest.makeSuite(ChatLeftSide),
        unittest.makeSuite(CheckSearch),
        unittest.makeSuite(CheckRecommendations),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
