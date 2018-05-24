import sys
import unittest

from tests.test_settings import *

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(TestsAddApp),
        # unittest.makeSuite(TestsChangeNameAndDescriptions),
        unittest.makeSuite(TestsAddStuff),
        # unittest.makeSuite(TestsAddGroupLinks),
        # unittest.makeSuite(TestsChangeType),
        # unittest.makeSuite(TestsHideSections),
        # unittest.makeSuite(TestsForbiddenComments),
        # unittest.makeSuite(TestsAddAPIKey),
        # unittest.makeSuite(TestsHideObsceneLanguage)
    ))
    result = unittest.TextTestRunner(failfast=True, verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
