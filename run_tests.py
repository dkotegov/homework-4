# -*- coding: utf-8 -*-
import sys
import unittest

from tests.auth_test import AuthTest
from tests.create_catalog_tests import CreateCatalogTests
from tests.create_remove_shop_test import CreateRemoveShopTest
from tests.create_topic_test import CreateTopicTest
from tests.edit_catalog_tests import EditCatalogTests
from tests.hashtag_tests import HashTagTests
from tests.topic_hashtag_tests import TopicHashTagsTests
from tests.products_tests import ProductsTests
from tests.remove_catalog_tests import RemoveCatalogTests

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(CreateRemoveShopTest),
        unittest.makeSuite(CreateCatalogTests),
        unittest.makeSuite(EditCatalogTests),
        unittest.makeSuite(RemoveCatalogTests),
        unittest.makeSuite(ProductsTests),
        unittest.makeSuite(CreateTopicTest),
        unittest.makeSuite(TopicHashTagsTests),
        unittest.makeSuite(HashTagTests),
    ])

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
