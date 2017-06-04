#!/usr/bin/env python2

import sys
import unittest
from tests.people_test import PeopleTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(PeopleTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
