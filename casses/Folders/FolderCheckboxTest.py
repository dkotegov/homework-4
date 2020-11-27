import os
import unittest

from steps.FoldersSteps import FoldersSteps
from casses.Base.BaseTest import BaseTest


class FolderCheckboxTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderCheckboxTest, self).setUp()
        self.folderSteps = FoldersSteps(self.driver)
        self.__folder_name = "folder"
        self.__folder_password_context = {
            'folder_password': 'qwertyuiop',
            'folder_re_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

    def tearDown(self):
        self.folderSteps.delete_folder(self.__folder_name, self.__folder_password_context['folder_password'])
        super(FolderCheckboxTest, self).tearDown()

    def test_pop3_check_box(self):
        self.folderSteps.add_folder(self.__folder_name, '', ['pop3'])
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))

    def test_archive_check_box(self):
        self.folderSteps.add_folder(self.__folder_name, '', ['archive'])
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))

    def test_folder_with_password(self):
        self.folderSteps.add_folder(self.__folder_name, '', ['has password'], self.__folder_password_context)
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))
