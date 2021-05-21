#!/usr/bin/env python2

import sys
import unittest
from tests.signup.signup_success import SignupSuccessTests
from tests.signup.signup_wrong import SignupWrongTests
from tests.subscribe.subscribe_tests import SubscribeTests
from tests.subscribe.unsubscribe_tests import UnsubscribeTests
from tests.auth.auth_success import AuthTests


if __name__ == '__main__':
    suite = unittest.TestSuite()
    #suite.addTest(unittest.makeSuite(AuthTests))
    # suite.addTest(unittest.makeSuite(SettingsTests))
    #suite.addTest(unittest.makeSuite(SignupSuccessTests))
    #suite.addTest(unittest.makeSuite(SignupWrongTests))
    suite.addTest(unittest.makeSuite(SubscribeTests))
    suite.addTest(unittest.makeSuite(UnsubscribeTests))
    # suite.addTest(unittest.makeSuite(SubscribeTests))
    # suite.addTest(unittest.makeSuite(PlaylistTests))
    # suite.addTest(unittest.makeSuite(RatingTests))
    # suite.addTest(unittest.makeSuite(SearchTests))
    # suite.addTest(unittest.makeSuite(CommentTests))
    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
