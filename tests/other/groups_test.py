# coding=utf-8

import unittest
from pages.groups_page import ContactsPage
from setup.default_setup import default_setup


class GroupsTestNames:

    def __init__(self):
        self.group_name = u'Группа 1'
        self.group_name2 = u'Группа 2'

        self.contact_email = u'test@mail.ru'
        self.contact_email2 = u'test2@mail.ru'


class GroupsTest(unittest.TestCase):

    def setUp(self):
        default_setup(self)

        self.names = GroupsTestNames()
        self.page = ContactsPage(self.driver)

        self.page.open()

        self.page.delete_all_groups()
        self.page.delete_all_contacts()

    def tearDown(self):
        self.page.open()

        self.driver.quit()

    def test_create_group_from_main_page(self):
        """
        Создание группы из главной страницы
        """
        self.page.create_group(self.names.group_name)

        self.assertTrue(self.page.group_name_exists(1, self.names.group_name))

    def test_create_group_from_contact_page(self):
        """
        Создание группы из страницы котакта
        """
        self.page.create_contact(self.names.contact_email)
        self.page.create_group_from_contact_page(self.names.contact_email, self.names.group_name)

        self.assertTrue(self.page.group_name_exists(1, self.names.group_name))

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

        self.assertTrue(self.page.group_name_exists(1, self.names.group_name2))

    def test_save_changes_without_changing_name(self):
        """
        Сохранение изменений без смены названия
        """
        self.page.create_group(self.names.group_name)
        self.page.change_group_name(1, self.names.group_name)

        self.assertTrue(self.page.group_name_exists(1, self.names.group_name))

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

        self.assertFalse(self.page.group_exists(1))

    def test_delete_not_empty_group(self):
        """
        Удаление непустой группы
        """
        self.page.create_group(self.names.group_name)

        self.page.create_contact(self.names.contact_email)
        self.page.add_contact_to_groups(self.names.contact_email, [1, ])

        self.page.delete_group(1)

        self.assertFalse(self.page.group_exists(1))

    def test_add_contact_to_group(self):
        """
        Добавление контакта в группу
        """
        self.page.create_group(self.names.group_name)

        self.page.create_contact(self.names.contact_email)
        self.page.add_contact_to_groups(self.names.contact_email, [1, ])

        self.assertTrue(self.page.contacts_exists([self.names.contact_email, ], 1))

    def test_add_contact_to_several_groups(self):
        """
        Добавление контакта в несколько групп
        """
        self.page.create_group(self.names.group_name)
        self.page.create_group(self.names.group_name2)

        self.page.create_contact(self.names.contact_email)
        self.page.add_contact_to_groups(self.names.contact_email, [1, 2])

        self.assertTrue(self.page.contacts_exists([self.names.contact_email, ], 1))
        self.assertTrue(self.page.contacts_exists([self.names.contact_email, ], 2))

    def test_add_selected_contacts_to_group(self):
        """
        Добавление выделенных контактов в группу
        """
        self.page.create_group(self.names.group_name)

        self.page.create_contact(self.names.contact_email)
        self.page.create_contact(self.names.contact_email2)

        self.page.add_all_contacts_to_groups([1, ])

        self.assertTrue(self.page.contacts_exists(
          [self.names.contact_email, self.names.contact_email2], 1))

    def test_add_selected_contact_to_several_groups(self):
        """
        Добавление выделенных контактов в несколько групп
        """
        self.page.create_group(self.names.group_name)
        self.page.create_group(self.names.group_name2)

        self.page.create_contact(self.names.contact_email)
        self.page.create_contact(self.names.contact_email2)

        self.page.add_all_contacts_to_groups([1, 2])

        self.assertTrue(self.page.contacts_exists(
            [self.names.contact_email, self.names.contact_email2], 1))
        self.assertTrue(self.page.contacts_exists(
            [self.names.contact_email, self.names.contact_email2], 2))

    def test_add_to_my_contacts_after_creating(self):
        """
        Добавление в группу “Мои контакты” при создании контакта
        """
        self.page.create_contact(self.names.contact_email)

        self.assertTrue(self.page.contacts_exists([self.names.contact_email, ], "personal"))

    def test_delete_contact_from_group(self):
        """
        Удаление контакта из группы
        """
        self.page.create_group(self.names.group_name)
        self.page.create_contact(self.names.contact_email)

        self.page.add_contact_to_groups(self.names.contact_email, [1, ])
        self.page.add_contact_to_groups(self.names.contact_email, [1, ])  # second call deletes from group

        self.assertFalse(self.page.contacts_exists([self.names.contact_email, ], 1))

    def test_delete_contact_from_several_groups(self):
        """
        Удаление контакта из нескольких групп
        """
        self.page.create_group(self.names.group_name)
        self.page.create_group(self.names.group_name2)
        self.page.create_contact(self.names.contact_email)

        self.page.add_contact_to_groups(self.names.contact_email, [1, 2])
        self.page.add_contact_to_groups(self.names.contact_email, [1, 2])  # second call deletes from groups

        self.assertFalse(self.page.contacts_exists([self.names.contact_email, ], 1))
        self.assertFalse(self.page.contacts_exists([self.names.contact_email, ], 2))

    def test_delete_selected_contacts_from_group(self):
        """
        Удаление выделенных контактов из группы
        """
        self.page.create_group(self.names.group_name)

        self.page.create_contact(self.names.contact_email)
        self.page.create_contact(self.names.contact_email2)

        self.page.add_all_contacts_to_groups([1, ])
        self.page.add_all_contacts_to_groups([1, ])  # second call deletes from groups

        self.assertFalse(self.page.contacts_exists(
            [self.names.contact_email, self.names.contact_email2], 1))

    def test_delete_selected_contacts_from_several_groups(self):
        """
        Удаление выделенных контактов из нескольких групп
        """
        self.page.create_group(self.names.group_name)
        self.page.create_group(self.names.group_name2)

        self.page.create_contact(self.names.contact_email)
        self.page.create_contact(self.names.contact_email2)

        self.page.add_all_contacts_to_groups([1, 2])
        self.page.add_all_contacts_to_groups([1, 2])  # second call deletes from groups

        self.assertFalse(self.page.contacts_exists(
            [self.names.contact_email, self.names.contact_email2], 1))
        self.assertFalse(self.page.contacts_exists(
            [self.names.contact_email, self.names.contact_email2], 2))
