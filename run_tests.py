#!/usr/bin/env python2

import sys
import unittest

from tests.Migranov.moving_letters_tests \
    import TestMovingLettersInFolders as RM_Test
from tests.Garifullin.folder_delete_tests import FolderDeleteTests as TG_Test

from tests.Poponkin.draft_create_test import Test as DP_Test

from tests.Parpibaeva.test_unlocked_folder import Test as NP_Test
from tests.Parpibaeva.test_encrypted_folder import Test as NP_Test_encr
from tests.Parpibaeva.test_edit_folder import Test as NP_Test_edit

if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(RM_Test),
        unittest.makeSuite(TG_Test),

        unittest.makeSuite(NP_Test),
        unittest.makeSuite(NP_Test_encr),
        unittest.makeSuite(NP_Test_edit),

        # unittest.makeSuite(DP_Test),
    ))
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(not result.wasSuccessful())
