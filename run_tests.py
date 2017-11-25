# -*- coding: utf-8 -*-

import unittest

from vp_check_list.run_tests import vp_tests
from es_check_list.run_tests import es_tests

if __name__ == '__main__':

    vp_suite = unittest.TestSuite(
        vp_tests()
    )
    es_suite = unittest.TestSuite(
        es_tests()
    )

    result = unittest.TextTestRunner().run(vp_suite)
    result = unittest.TextTestRunner().run(es_suite)
