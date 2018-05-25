#!/usr/bin/env python3

import os
import sys
import unittest


from util import config


if __name__ == '__main__':
    os.environ[config.PREFERRED_BROWSER_KEY] = config.PREF_CHROME
    suite = unittest.TestLoader().discover(config.TEST_DIR)
    result = unittest.TextTestRunner().run(suite)
    os.environ[config.PREFERRED_BROWSER_KEY] = config.PREF_FIREFOX
    suite = unittest.TestLoader().discover(config.TEST_DIR)

    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
