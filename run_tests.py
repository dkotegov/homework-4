#!/usr/bin/env python3

import sys
import unittest

from tests.comments_test import CommentsTest
from tests.mobile_album_create_test import MobileAlbumCreateTest
from tests.mobile_album_test import MobileAlbumTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MobileAlbumCreateTest),
        unittest.makeSuite(MobileAlbumTest),
        unittest.makeSuite(CommentsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
