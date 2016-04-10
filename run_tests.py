# -*- coding: utf-8 -*-
import unittest
import sys
from login import *

if __name__ == '__main__':
    # AnnTests
    # suite = unittest.TestSuite((unittest.makeSuite(UploadTest), unittest.makeSuite(CloseTest),
    #                             unittest.makeSuite(UploadAnySizes), unittest.makeSuite(UploadAnyNamesLatin),
    #                             unittest.makeSuite(UploadAnyNamesCyrillic)))
        suite = unittest.TestSuite((unittest.makeSuite(UploadAnySizes),))
        result = unittest.TextTestRunner().run(suite)
        sys.exit(not result.wasSuccessful())