# -*- coding: utf-8 -*-
import sys
import unittest
from tests import *


def create_suite(test_cases) -> unittest.TestSuite:
    loader = unittest.TestLoader()
    new_suite = unittest.TestSuite()

    for test_case in test_cases:
        new_suite.addTests(loader.loadTestsFromTestCase(test_case))

    return new_suite


if __name__ == '__main__':
    tests = [
        # FolderTests,
        # WorkWithFilesTests,
        # TrashBinTests,
        # HistoryTests,
        #
        # TabsAtHomePageTest,
        # SortAndFilterTest,
        # CreatingDocumentsTest,
        # DirectoryTest,
        #
        # RecommendTests,
        # DragAndDropUploadTests,
        UsualUploadTests
    ]

    suite = create_suite(tests)

    result = unittest.TextTestRunner(verbosity=3).run(suite)
    sys.exit(not result.wasSuccessful())
