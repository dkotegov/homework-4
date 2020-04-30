# -*- coding: utf-8 -*-

import sys
import unittest
from tests.cases import chat_test, search_test, user_test, general_test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(user_test.Test),
        unittest.makeSuite(chat_test.Test),
        unittest.makeSuite(search_test.Test),
        unittest.makeSuite(general_test.Test)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
