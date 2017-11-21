# -*- coding: utf-8 -*-

import unittest

from vp_check_list.run_tests import vp_tests

if __name__ == '__main__':
	for test_suite in vp_tests():
		unittest.TextTestRunner().run(test_suite)
