# -*- coding: utf-8 -*-
import sys
import unittest

from casses.ContactsCase import ContactsTest
from casses.MainPageCase import MainPageTests
from casses.PasswordCase import PasswordTest
from casses.PersonalDataCase import PersonalDataTests
from casses.SecurityCase import SecurityTest
from casses.folders.CloseFolderFormTest import CloseFolderFormTest
from casses.folders.FolderCheckboxTest import FolderCheckboxTest
from casses.folders.FolderNameTest import FolderNameTest
from casses.folders.FolderTypeTest import FolderTypeTest
from casses.folders.InvalidFolderPasswordFormTest import InvalidFolderPasswordFormTest
from casses.folders.UpdateFolderFormTest import UpdateFolderFormTest
from casses.folders.UpdateFolderTest import UpdateFolderTest

if __name__ == "__main__":
    suites = unittest.TestSuite(
        (
            unittest.makeSuite(MainPageTests),
            unittest.makeSuite(PersonalDataTests),
            unittest.makeSuite(PasswordTest),
            unittest.makeSuite(ContactsTest),
            unittest.makeSuite(SecurityTest),

            unittest.makeSuite(FolderCheckboxTest),
            unittest.makeSuite(FolderNameTest),
            unittest.makeSuite(FolderTypeTest),
            unittest.makeSuite(InvalidFolderPasswordFormTest),
            unittest.makeSuite(CloseFolderFormTest),
            unittest.makeSuite(UpdateFolderFormTest),
            unittest.makeSuite(UpdateFolderTest),
        )
    )
    result = unittest.TextTestRunner().run(suites)
    sys.exit(not result.wasSuccessful())
