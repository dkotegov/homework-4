#!/usr/bin/env python2

import sys
import unittest
from tests.tests_morozov.test import TestSearchingLetters as M_Test_1

if __name__ == '__main__':
    suite = unittest.TestSuite((
        #unittest.makeSuite(RM_Test_1),
        unittest.makeSuite(M_Test_1),

        # unittest.makeSuite(RM_Test_2),
        # unittest.makeSuite(RM_Test_3),
        # unittest.makeSuite(RM_Test_4),
        # unittest.makeSuite(RM_Test_5),
        #
        # unittest.makeSuite(TG_Test),
        #
        # unittest.makeSuite(NP_Test),
        # unittest.makeSuite(NP_Test_encr),
        # unittest.makeSuite(NP_Test_edit),
        #
        # unittest.makeSuite(DP_Test),
    ))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
