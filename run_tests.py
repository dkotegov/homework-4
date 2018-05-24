# -*- coding: utf-8 -*-

import unittest

from test_mikegus import TestsMikeGus
from tests import Tests



if __name__ == '__main__':
    #suite = unittest.TestSuite((unittest.makeSuite(Tests)),)
    suite2 = unittest.TestSuite((unittest.makeSuite(TestsMikeGus)))
    result = unittest.TextTestRunner().run(suite2)
