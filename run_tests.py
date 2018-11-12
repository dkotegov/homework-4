#!/usr/bin/env python2

import sys
import unittest

from tests.QA_72_Migranov.test import Test as RM_Test
from tests.Garifullin.test import Test as TG_Test
from tests.Poponkin.test import Test as DP_Test
from tests.Parpibaeva.test import Test as NP_Test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(RM_Test),
        unittest.makeSuite(TG_Test),
        unittest.makeSuite(DP_Test),
        unittest.makeSuite(NP_Test),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())