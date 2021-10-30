# -*- coding: utf-8 -*-

import sys
import unittest
from tests.movies.click_on_movie_test import ClickOnMovieTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(ClickOnMovieTest),

    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
