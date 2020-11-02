#!/usr/bin/env python2

import sys
import unittest
from tests.example_test import DirectoryTest
from tests.example_test import ButtonsTest


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(ButtonsTest))
    suite.addTests(loader.loadTestsFromTestCase(DirectoryTest))

    result = unittest.TextTestRunner(verbosity=3).run(suite)
    sys.exit(not result.wasSuccessful())
