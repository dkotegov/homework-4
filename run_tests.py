import unittest

from tests.auth_test import AuthTest
from tests.profile_test import ProfileTest
from tests.signup_test import SignupTest
from tests.change_password_test import ChangePasswordTest

from tests.main.main_test import MainTest
from tests.main.editor_test import EditorTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(SignupTest),
        unittest.makeSuite(ChangePasswordTest),

        unittest.makeSuite(MainTest),
        unittest.makeSuite(EditorTest)
    ))
    result = unittest.TextTestRunner().run(suite)
