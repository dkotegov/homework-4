# -*- coding: utf-8 -*-
import sys
import unittest
from tests import *


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(FolderTests))
    suite.addTests(loader.loadTestsFromTestCase(WorkWithFilesTests))
    suite.addTests(loader.loadTestsFromTestCase(TrashBinTests))
    suite.addTests(loader.loadTestsFromTestCase(HistoryTests))

    suite.addTests(loader.loadTestsFromTestCase(TabsAtHomePageTest))
    suite.addTests(loader.loadTestsFromTestCase(SortAndFilterTest))
    suite.addTests(loader.loadTestsFromTestCase(CreatingDocumentsTest))
    suite.addTests(loader.loadTestsFromTestCase(DirectoryTest))

    result = unittest.TextTestRunner(verbosity=3).run(suite)
    sys.exit(not result.wasSuccessful())
