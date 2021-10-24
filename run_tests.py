import sys
import unittest
from cases.createFolder import CreateFolder


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(CreateFolder),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
