# -*- coding: utf-8 -*-

import unittest
import sys
from tests import Tests

if __name__ == '__main__':
    suite = unittest.TestSuite((unittest.makeSuite(Tests)),)
    result = unittest.TextTestRunner().run(suite)
