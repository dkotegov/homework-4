# -*- coding: utf-8 -*-
import sys
import unittest
from tests import FolderTests

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    suite.addTests(loader.loadTestsFromTestCase(FolderTests))

    result = unittest.TextTestRunner(verbosity=3).run(suite)
    sys.exit(not result.wasSuccessful())
