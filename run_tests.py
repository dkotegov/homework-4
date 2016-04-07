# -*- coding: utf-8 -*-
import unittest
import sys
from login import *

if __name__ == '__main__':
        suite = unittest.TestSuite((unittest.makeSuite(UploadTest),))
        result = unittest.TextTestRunner().run(suite)
        sys.exit(not result.wasSuccessful())