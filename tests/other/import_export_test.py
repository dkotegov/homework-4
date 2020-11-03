# coding=utf-8

import unittest
import os
import time
from pages.features_page import FeaturesPage
from pages.groups_page import GroupsPage
from setup.default_setup import default_setup


class ImportExportTestNames:

    def __init__(self):
        self.group_name = u'Группа 1'
        self.group_name2 = u'Группа 2'
        self.contact_email = u'test@mail.ru'

        self.dir_path = os.environ['DIR_PATH']
        self.apple_path = self.dir_path + '/contacts.vcf'
        self.outlook_path = self.dir_path + '/contacts.csv'
        self.google_path = self.dir_path + '/google.csv'
        self.empty_path = self.dir_path + '/empty.vcf'

        self.downloads_path = os.environ['DOWNLOADS_PATH']

        self.apple_filename = 'contacts.vcf'
        self.outlook_filename = 'contacts.csv'
        self.google_filename = 'google.csv'


class ImportExportTest(unittest.TestCase):

    def wait_downloading(self, filename, timeout=10, poll_frequency=0.5):
        cur_time = 0

        while cur_time < timeout:
            time.sleep(poll_frequency)
            cur_time += poll_frequency

            if filename in os.listdir(self.names.downloads_path):
                return True

        return False

    def setUp(self):
        default_setup(self)

        self.names = ImportExportTestNames()
        self.features = FeaturesPage(self.driver)
        self.groups = GroupsPage(self.driver)

        self.features.open()

        self.groups.delete_all_groups()
        self.groups.delete_all_contacts()

        for filename in [self.names.apple_filename, self.names.outlook_filename, self.names.google_filename]:
            path = self.names.downloads_path + '/' + filename
            if os.path.exists(path):
                os.remove(path)

    def tearDown(self):
        self.features.open()

        self.driver.quit()

    def test_import_contact_from_apple(self):
        """
        Импорт контактов из формата vCard (Apple Address Book)
        """
        self.features.import_contacts(self.names.apple_path, self.names.group_name)

        self.assertTrue(self.groups.group_name_exists(1, self.names.group_name))
        self.assertTrue(self.groups.contacts_exists([self.names.contact_email, ], 1))

    def test_import_contact_from_outlook(self):
        """
        Импорт контактов из формата Outlook CSV
        """
        self.features.import_contacts(self.names.outlook_path, self.names.group_name)

        self.assertTrue(self.groups.group_name_exists(1, self.names.group_name))
        self.assertTrue(self.groups.contacts_exists([self.names.contact_email, ], 1))

    def test_import_contact_from_google(self):
        """
        Импорт контактов из формата Google CSV
        """
        self.features.import_contacts(self.names.google_path, self.names.group_name)

        self.assertTrue(self.groups.group_name_exists(1, self.names.group_name))
        self.assertTrue(self.groups.contacts_exists([self.names.contact_email, ], 1))

    def test_import_contact_from_empty_file(self):
        """
        Импорт контактов из пустого файла
        """
        self.features.import_contacts(self.names.empty_path, self.names.group_name)

        self.assertTrue(self.features.import_error_exists())

    def test_cancel_importing_contacts(self):
        """
        Отмена импорта контактов
        """
        self.features.open_import_popup()
        self.features.close_import_popup()

        self.assertFalse(self.features.import_popup_exists())

    def test_error_on_import_without_uploading_file(self):
        """
        Ошибка при импорте без загрузки файла
        """
        self.features.import_contacts(u'', self.names.group_name)

        self.assertTrue(self.features.import_error_exists())

    def test_error_on_import_to_group_with_duplicate_name(self):
        """
        Ошибка при импорте в группу с уже существующим именем
        """
        self.groups.create_group(self.names.group_name)
        self.features.import_contacts(self.names.apple_path, self.names.group_name)

        self.assertTrue(self.features.input_error_exists())

    def test_error_on_import_without_group_name_input(self):
        """
        Ошибка при импорте без ввода группы
        """
        self.features.import_contacts(self.names.apple_path, u'')

        self.assertTrue(self.features.input_error_exists())

    def test_export_all_contacts(self):
        """
        Экспорт всех контактов
        """
        self.features.export_all_contacts()

        self.assertTrue(self.wait_downloading(self.names.apple_filename))

    def test_export_contacts_from_one_group(self):
        """
        Экспорт контактов из одной группы
        """
        self.groups.create_group(self.names.group_name)

        self.features.export_contacts_from_groups([0, ])

        self.assertTrue(self.wait_downloading(self.names.apple_filename))

    def test_export_contacts_from_several_groups(self):
        """
        Экспорт контактов из нескольких групп
        """
        self.groups.create_group(self.names.group_name)
        self.groups.create_group(self.names.group_name2)

        self.features.export_contacts_from_groups([0, 1])

        self.assertTrue(self.wait_downloading(self.names.apple_filename))

    def test_export_to_apple_format(self):
        """
        Экспорт контактов в формат vCard (Apple Address Book)
        """
        self.groups.create_group(self.names.group_name)

        self.features.export_contacts_from_groups([0, ])

        self.assertTrue(self.wait_downloading(self.names.apple_filename))

    def test_export_to_outlook_format(self):
        """
        Экспорт контактов в формат Outlook CSV
        """
        self.groups.create_group(self.names.group_name)

        self.features.export_contacts_from_groups([0, ], format='outlook')

        self.assertTrue(self.wait_downloading(self.names.outlook_filename))

    def test_export_to_google_format(self):
        """
        Экспорт контактов в формат Google CSV
        """
        self.groups.create_group(self.names.group_name)

        self.features.export_contacts_from_groups([0, ], format='google')

        self.assertTrue(self.wait_downloading(self.names.google_filename))

    def test_cancel_exporting_contacts(self):
        """
        Отмена экспорта контактов
        """
        self.features.open_export_popup()
        self.features.close_export_popup()

        self.assertFalse(self.features.export_popup_exists())
