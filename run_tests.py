# -*- coding: utf-8 -*-

import sys
import unittest
import tests.cases.user_test as signup
from tests.cases import auth_test
from tests.cases import registration_test
from tests.cases import user_profile_test
from tests.cases import settings_profile_test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(signup.Test),

        # Ok tests
        # unittest.makeSuite(auth_test.AuthTest)

        # Ok tests
        # unittest.makeSuite(registration_test.RegTest),

        # Ok tests
        # unittest.makeSuite(user_profile_test.ProfileTest),

        # Ok tests
        # unittest.makeSuite(settings_profile_test.SettingsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
