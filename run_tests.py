#!/usr/bin/env python2

import sys
import unittest
from tests import DirectoryTest
from tests import SortAndFilterTest
from tests import CreatingDocumentsTest
from tests import TabsAtHomePageTest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TabsAtHomePageTest))
    suite.addTests(loader.loadTestsFromTestCase(SortAndFilterTest))
    suite.addTests(loader.loadTestsFromTestCase(CreatingDocumentsTest))
    suite.addTests(loader.loadTestsFromTestCase(DirectoryTest))

    result = unittest.TextTestRunner(verbosity=3).run(suite)
    sys.exit(not result.wasSuccessful())
