# -*- coding: utf-8 -*-

import sys
import unittest

from tests.auth_test import AuthTest
from tests.catalog_tests import CatalogTests
from tests.create_shop_test import CreateShopTest
from tests.post_tests import PostTests

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(CreateShopTest),
        unittest.makeSuite(CatalogTests),
        unittest.makeSuite(PostTests)
    ])

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
