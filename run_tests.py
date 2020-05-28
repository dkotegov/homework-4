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


    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
