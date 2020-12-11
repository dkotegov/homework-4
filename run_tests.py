# -*- coding: utf-8 -*-
import sys
import unittest

from casses.folders.FolderCheckboxTest import FolderCheckboxTest
from casses.folders.FolderNameTest import FolderNameTest
from casses.folders.FolderTypeTest import FolderTypeTest
from casses.folders.InvalidFolderPasswordFormTest import InvalidFolderPasswordFormTest
from casses.folders.CloseFolderFormTest import CloseFolderFormTest

from casses.MainPageCase import MainPageTests
from casses.PersonalDataCase import PersonalDataTests

from casses.ContactsCase import ContactsTest
from casses.FoldersTestSecond import FoldersTestSecond
from casses.PasswordCase import PasswordTest
from casses.SecurityCase import SecurityTest

if __name__ == "__main__":
    suites = unittest.TestSuite(
        (
            unittest.makeSuite(PersonalDataTests),
            unittest.makeSuite(MainPageTests),
            unittest.makeSuite(FoldersTestSecond),
            unittest.makeSuite(PasswordTest),
            unittest.makeSuite(ContactsTest),
            unittest.makeSuite(SecurityTest),

            unittest.makeSuite(FolderCheckboxTest),
            unittest.makeSuite(FolderNameTest),
            unittest.makeSuite(FolderTypeTest),
            unittest.makeSuite(InvalidFolderPasswordFormTest),
            unittest.makeSuite(CloseFolderFormTest),
        )
    )
    result = unittest.TextTestRunner().run(suites)
    sys.exit(not result.wasSuccessful())
