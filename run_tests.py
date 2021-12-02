#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest
from dotenv import load_dotenv
from tests.actor_test import ClickOnMovieNameTest
from tests.favourites_test import ClickOnMovieTest as ClickOnMovieTestFavourites, OnlyAddedMoviesTest
from tests.player_test import NotOpenedTest, ClosedTest

from tests.movies_test import ClickOnMovieTest, ClickOnMovieGenreTest

from tests.series_test import ClickOnGenreTest, ClickOnSeriesTest

from tests.navbar_test import LogoutTest, GoToProfileTest, GoToFavouritesTest

from tests.details_test import TransitToAuthTest, ClickOnActorNameTest, TransitToProfileTest, OpenPlayerTest, \
    AddToFavouritesTest, RemoveFromFavouritesTest, LikeMovieTest, DislikeMovieTest

from tests.profile_test import ClickOnSubscriptionBtnTest, ChangeToValidAvatarTest, ChangeToValidEmailTest, \
    ChangeToValidLoginTest, ChangeToValidLoginAndEmailTest, ChangeToInvalidLoginTest, ChangeToEmptyLoginTest, \
    ChangeToInvalidEmailTest, ChangeToEmptyEmailTest, ChangeToInvalidEmailAndLoginTest, \
    ChangeToInvalidLoginAndValidEmailTest

from tests.signup_test import TransitToLoginPageTest, SignUpWithEmptyFieldsTest, SignUpWithInvalidLoginTest, \
    SignUpWithNumericLoginTest, SignUpWithInvalidEmailTest, SignUpWithSmallPasswordTest, SignUpWithLetterLoginTest, \
    SignUpWithBigPasswordTest, SignUpWithDifferentPasswordsTest, SignUpWithAllInvalidFieldsTest, \
    SignUpAlreadySignupedTest

from tests.search_popup_test import ClosePopupTest, EnterLetterTest, FindMovieTest, FindActorTest

from tests.login_test import EmptyFieldsLoginTest, GoToSignupTest, InvalidEmailLoginTest, LoginTest

from tests.navbar_test import GoToMoviesTest, GoToSeriesTest, GoToMainTest

from tests.main_test import HorizontalScrollRightTest, HorizontalScrollLeftTest, ClickOnCardTest, \
    ClickOnWatchButtonTest

if __name__ == '__main__':
    load_dotenv()
    suite = unittest.TestSuite((
        unittest.makeSuite(ClickOnSeriesTest),
        unittest.makeSuite(ClickOnGenreTest),
        unittest.makeSuite(ClickOnMovieTest),
        unittest.makeSuite(ClickOnMovieGenreTest),

        # login
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(EmptyFieldsLoginTest),
        unittest.makeSuite(GoToSignupTest),
        unittest.makeSuite(InvalidEmailLoginTest),
        # unittest.makeSuite(WrongCredsLoginTest), # bug
        # unittest.makeSuite(WrongPasswordLoginTest), # bug

        # navbar
        unittest.makeSuite(GoToMoviesTest),
        unittest.makeSuite(GoToSeriesTest),
        unittest.makeSuite(GoToProfileTest),
        unittest.makeSuite(GoToFavouritesTest),
        unittest.makeSuite(GoToMainTest),
        unittest.makeSuite(LogoutTest),

        # main
        unittest.makeSuite(HorizontalScrollRightTest),
        unittest.makeSuite(HorizontalScrollLeftTest),
        unittest.makeSuite(ClickOnCardTest),
        unittest.makeSuite(ClickOnWatchButtonTest),

        # details
        unittest.makeSuite(TransitToAuthTest),
        unittest.makeSuite(ClickOnActorNameTest),
        unittest.makeSuite(TransitToProfileTest),
        unittest.makeSuite(OpenPlayerTest),
        unittest.makeSuite(AddToFavouritesTest),
        unittest.makeSuite(RemoveFromFavouritesTest),
        unittest.makeSuite(LikeMovieTest),
        unittest.makeSuite(DislikeMovieTest),

        # profile
        unittest.makeSuite(ClickOnSubscriptionBtnTest),
        # unittest.makeSuite(ChangeToInvalidAvatarTest), bug
        unittest.makeSuite(ChangeToValidAvatarTest),
        unittest.makeSuite(ChangeToValidEmailTest),
        unittest.makeSuite(ChangeToValidLoginTest),
        unittest.makeSuite(ChangeToValidLoginAndEmailTest),
        unittest.makeSuite(ChangeToInvalidLoginTest),
        unittest.makeSuite(ChangeToEmptyLoginTest),
        unittest.makeSuite(ChangeToEmptyEmailTest),
        unittest.makeSuite(ChangeToInvalidEmailTest),
        unittest.makeSuite(ChangeToInvalidEmailAndLoginTest),
        unittest.makeSuite(ChangeToInvalidLoginAndValidEmailTest),

        # signup
        unittest.makeSuite(TransitToLoginPageTest),
        unittest.makeSuite(SignUpWithEmptyFieldsTest),
        unittest.makeSuite(SignUpWithInvalidLoginTest),
        unittest.makeSuite(SignUpWithNumericLoginTest),
        unittest.makeSuite(SignUpWithInvalidEmailTest),
        unittest.makeSuite(SignUpWithLetterLoginTest),
        unittest.makeSuite(SignUpWithSmallPasswordTest),
        unittest.makeSuite(SignUpWithBigPasswordTest),
        unittest.makeSuite(SignUpWithDifferentPasswordsTest),
        unittest.makeSuite(SignUpWithAllInvalidFieldsTest),
        unittest.makeSuite(SignUpAlreadySignupedTest),
        # unittest.makeSuite(SignUpTest), # работет, но активируем, когда будет сделано удаление аккаунта

        # search popup
        unittest.makeSuite(ClosePopupTest),
        unittest.makeSuite(EnterLetterTest),
        unittest.makeSuite(FindMovieTest),
        unittest.makeSuite(FindActorTest),

        # actor
        unittest.makeSuite(ClickOnMovieTest),
        unittest.makeSuite(ClickOnMovieNameTest),

        # favourites
        unittest.makeSuite(ClickOnMovieTestFavourites),
        unittest.makeSuite(NotOpenedTest),
        unittest.makeSuite(OnlyAddedMoviesTest),

        # player
        # unittest.makeSuite(CloseFullscreenTest) # баг, починим в таска RED-...
        unittest.makeSuite(ClosedTest),
        # unittest.makeSuite(EscToPartScreenTest) # баг, починим в таска RED-...
        unittest.makeSuite(NotOpenedTest),

    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
