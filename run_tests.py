# -*- coding: utf-8 -*-
# !/usr/bin/env python3

import sys
import unittest
import test

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(test.ExampleTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
