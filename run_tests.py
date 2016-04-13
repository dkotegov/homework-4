# -*- coding: utf-8 -*-

import sys

from tests.profile_page_test import *

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainHeaderTestCase)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
