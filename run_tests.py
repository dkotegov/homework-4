#!/usr/bin/env python2

import sys
import unittest
from tests.signup.signup_success import SignupSuccessTests
from tests.signup.signup_wrong import SignupWrongTests
from tests.subscribe.subscribe_tests import SubscribeTests
from tests.subscribe.unsubscribe_tests import UnsubscribeTests
from tests.rating.rating_first_time_tests import RatingTestsFirst
from tests.rating.rerating_tests import ReratingTests
from tests.auth.auth_success import AuthTests
from tests.search.film_search_tests import FilmSearchTests
from tests.search.actors_search_tests import ActorsSearchTests
from tests.search.people_search_tests import PeopleSearchTests
from tests.search.save_instanse_search_test import SaveInstanceSearchTests
from tests.comment.comments_tests import CommentsTests

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # suite.addTest(unittest.makeSuite(SettingsTests))
    #suite.addTest(unittest.makeSuite(AuthTests))
    #suite.addTest(unittest.makeSuite(SignupSuccessTests))
    #suite.addTest(unittest.makeSuite(SignupWrongTests))
    #suite.addTest(unittest.makeSuite(SubscribeTests))
    #suite.addTest(unittest.makeSuite(UnsubscribeTests))
    #suite.addTest(unittest.makeSuite(RatingTestsFirst))
    #suite.addTest(unittest.makeSuite(ReratingTests))
    # suite.addTest(unittest.makeSuite(PlaylistTests))
    #suite.addTest(unittest.makeSuite(FilmSearchTests))
    #suite.addTest(unittest.makeSuite(ActorsSearchTests))
    #suite.addTest(unittest.makeSuite(PeopleSearchTests))
    #suite.addTest(unittest.makeSuite(SaveInstanceSearchTests))
    suite.addTest(unittest.makeSuite(CommentsTests))
    # suite.addTest(unittest.makeSuite(CommentTests))
    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
