import sys
import unittest
from tests.tests_yakovidis.authentication import AuthenticationTest
from tests.tests_postnikov.add_restaurants import AddRestaurantTest
from tests.tests_postnikov.add_rest_point import AddPointTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AuthenticationTest)
        unittest.makeSuite(AddPointTest)
        # unittest.makeSuite(AddRestaurantTest)
    ))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful)
