import sys
import unittest
from tests.folder_test import FolderTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(FolderTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
