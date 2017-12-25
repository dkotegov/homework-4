#!/usr/bin/env python2

import unittest

from tests_rogachev import photos_page_tests
from tests_rogachev import search_input_tests
from tests_rogachev import search_page_tests


if __name__ == '__main__':

    tests = [
        unittest.TestSuite((
            unittest.makeSuite(photos_page_tests.AddAndDeleteNewAlbum)
        )),
        unittest.TestSuite((
            unittest.makeSuite(photos_page_tests.AddAndDeleteNewPhoto)
        )),

        unittest.TestSuite((
            unittest.makeSuite(search_input_tests.SearchInputSubmitTest),
        )),

        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageSetCountryTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageSetFullLocationTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageAgeLimitTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageGroupSearchTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageMusicTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageMusicAlbumTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageUniversityTest)
        )),
        unittest.TestSuite((
            unittest.makeSuite(search_page_tests.SearchPageGenderTest),
        )),
    ]

    for test_suite in tests:
        unittest.TextTestRunner().run(test_suite)
