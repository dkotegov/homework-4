# -*- coding: utf-8 -*-
import unittest

import sys

from tests.other.check_auth import CheckAuth
from tests.other.check_registration import CheckRegistration
from tests.other.navbar import Navbar
from tests.profile.check_profile import CheckProfile
from tests.vacancy.check_search_mainpage import CheckSearch
from tests.resume.create import CreateResume
from tests.resume.create_experience import CreateExperience
from tests.resume.edit import EditResume
from tests.resume.list_resume import ListResume
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
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
