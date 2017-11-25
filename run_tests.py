#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
from like_tests.tests.auth import *
from like_tests.tests.photo import *


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AuthTests),
        unittest.makeSuite(LikePhotoTests)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
