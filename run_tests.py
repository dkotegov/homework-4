# -*- coding: utf-8 -*-
import unittest
import sys
from login import *

if __name__ == '__main__':
        # suite = unittest.TestSuite((unittest.makeSuite(AuthTest), unittest.makeSuite(UploadTest),
        #                             unittest.makeSuite(CloseTest)))
        suite = unittest.TestSuite((unittest.makeSuite(UploadAnySizes),))
        result = unittest.TextTestRunner().run(suite)
        sys.exit(not result.wasSuccessful())