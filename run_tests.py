# -*- coding: utf-8 -*-
import sys

from tests.other.check_auth import CheckAuth
from tests.other.check_registration import CheckRegistration
from tests.other.navbar import Navbar
from tests.profile.check_profile import CheckProfile
from tests.resume.create import CreateResume, CreateResumeWrong
from tests.resume.create_experience import CreateExperience
from tests.resume.edit import EditResume
from tests.resume.list_resume import ListResume
from tests.other.chat_leftside import ChatLeftSide, ChatLeftSideWithCreate
from tests.other.chat_rightside import ChatRightSide
from tests.vacancy.check_recommendation import CheckRecommendations, CheckRecommendationsCreate
from tests.vacancy.check_search_mainpage import CheckSearch
from tests.resume.resume import Favorite, Response
from tests.other.main_page import PopularCategory
from tests.vacancy.check_search_vacancypage import CheckSearchVacancyPage
from tests.other.notification import Notification
from tests.vacancy.check_vacancy import Vacancy
from tests.company.check_company import Company
import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CheckRegistration),
        unittest.makeSuite(CheckAuth),
        unittest.makeSuite(CheckProfile),
        unittest.makeSuite(Navbar),

        unittest.makeSuite(CreateResume),
        unittest.makeSuite(CreateResumeWrong),
        unittest.makeSuite(EditResume),
        unittest.makeSuite(CreateExperience),
        unittest.makeSuite(ListResume),
        unittest.makeSuite(Favorite),
        unittest.makeSuite(PopularCategory),
        unittest.makeSuite(Notification),
        unittest.makeSuite(Response),
        unittest.makeSuite(CheckSearch),

        unittest.makeSuite(CheckSearchVacancyPage),
        unittest.makeSuite(ChatRightSide),
        unittest.makeSuite(ChatLeftSide),
        unittest.makeSuite(CheckSearch),
        unittest.makeSuite(CheckRecommendations),

        unittest.makeSuite(Vacancy),
        unittest.makeSuite(Company),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
