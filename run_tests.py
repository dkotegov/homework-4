#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import unittest

from tests.movies.click_on_genre_test import ClickOnGenreTest as ClickOnMovieGenreTest
from tests.movies.click_on_movie_test import ClickOnMovieTest
from tests.series.click_on_genre_test import ClickOnGenreTest
from tests.series.click_on_series_test import ClickOnSeriesTest
from tests.details.tests_without_auth.transit_to_auth_page_test import TransitToAuthTest
from tests.details.tests_without_auth.click_on_actor_name_test import ClickOnActorNameTest
from tests.details.tests_with_auth.transit_to_profile_page_test import TransitToProfileTest
from tests.details.tests_with_auth.details_buttons_tests import OpenPlayerTest, AddToFavouritesTest,\
    RemoveFromFavouritesTest, LikeMovieTest, DislikeMovieTest
from tests.profile.click_on_sub_btn import ClickOnSubscriptionBtnTest
from tests.profile.change_to_invalid_avatar_test import ChangeToInvalidAvatarTest
from tests.profile.correct_update_profile_tests import ChangeToValidAvatarTest, ChangeToValidEmailTest, \
    ChangeToValidLoginTest, ChangeToValidLoginAndEmailTest
from tests.profile.error_update_profile_tests import ChangeToInvalidLoginTest, ChangeToEmptyLoginTest, \
    ChangeToInvalidEmailTest, ChangeToEmptyEmailTest, ChangeToInvalidEmailAndLoginTest, \
    ChangeToInvalidLoginAndValidEmailTest
from tests.signup.transit_to_login_page_test import TransitToLoginPageTest
from tests.signup.signup_with_errors_test import SignUpWithEmptyFieldsTest, SignUpWithInvalidLoginTest, \
    SignUpWithNumericLoginTest, SignUpWithInvalidEmailTest, SignUpWithSmallPasswordTest, SignUpWithLetterLoginTest, \
    SignUpWithBigPasswordTest, SignUpWithDifferentPasswordsTest, SignUpWithAllInvalidFieldsTest, \
    SignUpAlreadySignupedTest
from tests.signup.signup_test import SignUpTest
from tests.search_popup.close_popup_test import ClosePopupTest
from tests.search_popup.enter_letter_test import EnterLetterTest
from tests.search_popup.find_movie_test import FindMovieTest
from tests.search_popup.find_actor_test import FindActorTest
from tests.player.closed_test import ClosedTest
from tests.player.not_opened_test import NotOpenedTest
from tests.player.esc_to_part_screen_test import EscToPartScreenTest
from tests.player.close_fullscreen_test import CloseFullscreenTest
from tests.actor.click_on_movie_test import ClickOnMovieTest as ClickOnMovieActorTest
from tests.actor.click_on_movie_name_test import ClickOnMovieNameTest
from tests.favourites.click_on_movie_test import ClickOnMovieTest as ClickOnFavouriteMovieTest
from tests.favourites.not_opened_test import NotOpenedTest as NotOpenedFavouritesTest
from tests.favourites.only_added_movies_test import OnlyAddedMoviesTest
from tests.navbar.go_to_profile_test import GoToProfileTest
from tests.navbar.go_to_favourites_test import GoToFavouritesTest
from tests.navbar.go_to_main_test import GoToMainTest
from tests.navbar.logout_test import LogoutTest
from tests.navbar.go_to_movies_test import GoToMoviesTest
from tests.navbar.go_to_series_test import GoToSeriesTest
from tests.main.horizontal_scroll_tests import HorizontalScrollRightTest, HorizontalScrollLeftTest
from tests.main.click_on_watch_button_test import ClickOnWatchButtonTest
from tests.main.click_on_card_test import ClickOnCardTest
from tests.login.login_test import LoginTest
from tests.login.empty_fields_login_test import EmptyFieldsLoginTest
from tests.login.go_to_signup_test import GoToSignupTest
from tests.login.invalid_email_login_test import InvalidEmailLoginTest
from tests.login.wrong_creds_login_test import WrongCredsLoginTest
from tests.login.wrong_password_login_test import WrongPasswordLoginTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ClickOnSeriesTest),
        unittest.makeSuite(ClickOnGenreTest),
        unittest.makeSuite(ClickOnMovieTest),
        unittest.makeSuite(ClickOnMovieGenreTest),
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(LogoutTest),
        unittest.makeSuite(GoToProfileTest),
        unittest.makeSuite(GoToFavouritesTest),
        unittest.makeSuite(TransitToAuthTest),
        unittest.makeSuite(ClickOnActorNameTest),
        unittest.makeSuite(TransitToProfileTest),
        unittest.makeSuite(OpenPlayerTest),
        unittest.makeSuite(AddToFavouritesTest),
        unittest.makeSuite(RemoveFromFavouritesTest),
        unittest.makeSuite(LikeMovieTest),
        unittest.makeSuite(DislikeMovieTest),
        unittest.makeSuite(ClickOnSubscriptionBtnTest),
        unittest.makeSuite(ChangeToInvalidAvatarTest),
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
        # unittest.makeSuite(SignUpTest),
        unittest.makeSuite(ClosePopupTest),
        unittest.makeSuite(EnterLetterTest),
        unittest.makeSuite(FindMovieTest),
        unittest.makeSuite(FindActorTest),
        unittest.makeSuite(ClosedTest),
        unittest.makeSuite(NotOpenedTest),
        # unittest.makeSuite(EscToPartScreenTest),
        # unittest.makeSuite(CloseFullscreenTest),
        unittest.makeSuite(ClickOnMovieNameTest),
        unittest.makeSuite(ClickOnMovieTest),
        unittest.makeSuite(ClickOnFavouriteMovieTest),
        unittest.makeSuite(NotOpenedFavouritesTest),
        unittest.makeSuite(OnlyAddedMoviesTest),
        unittest.makeSuite(GoToMainTest),
        unittest.makeSuite(GoToMoviesTest),
        unittest.makeSuite(GoToSeriesTest),
        unittest.makeSuite(HorizontalScrollRightTest),
        unittest.makeSuite(HorizontalScrollLeftTest),
        unittest.makeSuite(ClickOnWatchButtonTest),
        unittest.makeSuite(ClickOnCardTest),
        unittest.makeSuite(EmptyFieldsLoginTest),
        unittest.makeSuite(GoToSignupTest),
        unittest.makeSuite(InvalidEmailLoginTest),
        unittest.makeSuite(InvalidEmailLoginTest),
        unittest.makeSuite(WrongCredsLoginTest),
        unittest.makeSuite(WrongPasswordLoginTest),
        unittest.makeSuite(ClickOnMovieActorTest)
    ))

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
