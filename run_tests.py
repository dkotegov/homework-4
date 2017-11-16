# -*- coding: utf-8 -*-

import sys
import unittest

from es_check_list.tests import tests


if __name__ == '__main__':
    suite = unittest.TestSuite(
        tests
    )
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
