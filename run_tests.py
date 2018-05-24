# -*- coding: utf-8 -*-

import unittest

from test_mikegus import TestsMikeGus
from tests import Tests
from alltests import TestsBuevichGusev

if __name__ == '__main__':
    #suite = unittest.TestSuite((unittest.makeSuite(Tests)),)
    # suite1 = unittest.TestSuite((unittest.makeSuite(TestsBuevichGusev)),)
    suite2 = unittest.TestSuite((unittest.makeSuite(TestsMikeGus)))
    result = unittest.TextTestRunner().run(suite2)
