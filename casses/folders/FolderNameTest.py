import unittest

from steps.FoldersSteps import FoldersSteps
from casses.base.BaseTest import BaseTest


class FolderNameTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(FolderNameTest, self).setUp()
        self.__folder_steps = FoldersSteps(self.driver)

    def test_empty_folder_name(self):
        """ Проверка создания папки с пустым названием """

        self.__folder_steps.add_folder('')
        self.assertTrue(self.__folder_steps.get_form_errors()['emptyFolderName'])

    def test_spaces_folder_name(self):
        """ Проверка создания папки с названием из пробелов """

        self.__folder_steps.add_folder('        ')
        self.assertTrue(self.__folder_steps.get_form_errors()['emptyFolderName'])
