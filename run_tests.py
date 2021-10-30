import unittest
from tests.auth_test import AuthTest
from tests.profile_test import ProfileTest
from tests.main_test import MainTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainTest),
    ))
    result = unittest.TextTestRunner().run(suite)
