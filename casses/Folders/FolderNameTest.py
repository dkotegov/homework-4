import unittest

from steps.FoldersSteps import FoldersSteps
from casses.Base.BaseTest import BaseTest


class FolderNameTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderNameTest, self).setUp()
        self.folderSteps = FoldersSteps(self.driver)

    def test_empty_folder_name(self):
        self.folderSteps.add_folder('')
        self.assertTrue(self.folderSteps.get_form_errors()['emptyFolderName'])

    def test_spaces_folder_name(self):
        self.folderSteps.add_folder('     ')
        self.assertTrue(self.folderSteps.get_form_errors()['emptyFolderName'])
