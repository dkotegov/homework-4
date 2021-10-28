import unittest

from tests.auth_test import AuthTest
from tests.profile_test import ProfileTest
from tests.signup_test import SignupTest
from tests.change_password_test import ChangePasswordTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(SignupTest),
        unittest.makeSuite(ChangePasswordTest)
    ))
    result = unittest.TextTestRunner().run(suite)
