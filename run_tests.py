# -*- coding: utf-8 -*-
#!/usr/bin/env python2

import sys
import unittest
# from tests.example_test import ExampleTest
from tests.test import AuthTest, MonthToolbarTest, HeaderTest, CalendarTableTest, SidebarTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(MonthToolbarTest),
        unittest.makeSuite(HeaderTest),
        unittest.makeSuite(CalendarTableTest),
        unittest.makeSuite(SidebarTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
