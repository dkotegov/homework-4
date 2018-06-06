# -*- coding: utf-8 -*-

import sys
import unittest

from tests.auth_test import AuthTest
from tests.create_catalog_tests import CreateCatalogTests
from tests.create_remove_shop_test import CreateRemoveShopTest
from tests.remove_catalog_tests import RemoveCatalogTests
from tests.edit_catalog_tests import EditCatalogTests
from tests.products_tests import ProductsTests

if __name__ == '__main__':
    suite = unittest.TestSuite([
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(CreateRemoveShopTest),
        unittest.makeSuite(CreateCatalogTests),
        unittest.makeSuite(EditCatalogTests),
        unittest.makeSuite(RemoveCatalogTests),
        unittest.makeSuite(ProductsTests)
    ])

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
