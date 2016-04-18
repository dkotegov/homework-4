# -*- coding: utf-8 -*-

import sys
import unittest
from tests.common_blocks_test import *
from tests.favorites_page_test import *
from tests.awards_page_test import *
from tests.profile_page_test import *
from tests.ratings_page_test import *

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ProfilePageTestCase),
        unittest.makeSuite(AwardsPageTestCase),
        unittest.makeSuite(CommonBlocksTestCase),
        unittest.makeSuite(FavoritesPageTestCase),
        unittest.makeSuite(RatingsPageTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
