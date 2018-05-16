#!/usr/bin/env python3
import sys
from os.path import join, dirname, realpath
from unittest import TestLoader

from config import TESTS_DIR, TEST_PATTERN
from library.selenium import ScreenshotTextTestRunner

if __name__ == '__main__':
    loader = TestLoader()
    tests_dir = join(dirname(realpath(__file__)), TESTS_DIR)
    tests = loader.discover(tests_dir, pattern=TEST_PATTERN)
    runner = ScreenshotTextTestRunner()
    result = runner.run(tests)
    sys.exit(not result.wasSuccessful())
