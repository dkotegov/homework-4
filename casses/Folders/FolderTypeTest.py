import unittest
from steps.FoldersSteps import FoldersSteps
from casses.Base.BaseTest import BaseTest


class FolderTypeTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderTypeTest, self).setUp()
        self.folderSteps = FoldersSteps(self.driver)
        self.__folderName = "folder"

    def tearDown(self):
        self.folderSteps.delete_folder(self.__folderName)
        super(FolderTypeTest, self).tearDown()

    def test_select_top_folder(self):
        """
        Проверка создания папки на верхнем уровне
        """

        self.folderSteps.add_folder(self.__folderName, 'Папка на верхнем уровне')
        self.assertTrue(self.folderSteps.wait_folder(self.__folderName))

    def test_select_check_incoming_folder(self):
        """
        Проверка создания папки входящие
        """

        self.folderSteps.add_folder(self.__folderName, 'Входящие')
        self.assertTrue(self.folderSteps.wait_folder(self.__folderName))

    def test_select_check_sent_folder(self):
        """
        Проверка создания папки отправленные
        """

        self.folderSteps.add_folder(self.__folderName, 'Отправленные')
        self.assertTrue(self.folderSteps.wait_folder(self.__folderName))

    def test_select_drafts(self):
        """
        Проверка создания папки черновики
        """

        self.folderSteps.add_folder(self.__folderName, 'Черновики')
        self.assertTrue(self.folderSteps.wait_folder(self.__folderName))
