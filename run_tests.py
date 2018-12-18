#!/usr/bin/env python2

import sys
import unittest
from tests.tests_morozov.test import TestSearchingLetters as M_Tests
from tests.tests_babkov.test import TestSearchLetters as B_Tests

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(M_Tests),
        unittest.makeSuite(B_Tests),
    ))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
