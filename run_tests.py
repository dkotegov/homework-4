# -*- coding: utf-8 -*-

import unittest
import sys

from egogoger.run_egogoger_tests import run_egogoger_tests
from margarita.run_tests import run_tests as run_tests_margarita
from nikita.run_tests import run_tests as run_tests_nikita
if __name__ == '__main__':
    run_egogoger_tests()
    run_tests_margarita()
    run_tests_nikita()
