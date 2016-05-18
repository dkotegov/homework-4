# -*- coding: utf-8 -*-

import unittest

from tests import DetiTest

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.makeSuite(DetiTest))
    unittest.main()
