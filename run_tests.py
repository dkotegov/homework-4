#!/usr/bin/env python2

import sys
import unittest
from tests.createFilter import CreateNewFilterTest

if __name__ == '__main__':
	suite = unittest.TestSuite((
        unittest.makeSuite(CreateNewFilterTest),
    ))
	result = unittest.TextTestRunner().run(suite)
    #sys.exit(not result.wasSuccessful())
    