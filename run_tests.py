import sys
import unittest
from tests.tests_postnikov.test import FirstTest, AddRestaurantTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AddRestaurantTest)
    ))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful)
