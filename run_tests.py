# -*- coding: utf-8 -*-

import unittest

from tests.eugenmorozov.future_date import FutureDateTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(DP_Test),
    ))
    print("Hello1!!!")
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())