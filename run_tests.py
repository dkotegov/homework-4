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


def create_suite(test_cases) -> unittest.TestSuite:
    loader = unittest.TestLoader()
    new_suite = unittest.TestSuite()

    for test_case in test_cases:
        new_suite.addTests(loader.loadTestsFromTestCase(test_case))

    return new_suite


if __name__ == "__main__":
    tests = [
        MainPageTests,
        PersonalDataTests,

        PasswordTest,
        ContactsTest,
        SecurityTest,
        FolderCheckboxTest,
        FolderNameTest,
        FolderTypeTest,

        InvalidFolderPasswordFormTest,
        CloseFolderFormTest,
        UpdateFolderFormTest,
        UpdateFolderTest,
    ]

    suite = create_suite(tests)
    result = unittest.TextTestRunner(verbosity=4).run(suite)
    sys.exit(not result.wasSuccessful())
