# -*- coding: utf-8 -*-

import unittest

from pages.settings_page import SettingsPage
from setup.default_setup import default_setup


class DeletionTest(unittest.TestCase):
    NORMAL0_STRING = 'Michael Balitsky'
    NORMAL1_STRING = u'Михаил Балицкий'

    UNICODE_STRING = u'åΩ!2#%_=+±§'  # эмодзи не поддерживаются селениумом, инжектить js – геморройно
    EMPTY_STRING = ''
    SPACE_STRING = ' '

    FORBIDDEN_STRING = '<>:"'

    TOO_LONG_STRING = 'x' * 101

    def setUp(self):
        default_setup(self)

        self.settings = SettingsPage(self.driver)
        self.settings.open()
        general = self.settings.general()
        # Убрать лишние подписи
        self.settings.clear_signatures()

        self.assertFalse(general.second_signature_exists(), "Вторая подпись существует")
        self.assertFalse(general.third_signature_exists(), "Третья подпись существует")

        self.settings.create_signature(self.NORMAL0_STRING, False)
        self.settings.create_signature(self.NORMAL1_STRING, False)

    def tearDown(self):
        self.driver.quit()

    def test_deletion(self):
        """
        Проверка возможности удалить подпись
        """
        general = self.settings.general()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")

        self.settings.delete_second_signature()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertFalse(general.third_signature_exists(), "Третья подпись существует")

        self.assertEqual(general.second_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")

    def test_deletion2(self):
        """
        Проверка возможности удалить подпись
        """
        general = self.settings.general()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")

        self.settings.delete_third_signature()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_default_deletion(self):
        """
        Проверка возможности удалить подпись по умолчанию
        """
        general = self.settings.general()

        self.assertEqual(general.default_signature_id(), 0, "Некорректно выбрана подпись по умолчанию")
        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.set_second_signature_default()
        self.assertEqual(general.default_signature_id(), 1, "Некорректно выбрана подпись по умолчанию")

        self.settings.delete_second_signature()

        self.assertFalse(general.third_signature_exists(), "Третья подпись существует")
        self.assertIn(general.default_signature_id(), [0, 1], "Некорректно выбрана подпись по умолчанию")
        # assert general.default_signature_id() == 0 or general.default_signature_id() == 1

    def test_default_deletion2(self):
        """
        Проверка возможности удалить подпись по умолчанию
        """
        general = self.settings.general()

        self.assertEqual(general.default_signature_id(), 0, "Некорректно выбрана подпись по умолчанию")
        # assert general.default_signature_id() == 0
        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.set_third_signature_default()
        self.assertEqual(general.default_signature_id(), 2, "Некорректно выбрана подпись по умолчанию")
        # assert general.default_signature_id() == 2

        self.settings.delete_third_signature()

        self.assertFalse(general.third_signature_exists(), "Третья подпись существует")
        self.assertIn(general.default_signature_id(), [0, 1], "Некорректно выбрана подпись по умолчанию")
        # assert general.default_signature_id() == 0 or general.default_signature_id() == 1

    def test_cancel_deletion(self):
        """
        Проверка возможности отменить удаление подписи
        """
        general = self.settings.general()
        deletion = self.settings.deletion()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.remove_second_signature()
        deletion.decline_removing_second()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.remove_third_signature()
        deletion.decline_removing_third()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

    def test_cancel_deletion2(self):
        """
        Проверка возможности отменить удаление подписи
        """
        general = self.settings.general()
        deletion = self.settings.deletion()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.remove_second_signature()
        deletion.cancel_removing_second()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.remove_third_signature()
        deletion.cancel_removing_third()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

    def test_cancel_deletion_default(self):
        """
        Проверка возможности отменить удаление подписи по умолчанию
        """
        general = self.settings.general()
        deletion = self.settings.deletion()

        self.assertEqual(general.default_signature_id(), 0, "Некорректно выбрана подпись по умолчанию")
        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")

        general.set_second_signature_default()
        self.assertEqual(general.default_signature_id(), 1, "Некорректно выбрана подпись по умолчанию")

        general.remove_second_signature()
        deletion.decline_removing_second()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")
        self.assertEqual(general.default_signature_id(), 1, "Некорректно выбрана подпись по умолчанию")

        general.set_third_signature_default()
        general.remove_third_signature()
        deletion.decline_removing_third()

        self.assertTrue(general.second_signature_exists(), "Вторая подпись не существует")
        self.assertTrue(general.third_signature_exists(), "Третья подпись не существует")
        self.assertEqual(general.default_signature_id(), 2, "Некорректно выбрана подпись по умолчанию")