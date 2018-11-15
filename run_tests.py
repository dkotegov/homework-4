#!/usr/bin/env python2

import sys
import unittest

from tests.QA_72_Migranov.test import Test as RM_Test
from tests.Garifullin.test_1 import FolderDeleteTest as TG_Test_1
from tests.Garifullin.test_2 import FolderDeleteTest as TG_Test_2
from tests.Garifullin.test_3 import FolderDeleteTest as TG_Test_3
from tests.Garifullin.test_4 import FolderDeleteTest as TG_Test_4
from tests.Garifullin.test_5 import FolderDeleteTest as TG_Test_5
from tests.Poponkin.test import Test as DP_Test
from tests.Parpibaeva.test import Test as NP_Test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(RM_Test),
        unittest.makeSuite(TG_Test_1),
        unittest.makeSuite(TG_Test_2),
        unittest.makeSuite(TG_Test_3),
        unittest.makeSuite(TG_Test_4),
        unittest.makeSuite(TG_Test_5),
        unittest.makeSuite(DP_Test),
        unittest.makeSuite(NP_Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())