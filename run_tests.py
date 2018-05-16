#!/usr/bin/env python3
import unittest

from library.selenium import ScreenshotTextTestRunner

if __name__ == '__main__':
    unittest.main(testRunner=ScreenshotTextTestRunner)
