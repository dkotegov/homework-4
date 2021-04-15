import sys
import os
from multiprocessing import Process
from typing import List
import subprocess
from testutils import GlobalCurrentBrowser

import unittest

import settings


def run_tests(tests: List):
    suites = []
    for test in tests:
        suites.append(unittest.makeSuite(test))
    suite = unittest.TestSuite(suites)
    return unittest.TextTestRunner().run(suite)


def init_grid():
    subprocess.call(['sh', './grid.sh', settings.SELENIUM_BIN])


def init_node():
    subprocess.call(['sh', './node.sh', settings.CHROME_BIN, settings.FIREFOX_BIN, settings.SELENIUM_BIN])


def run_selenium():
    grid = Process(target=init_grid)
    node = Process(target=init_node)
    grid.start()
    node.start()
    grid.join()
    node.join()


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Usage: python manage.py [test, run_selenium]")

    if sys.argv[1] == 'test':
        results = []
        for browser in settings.BROWSERS:

            GlobalCurrentBrowser.set(browser)
            result = run_tests(settings.TESTS)
            results.append(result.wasSuccessful())
        if len(results) == 0:
            print("You should specify browsers in settings")
            sys.exit(1)

        sys.exit(False in results)
    elif sys.argv[1] == 'run_selenium':
        run_selenium()
