#!/usr/bin/env python2

import sys
import unittest

from tests.gifts_page_tests import GiftsPageTests
from tests.gifts_dialog_page_tests import GiftDialogPageTests
from tests.main_page_tests import MainPageTests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(MainPageTests),
        # unittest.makeSuite(GiftsPageTests),
        unittest.makeSuite(GiftDialogPageTests),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
