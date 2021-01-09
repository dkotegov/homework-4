import os
import unittest

from steps.FoldersSteps import FoldersSteps
from casses.base.BaseTest import BaseTest


class FolderCheckboxTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderCheckboxTest, self).setUp()
        self.folderSteps = FoldersSteps(self.driver)
        self.__folderName = "folder"
        self.__folderPasswordContext = {
            'folder_password': 'qwertyuiop',
            'folder_re_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

    def tearDown(self):
        try:
            self.folderSteps.delete_folder(self.__folderName, self.__folderPasswordContext['folder_password'])
        finally:
            super(FolderCheckboxTest, self).tearDown()

    def test_pop3_check_box(self):
        """ Проверка создания папки pop3 """

        self.folderSteps.add_folder(self.__folderName, '', ['pop3'])
        self.assertTrue(self.folderSteps.wait_folder(self.__folderName))

    # def test_folder_with_password(self):
    #     """ Проверка создания папки с паролем """
    #
    #     self.folderSteps.add_folder(self.__folderName, '', ['has password'], self.__folderPasswordContext)
    #     self.assertTrue(self.folderSteps.wait_folder(self.__folderName))
    #
    # def test_archive_check_box(self):
    #     """ Проверка создания архивированной папки """
    #
    #     self.folderSteps.add_folder(self.__folderName, '', ['archive'])
    #     self.assertTrue(self.folderSteps.wait_folder(self.__folderName))
