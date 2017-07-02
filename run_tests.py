#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from tests.event_list_page.event_list_page_tests import EventListTests
from tests.create_page.create_page_tests import CreatePageTests
from tests.event_page.event_page_tests import EventPageTests

if __name__ == '__main__':
    tests_classes = [
        EventListTests,
        CreatePageTests,
        EventPageTests,
    ]
    suites = []
    test_loader = unittest.TestLoader()
    for test_class in tests_classes:
        suites.append(test_loader.loadTestsFromTestCase(test_class))

    suite = unittest.TestSuite(suites)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
