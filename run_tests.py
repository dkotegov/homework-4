# -*- coding: utf-8 -*-

import unittest

from tests.signatures.creation_test import CreationTest
from tests.signatures.editing_test import EditingTest
from tests.signatures.deletion_test import DeletionTest
from tests.other.groups_test import GroupsTest
import sys


if __name__ == '__main__':
    suite = unittest.TestSuite((
        # unittest.makeSuite(CreationTest),
        # unittest.makeSuite(EditingTest),
        # unittest.makeSuite(DeletionTest),
        unittest.makeSuite(GroupsTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
