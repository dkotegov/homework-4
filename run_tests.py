# -*- coding: utf-8 -*-

import sys
import unittest
from tests.favorites_page_test import FavoritesPageTestCase
from tests.awards_page_test import AwardsPageTestCase
from tests.film_page_test import FilmPageTestCase
from tests.profile_page_test import ProfilePageTestCase
from tests.ratings_page_test import RatingsPageTestCase
from tests.birth_page_test import BirthPageTestCase

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(BirthPageTestCase),
        unittest.makeSuite(ProfilePageTestCase),
        # unittest.makeSuite(AwardsPageTestCase),
        # unittest.makeSuite(FavoritesPageTestCase),
        # unittest.makeSuite(RatingsPageTestCase),
        # unittest.makeSuite(FilmPageTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
