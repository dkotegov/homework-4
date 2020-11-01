# -*- coding: utf-8 -*-
import sys
import unittest
from tests import FolderTests, TrashBinTests, HistoryTests, WorkWithFilesTests

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # suite.addTests(loader.loadTestsFromTestCase(FolderTests))
    suite.addTests(loader.loadTestsFromTestCase(WorkWithFilesTests))
    # suite.addTests(loader.loadTestsFromTestCase(TrashBinTests))
    # suite.addTests(loader.loadTestsFromTestCase(HistoryTests))

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
