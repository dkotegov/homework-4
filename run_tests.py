#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
from tests.movies.click_on_movie_test import ClickOnMovieTest
from tests.movies.click_on_genre_test import ClickOnGenreTest as ClickOnMovieGenreTest
from tests.series.click_on_genre_test import ClickOnGenreTest
from tests.series.click_on_series_test import ClickOnSeriesTest
from tests.login.login_test import LoginTest
from tests.navbar.logout_test import LogoutTest
from tests.navbar.go_to_profile_test import GoToProfileTest
from tests.navbar.go_to_favourites_test import GoToFavouritesTest
from tests.details.tests_without_auth.transit_to_auth_page_test import TransitToAuthTest
from tests.details.tests_without_auth.click_on_actor_name_test import ClickOnActorNameTest
from tests.details.tests_with_auth.transit_to_profile_page_test import TransitToProfileTest
from tests.details.tests_with_auth.details_buttons_tests import OpenPlayerTest, AddToFavouritesTest,\
    RemoveFromFavouritesTest, LikeMovieTest, DisikeMovieTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(ClickOnSeriesTest),
        # unittest.makeSuite(ClickOnGenreTest),
        # unittest.makeSuite(ClickOnMovieTest),
        # unittest.makeSuite(ClickOnMovieGenreTest),
        # unittest.makeSuite(LoginTest),
        # unittest.makeSuite(LogoutTest),
        # unittest.makeSuite(GoToProfileTest)
        # unittest.makeSuite(GoToFavouritesTest)
        # unittest.makeSuite(TransitToAuthTest)
        # unittest.makeSuite(ClickOnActorNameTest)
        # unittest.makeSuite(TransitToProfileTest)
        # unittest.makeSuite(OpenPlayerTest),
        # unittest.makeSuite(AddToFavouritesTest),
        # unittest.makeSuite(RemoveFromFavouritesTest),
        # unittest.makeSuite(LikeMovieTest),
        unittest.makeSuite(DisikeMovieTest),
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
