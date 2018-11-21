#!/usr/bin/env python2

import sys
import unittest

from tests.QA_72_Migranov.several_letters import TestMovingLettersInFolders as RM_Test_1
from tests.QA_72_Migranov.by_right_mouse_button_click import TestMovingLettersInFolders as RM_Test_2
from tests.QA_72_Migranov.from_view_to_archieve import TestMovingLettersInFolders as RM_Test_3
from tests.QA_72_Migranov.from_view_to_new_folder import TestMovingLettersInFolders as RM_Test_4
from tests.QA_72_Migranov.to_the_same_folder import TestMovingLettersInFolders as RM_Test_5

from tests.Garifullin.unlocked_dirs_delete import UnlockedFolderDeleteTest as TG_Test_1
from tests.Garifullin.subdirs_delete import SubFolderDeleteTest as TG_Test_2
from tests.Garifullin.locked_folder_delete import LockedFolderDeleteTest as TG_Test_3
from tests.Garifullin.folder_with_subdir_delete import FolderWithSubdirDeleteTest as TG_Test_4

from tests.Poponkin.draft_create_test import Test as DP_Test

from tests.Parpibaeva.test_unlocked_folder import Test as NP_Test
from tests.Parpibaeva.test_encrypted_folder import Test as NP_Test_encr
from tests.Parpibaeva.test_edit_folder import Test as NP_Test_edit

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(RM_Test_1),
        unittest.makeSuite(RM_Test_2),
        unittest.makeSuite(RM_Test_3),
        unittest.makeSuite(RM_Test_4),
        unittest.makeSuite(RM_Test_5),

        unittest.makeSuite(TG_Test_1),
        unittest.makeSuite(TG_Test_2),
        unittest.makeSuite(TG_Test_3),
        unittest.makeSuite(TG_Test_4),

        unittest.makeSuite(NP_Test),
        unittest.makeSuite(NP_Test_encr),
        unittest.makeSuite(NP_Test_edit),

        unittest.makeSuite(DP_Test),
    ))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())