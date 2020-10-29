#!/usr/bin/env python2

import sys
import unittest

from cases.auth import AuthTest
from cases.source import SourceTest
from cases.tag import TagTest
from cases.transform import TransformTest
from cases.new_proj import NewProjTest
from cases.clone import CloneTest
from cases.iframe import IframeTest

if __name__ == '__main__':
    # suite = unittest.TestSuite((
    #     unittest.makeSuite(AuthTest),
    # ))
    # result = unittest.TextTestRunner().run(suite)

    suite = unittest.TestSuite((
        unittest.makeSuite(TransformTest),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
