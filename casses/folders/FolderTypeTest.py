import unittest
from steps.FoldersSteps import FoldersSteps
from casses.base.BaseTest import BaseTest


class FolderTypeTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderTypeTest, self).setUp()
        self.__folder_steps = FoldersSteps(self.driver)
        self.__folder_name = "folder"

    def tearDown(self):
        self.__folder_steps.delete_folder(self.__folder_name)
        self.__folder_steps.wait_delete_folder(self.__folder_name)
        super(FolderTypeTest, self).tearDown()

    def test_select_top_folder(self):
        """
        Проверка создания папки на верхнем уровне
        """

        self.__folder_steps.add_folder(self.__folder_name, 'Папка на верхнем уровне')
        self.assertTrue(self.__folder_steps.wait_folder(self.__folder_name))

    def test_select_check_incoming_folder(self):
        """
        Проверка создания папки входящие
        """

        self.__folder_steps.add_folder(self.__folder_name, 'Входящие')
        self.assertTrue(self.__folder_steps.wait_folder(self.__folder_name))

    def test_select_check_sent_folder(self):
        """
        Проверка создания папки отправленные
        """

        self.__folder_steps.add_folder(self.__folder_name, 'Отправленные')
        self.assertTrue(self.__folder_steps.wait_folder(self.__folder_name))

    def test_select_drafts(self):
        """
        Проверка создания папки черновики
        """

        self.__folder_steps.add_folder(self.__folder_name, 'Черновики')
        self.assertTrue(self.__folder_steps.wait_folder(self.__folder_name))
