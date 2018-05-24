# -*- coding: utf-8 -*-

import unittest
from tests import Tests
from alltests import TestsBuevichGusev

if __name__ == '__main__':
    suite = unittest.TestSuite((unittest.makeSuite(Tests)),)
    result = unittest.TextTestRunner().run(suite)
