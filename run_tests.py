#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import unittest
from like_tests.tests.auth import AuthTests
from like_tests.tests.photo import LikePhotoTests
from like_tests.tests.gift import GiftLikeTests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(AuthTests),
        unittest.makeSuite(LikePhotoTests),
        unittest.makeSuite(GiftLikeTests)
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
