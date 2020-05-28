# -*- coding: utf-8 -*-

import sys
import unittest

from tests.cases import chat_test, search_test, user_test, general_test, pin_view_test
import tests.cases.user_test as signup
from tests.cases import auth_test
from tests.cases import registration_test
from tests.cases import user_profile_test
from tests.cases import settings_profile_test
from tests.cases import board_test
from tests.cases import pin_test
from tests.cases import edit_pin_test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(board_test.Test),
        unittest.makeSuite(pin_view_test.Test),
        unittest.makeSuite(user_test.Test),
        unittest.makeSuite(chat_test.Test),
        unittest.makeSuite(search_test.Test),
        unittest.makeSuite(general_test.Test),

        unittest.makeSuite(signup.Test),

        # Ok tests
        unittest.makeSuite(auth_test.AuthTest),

        # Ok tests
        unittest.makeSuite(registration_test.RegTest),

        # Ok tests
        unittest.makeSuite(user_profile_test.ProfileTest),

        # Ok tests
        unittest.makeSuite(settings_profile_test.SettingsTest),
        unittest.makeSuite(pin_test.Test),
        unittest.makeSuite(edit_pin_test.Test),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
