import os
import unittest

from steps.FoldersSteps import FoldersSteps
from casses.base.BaseTest import BaseTest


class InvalidFolderPasswordFormTest(BaseTest, unittest.TestCase):

    def setUp(self):
        super(InvalidFolderPasswordFormTest, self).setUp()

        self.folderSteps = FoldersSteps(self.driver)
        self.__folderName = 'folder'
        self.__folderPasswordContext = {
            'folder_password': 'qwertyuiop',
            'folder_re_password': 'qwertyuiop',
            'question': 'why?',
            'question_answer': 'because',
            'current_password': os.environ['PASSWORD']
        }

    def test_short_password(self):
        """ Проверка создания папки с паролем < 3 символов """

        context = self.__folderPasswordContext.copy()
        context['folder_password'] = 'ps'
        context['folder_re_password'] = 'ps'
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_long_password(self):
        """ Проверка создания папки с паролем > 32 символов """

        context = self.__folderPasswordContext.copy()
        context['folder_password'] = 'ps' * 32
        context['folder_re_password'] = 'ps' * 32
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_password_started_with_space(self):
        """ Проверка создания папки с паролем, начинающимся с пробела """

        context = self.__folderPasswordContext.copy()
        context['folder_password'] = ' ' + context['folder_password']
        context['folder_re_password'] = ' ' + context['folder_password']
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_password_ended_with_space(self):
        """ Проверка создания папки с паролем, заканчивающимся на пробел """

        context = self.__folderPasswordContext.copy()
        context['folder_password'] = context['folder_password'] + ' '
        context['folder_re_password'] = context['folder_password'] + ' '
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_invalid_password(self):
        """ Проверка создания папки с паролем, состоящим из запрещённых символов """

        context = self.__folderPasswordContext.copy()
        context['folder_password'] = '@#$%^&*()askdl'
        context['folder_re_password'] = context['folder_password']
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidPassword'])

    def test_invalid_re_password(self):
        """ Проверка создания папки с неправильным повторным паролем """

        context = self.__folderPasswordContext.copy()
        context['folder_re_password'] = context['folder_password'] + 'text'
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidRePassword'])

    def test_missing_secret_question(self):
        """ Проверка создания папки с паролем, без указания секретного вопроса """

        context = self.__folderPasswordContext.copy()
        context['question'] = ''
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidSecretQuestion'])

    def test_missing_secret_question_answer(self):
        """ Проверка создания папки с паролем, без указания ответа на секретный вопрос """

        context = self.__folderPasswordContext.copy()
        context['question_answer'] = ''
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidSecretQuestionAnswer'])

    def test_invalid_current_password(self):
        """ Проверка создания папки с паролем, с указанием некоректного текущего пароля """

        context = self.__folderPasswordContext.copy()
        context['current_password'] = ''
        self.folderSteps.add_folder(self.__folderName, '', ['has password'], context)
        self.assertTrue(self.folderSteps.get_form_errors()['passwordForm']['invalidUserPassword'])
