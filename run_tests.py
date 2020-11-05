#!/usr/bin/env python2

import sys
import unittest

from cases.auth import AuthTest
from cases.source import SourceFailedTest
from cases.source import SourceSuccessTest
from cases.tag import TagTest
from cases.transform import TransformTest
from cases.new_proj import NewProjTest
from cases.clone import CloneTest
from cases.clone import RemoveProjTest
from cases.iframe import IframeTest
from cases.edit import EditTest
from cases.watch import WatchTestNoLegend
from cases.watch import WatchTestWithLegend

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(SourceSuccessTest),
        unittest.makeSuite(SourceFailedTest),
        unittest.makeSuite(TagTest),
        unittest.makeSuite(TransformTest),
        unittest.makeSuite(NewProjTest),
        unittest.makeSuite(CloneTest),
        unittest.makeSuite(RemoveProjTest),
        unittest.makeSuite(IframeTest),
        unittest.makeSuite(EditTest),
        unittest.makeSuite(WatchTestNoLegend),
        unittest.makeSuite(WatchTestWithLegend),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
