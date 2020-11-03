import sys
import unittest
from tests.tests_yakovidis.authentication import AuthenticationTest
from tests.tests_yakovidis.profile import ProfileTest
from tests.tests_yakovidis.registration import RegistrationTest
from tests.tests_postnikov.test import AddRestaurantTest
from tests.tests_yakovidis.change_address import AddressTest
from tests.tests_yakovidis.main_page import MainPageTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthenticationTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(RegistrationTest),
        unittest.makeSuite(AddressTest),
        unittest.makeSuite(MainPageTest)
    ))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful)
