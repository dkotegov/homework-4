#!/usr/bin/env python2

import sys
import unittest

from cases.auth import AuthTest
from cases.new_source.new_source_success import NewSourceSuccessTest
from cases.new_source.new_source_failed import NewSourceFailedTest
from cases.tag_list.tag_list_appears import TagListAppearsTest
from cases.tag_list.tag_list_delete import TagListDeleteTest
from cases.transform import TransformTest
from cases.new_proj.new_proj_success import NewProjSuccessTest
from cases.new_proj.new_proj_failed import NewProjFailedTest
from cases.clone_proj.clone_proj_success import CloneProjSuccessTest
from cases.clone_proj.clone_proj_failed import CloneProjFailedTest
from cases.edit_proj.remove_proj import RemoveProjTest
from cases.gen_iframe import GenIframeTest
from cases.edit_proj.edit_proj import EditProjTest
from cases.watch_proj.watch_proj_no_legend import WatchProjTestNoLegend
from cases.watch_proj.watch_proj_with_legend import WatchProjTestWithLegend

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(AuthTest),
        unittest.makeSuite(NewSourceSuccessTest),
        unittest.makeSuite(NewSourceFailedTest),
        unittest.makeSuite(TagListAppearsTest),
        unittest.makeSuite(TagListDeleteTest),
        unittest.makeSuite(TransformTest),
        unittest.makeSuite(NewProjSuccessTest),
        unittest.makeSuite(NewProjFailedTest),
        unittest.makeSuite(CloneProjSuccessTest),
        unittest.makeSuite(CloneProjFailedTest),
        unittest.makeSuite(RemoveProjTest),
        unittest.makeSuite(GenIframeTest),
        unittest.makeSuite(EditProjTest),
        unittest.makeSuite(WatchProjTestNoLegend),
        unittest.makeSuite(WatchProjTestWithLegend),
    ))
    result = unittest.TextTestRunner().run(suite)

    sys.exit(not result.wasSuccessful())
