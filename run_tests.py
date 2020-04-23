# -*- coding: utf-8 -*-

import sys
import unittest
import tests.cases.user_test as signup
from tests.cases import chat_test, search_test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(signup.Test),
        # unittest.makeSuite(chat_test.Test),
        unittest.makeSuite(search_test.Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
