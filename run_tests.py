#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys
import unittest
from tests.slider_test import RealtyTestCase


if __name__ == '__main__':
    #unittest.main(verbosity=2)
    suite = unittest.TestSuite((
        unittest.makeSuite(RealtyTestCase),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
