# -*- coding: utf-8 -*-
import unittest
import sys
from login import *

if __name__ == '__main__':
        check_list = os.environ.get('HW4CHECKLIST', 'ALL')

        test_set1 = unittest.makeSuite(UploadTest), unittest.makeSuite(CloseTest), unittest.makeSuite(
                UploadAnySizes), unittest.makeSuite(UploadAnyNamesLatin), unittest.makeSuite(UploadAnyNamesCyrillic)
        test_set2 = unittest.makeSuite(CopyTests), unittest.makeSuite(MovementTests), unittest.makeSuite(RenameTests)
        test_set = test_set = test_set1 + test_set2
        if check_list == 'ANNA':
                test_set = test_set1
        elif check_list == 'OLEG':
                test_set = test_set2

        suite = unittest.TestSuite((unittest.makeSuite(
                UploadAnySizes)))
        result = unittest.TextTestRunner().run(suite)
        sys.exit(not result.wasSuccessful())