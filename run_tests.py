#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import unittest

from tests.event_list_page import event_list_page_tests as elp
from tests.create_page import create_page_tests as cp
from tests.event_page import event_page_tests as ep

if __name__ == '__main__':
    tests = [
        elp.Test1,
        elp.Test2,
        elp.Test3,
        elp.Test4,
        elp.Test5,
        elp.Test6,
        cp.Test1,
        cp.Test2,
        cp.Test3,
        ep.Test1,
        ep.Test2,
        ep.Test3,
        ep.Test4,
        ep.Test5,
        ep.Test6,
        ep.Test7,
    ]
    tests = map(unittest.makeSuite, tests)
    suite = unittest.TestSuite(tests)
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
