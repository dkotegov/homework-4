import unittest

from search_input_tests import SearchInputPopupTest, \
    SearchInputOverlayTest, \
    SearchInputSuggestionsShowAllTest, \
    SearchInputSubmitTest

from search_page_tests import SearchPageDefaultSearchTest, \
    SearchPageGenderTest, \
    SearchPageAgeTest, \
    SearchPageHideFilterTest, \
    SearchPageClearTest, \
    SearchPageFilterTagsTest, \
    SearchPageClearFilterTest


tests_orel = [
    # search_input_tests
    SearchInputPopupTest,
    SearchInputOverlayTest,
    SearchInputSuggestionsShowAllTest,
    SearchInputSubmitTest,

    # search_page_tests
    SearchPageDefaultSearchTest,
    SearchPageGenderTest,
    SearchPageAgeTest,
    SearchPageHideFilterTest,
    SearchPageClearTest,
    SearchPageFilterTagsTest,
    SearchPageClearFilterTest,
]

run_tests_orel = list(map(
    lambda test:
        unittest.TestSuite((
            unittest.makeSuite(test),
        )),
    tests_orel
))
