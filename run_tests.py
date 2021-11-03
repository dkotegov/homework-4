import unittest

from tests.profile.auth_test import AuthTest
from tests.profile.profile_test import ProfileTest
from tests.profile.signup_test import SignupTest
from tests.profile.change_password_test import ChangePasswordTest

from tests.main.messages_test import MessagesTest
from tests.main.editor_test import EditorTest
from tests.main.dialogues_test import DialoguesTest
from tests.main.folders_test import FoldersTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(ProfileTest),
        unittest.makeSuite(SignupTest),
        unittest.makeSuite(ChangePasswordTest),

        unittest.makeSuite(MessagesTest),
        unittest.makeSuite(EditorTest),
        unittest.makeSuite(DialoguesTest),
        unittest.makeSuite(FoldersTest)
    ))
    result = unittest.TextTestRunner().run(suite)
