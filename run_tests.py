# -*- coding: utf-8 -*-
#!/usr/bin/env python2

import sys
import unittest
# from tests.example_test import ExampleTest
from tests.test  import AuthTest, MonthToolbarTest, HeaderTest, CalendarTableTest, SidebarTest
from tests.test2 import DateTest, ExtraTest, CitiesTest, CalendarTest
from tests.testWeekPage import Tests


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(Tests),
        # unittest.makeSuite(DateTest),
        # unittest.makeSuite(ExtraTest),
        # unittest.makeSuite(CitiesTest),
        # unittest.makeSuite(CalendarTest),
        # unittest.makeSuite(AuthTest),
        # unittest.makeSuite(MonthToolbarTest),
        # unittest.makeSuite(HeaderTest),
        unittest.makeSuite(CalendarTableTest),
        # unittest.makeSuite(SidebarTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
