# coding=utf-8

import unittest
from time import sleep

from pages.contacts_page import ContactsPage
from setup.default_setup import default_setup


class GroupsTestNames:

    def __init__(self):
        self.group_name = u'Группа 1'
        self.group_name2 = u'Группа 2'


class GroupsTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.names = GroupsTestNames()
        self.page = ContactsPage(self.driver)

        self.page.open()

    def tearDown(self):
        self.page.open()

        self.page.delete_all_groups()

        self.driver.quit()

    def test_create_group_from_main_page(self):
        """
        Создание группы из главной страницы
        """
        self.page.create_group(self.names.group_name)

        self.assertTrue(self.page.check_group_name(1, self.names.group_name))

    # def test_create_group_from_contact_page(self):
    #     """
    #     Создание группы из страницы котакта
    #     """

    def test_error_on_empty_group_name(self):
        """
        Ошибка при вводе пустого названия группы
        """
        self.page.create_group(u'')

        self.assertTrue(self.page.error_exists())

    def test_error_on_duplicate_name(self):
        """
        Ошибка при создании группы с уже существующим именем
        """
        self.page.create_group(self.names.group_name)
        self.page.create_group(self.names.group_name)

        self.assertTrue(self.page.error_exists())

    def test_edit_group_name(self):
        """
        Изменение названия группы
        """
        self.page.create_group(self.names.group_name)
        self.page.change_group_name(1, self.names.group_name2)

        self.assertTrue(self.page.check_group_name(1, self.names.group_name2))

    def test_save_changes_without_changing_name(self):
        """
        Сохранение изменений без смены названия
        """
        self.page.create_group(self.names.group_name)
        self.page.change_group_name(1, self.names.group_name)

        self.assertTrue(self.page.check_group_name(1, self.names.group_name))

    def test_error_on_change_name_to_empty(self):
        """
        Ошибка при изменении названия группы на пустое
        """
        self.page.create_group(self.names.group_name)
        self.page.change_group_name(1, '')

        self.assertTrue(self.page.error_exists())

    def test_error_on_change_to_duplicate_name(self):
        """
        Ошибка при изменении названия группы на уже существующее
        """
        self.page.create_group(self.names.group_name)
        self.page.create_group(self.names.group_name2)
        self.page.change_group_name(2, self.names.group_name)

        self.assertTrue(self.page.error_exists())

    def test_delete_empty_group(self):
        """
        Удаление пустой группы
        """
        self.page.create_group(self.names.group_name)
        self.page.delete_group(1)

        self.assertFalse(self.page.check_group(1))
