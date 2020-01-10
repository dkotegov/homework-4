import sys
import unittest

from tests.LoginTest import LoginTest
from tests.SettingsTest import SettingsTest
from tests.MainTest import MainTest
from tests.DirectoryTest import DirectoryTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(MainTest),
        unittest.makeSuite(LoginTest),
        unittest.makeSuite(SettingsTest),
        unittest.makeSuite(DirectoryTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
