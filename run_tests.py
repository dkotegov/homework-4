import subprocess
import sys
import unittest

from tests.LoginTest import LoginTest
from tests.SettingsTest import SettingsTest
from tests.MainTest import MainTest
from tests.DirectoryTest import DirectoryTest
from tests.SignUpTest import SignUpTest
from tests.config import config

if __name__ == '__main__':
    if (not config.DRIVER):
        subprocess.Popen(["bash", "./hub.sh"])
        subprocess.Popen(["bash", "./node.sh"])
    suite = unittest.TestSuite((
        # unittest.makeSuite(SignUpTest),
        # unittest.makeSuite(MainTest),
        # unittest.makeSuite(LoginTest),
        # unittest.makeSuite(SettingsTest),
        unittest.makeSuite(DirectoryTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())