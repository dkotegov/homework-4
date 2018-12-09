#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import unittest
from tests.createFilterTests import CreateFilterTest
from tests.changeFilterTests import ChangeFilterTest
from tests.errorCheckingTests import ErrorCheckingTest

if __name__ == '__main__':
    #create_filters_test = unittest.TestLoader().loadTestsFromTestCase(CreateFilterTest)
    change_filter_test = unittest.TestLoader().loadTestsFromTestCase(ChangeFilterTest)
    #error_checking_test = unittest.TestLoader().loadTestsFromTestCase(ErrorCheckingTest)
    #suite = unittest.TestSuite([create_filters_test, change_filter_test, error_checking_test])
    suite = unittest.TestSuite([change_filter_test])
    result = unittest.TextTestRunner().run(suite)