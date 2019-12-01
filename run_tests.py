import sys
import unittest

from LoginTest import LoginTest
from CalendarTest import CalendarTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(LoginTest),
        unittest.makeSuite(CalendarTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
