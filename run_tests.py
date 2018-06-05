# -*- coding: utf-8 -*-

import sys
import unittest

from tests.products_tests import ProductsTests
from tests.auth_test import AuthTest
from tests.create_catalog_tests import CreateCatalogTests
from tests.create_remove_shop_test import CreateRemoveShopTest
from tests.delete_catalog_tests import DeleteCatalogTests
from tests.edit_catalog_tests import EditCatalogTests
from tests.post_tests import PostTests

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(CreateRemoveShopTest),
        unittest.makeSuite(CreateCatalogTests),
        unittest.makeSuite(EditCatalogTests),
        unittest.makeSuite(DeleteCatalogTests),
        unittest.makeSuite(ProductsTests),
        unittest.makeSuite(PostTests)
    ])

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
