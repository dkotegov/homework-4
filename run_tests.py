# -*- coding: utf-8 -*-

# import sys
# import unittest
# from tests.tests import PhotoAlbumTests

# if __name__ == '__main__':
#     suite = unittest.TestSuite((
#         unittest.makeSuite(PhotoAlbumTests),
#     ))
#     result = unittest.TextTestRunner().run(suite)
#     sys.exit(not result.wasSuccessful())

import unittest
from tests.tests import buklin_tests

if __name__ == '__main__':

    for test_suite in buklin_tests:
        unittest.TextTestRunner().run(test_suite)
