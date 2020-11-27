import unittest

from steps.FoldersSteps import FoldersSteps
from casses.Base.BaseTest import BaseTest


class CloseFolderFormTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(CloseFolderFormTest, self).setUp()
        self.folderSteps = FoldersSteps(self.driver)
        self.folderSteps.folders_page.open()

    def test_close_add_folder_form(self):
        self.folderSteps.folders_page.add_folder.open()
        self.folderSteps.folders_page.add_folder.close()
        self.assertFalse(self.folderSteps.folders_page.add_folder.form_opened)

    def test_cancel_add_folder_form(self):
        self.folderSteps.folders_page.add_folder.open()
        self.folderSteps.folders_page.add_folder.cancel()
        self.assertFalse(self.folderSteps.folders_page.add_folder.form_opened)
