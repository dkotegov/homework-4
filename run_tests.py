import sys
import unittest
from tests.folder_tests.test.folder_test import FolderTest
from tests.contacts_and_addresses.test.phone_test import PhoneTest
from tests.folder_tests.test.pop3_test import POP3Test
from tests.folder_tests.test.to_edit_test import ToEditTest
from tests.contacts_and_addresses.test.email_test import EmailTest



if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(FolderTest),
        # unittest.makeSuite(PhoneTest),
        unittest.makeSuite(EmailTest),
        # unittest.makeSuite(POP3Test),
        # unittest.makeSuite(ToEditTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
