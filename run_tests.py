import sys
import unittest
from tests.userinfo_wrongtown_test import WrongTownTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(WrongTownTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())