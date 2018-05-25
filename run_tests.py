import sys
import unittest

if __name__ == '__main__':
    suite = unittest.TestLoader().discover('tests')
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
