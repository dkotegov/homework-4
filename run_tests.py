import unittest
from tests.auth_test import AuthTest
from tests.profile_test import ProfileTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(ProfileTest)
    ))
    result = unittest.TextTestRunner().run(suite)
