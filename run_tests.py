# -*- coding: utf-8 -*-

import sys
import unittest

from tests.auth_test import AuthTest
from tests.catalog_tests import CatalogTests
from tests.create_shop_test import CreateShopTest
from tests.create_topic_test import CreateDeleteTopicTest
from tests.hashtag_tests import HashTagTests
from tests.keyword_tests import SetDeleteKeyWordTests

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(CreateShopTest),
        unittest.makeSuite(CatalogTests),
        unittest.makeSuite(CreateDeleteTopicTest),
        unittest.makeSuite(SetDeleteKeyWordTests),
        unittest.makeSuite(HashTagTests),
    ])

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
