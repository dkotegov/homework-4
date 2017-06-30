#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from tests import event_list_page_tests as elp
from tests import create_page_tests as cp

if __name__ == '__main__':
    tests = [
        # elp.Test1,
        # elp.Test2,
        # elp.Test3,
        # elp.Test4,
        # elp.Test5,
        # elp.Test6,
        # cp.Test1,
        # cp.Test2,
        cp.Test3,
    ]
    print tests

    tests = map(unittest.makeSuite, tests)
    suite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
