# -*- coding: utf-8 -*-

import sys
import unittest
from tests.shop_tests import ShopTests
from tests.post_tests import PostTests

if __name__ == '__main__':
    suite = unittest.TestSuite([
        # unittest.makeSuite(ShopTests),
        unittest.makeSuite(PostTests)])

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
