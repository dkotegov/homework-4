import sys
import unittest

from test.auth.auth_success import AuthTests
from test.menu.function_menu import MenuTests

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MenuTests))
    suite.addTest(unittest.makeSuite(AuthTests))
    result = unittest.TextTestRunner().run(suite)
    successfulRes = result.wasSuccessful()
    if not successfulRes:
        sys.exit(not successfulRes)
