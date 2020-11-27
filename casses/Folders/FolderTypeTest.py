import unittest
from steps.FoldersSteps import FoldersSteps
from casses.Base.BaseTest import BaseTest


class FolderTypeTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderTypeTest, self).setUp()
        self.folderSteps = FoldersSteps(self.driver)
        self.__folder_name = "folder"

    def tearDown(self):
        self.folderSteps.delete_folder(self.__folder_name)
        super(FolderTypeTest, self).tearDown()

    def test_select_top_folder(self):
        self.folderSteps.add_folder(self.__folder_name, 'Папка на верхнем уровне')
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))

    def test_select_check_incoming_folder(self):
        self.folderSteps.add_folder(self.__folder_name, 'Входящие')
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))

    def test_select_check_sent_folder(self):
        self.folderSteps.add_folder(self.__folder_name, 'Отправленные')
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))

    def test_select_drafts(self):
        self.folderSteps.add_folder(self.__folder_name, 'Черновики')
        self.assertTrue(self.folderSteps.wait_folder(self.__folder_name))
