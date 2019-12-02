import sys
import unittest

from EventTest import EventTest

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(EventTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
