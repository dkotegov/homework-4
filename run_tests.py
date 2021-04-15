import sys
import unittest

from tests.contacts_and_addresses.test.phone_test import PhoneTest
from tests.contacts_and_addresses.test.email_test import EmailTest

from tests.folder_tests.test.pop3_test import POP3Test
from tests.folder_tests.test.clear_folder_test import ClearFolderTest
from tests.folder_tests.test.to_edit_test import ToEditTest
from tests.folder_tests.test.folder_test import FolderTest
from tests.folder_tests.test.password_test import PasswordTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(PhoneTest),
        unittest.makeSuite(EmailTest),
        unittest.makeSuite(POP3Test),
        unittest.makeSuite(ClearFolderTest),
        unittest.makeSuite(ToEditTest),
        unittest.makeSuite(FolderTest),
        unittest.makeSuite(PasswordTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
