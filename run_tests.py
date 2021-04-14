import sys
import unittest

from tests.folder_tests.test.pop3_test import POP3Test
from tests.folder_tests.test.clear_folder_test import ClearFolderTest
from tests.folder_tests.test.to_edit_test import ToEditTest
from tests.folder_tests.test.folder_test import FolderTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(POP3Test),
        # unittest.makeSuite(ClearFolderTest),
        unittest.makeSuite(ToEditTest),
        # unittest.makeSuite(FolderTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
