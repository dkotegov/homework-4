# -*- coding: utf-8 -*-

import unittest

from pages.settings_page import SettingsPage
from setup.default_setup import default_setup


class EditingTest(unittest.TestCase):
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

    def test_valid_editing(self):
        """
        Редактирование подписей с корректным полем "имя отправителя"
        """
        general = self.settings.general()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")

        self.settings.edit_second_signature(self.NORMAL1_STRING, False)
        self.settings.edit_third_signature(self.NORMAL0_STRING, False)

        self.assertEqual(general.second_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.third_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_unicode_editing(self):
        """
        Редактирование подписей с корректным полем "имя отправителя", используя unicode символы
        """
        general = self.settings.general()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        self.settings.edit_second_signature(self.UNICODE_STRING, False)

        self.assertEqual(general.second_signature_name(), self.UNICODE_STRING, "Имена отправителей не совпадают")

    def test_empty_editing(self):
        """
        Редактирование подписей с пустым "имя отправителя"
        """
        general = self.settings.general()
        editing = self.settings.editing()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        general.edit_second_signature()
        editing.clear_second_sender_name()
        # @bug: при нажатии на сохранить с пустым именим отправителя окно закрывается (при создании не закрывается)
        editing.set_second_sender_name(self.SPACE_STRING)
        editing.save_second()

        self.assertTrue(editing.second_empty_warning_appeared(), "Уведомление об ошибке не появилось")

        editing.abort_second()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_forbidden_editing(self):
        """
        Редактирование "имя отправителя", используя запрещенные символы
        """
        general = self.settings.general()
        editing = self.settings.editing()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        general.edit_second_signature()
        editing.clear_second_sender_name()
        editing.set_second_sender_name(self.FORBIDDEN_STRING)
        editing.save_second()

        self.assertTrue(editing.second_forbidden_warning_appeared(), "Уведомление не появилось")

        editing.abort_second()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_too_long_editing(self):
        """
        Редактирование "имя отправителя", используя слишком длинную строку
        """
        general = self.settings.general()
        editing = self.settings.editing()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        general.edit_second_signature()
        editing.clear_second_sender_name()
        # @bug: при нажатии на сохранить с пустым именим отправителя окно закрывается (при создании не закрывается)
        editing.set_second_sender_name(self.TOO_LONG_STRING)
        editing.save_second()

        self.assertTrue(editing.second_too_long_warning_appeared(), "Уведомление не появилось")

        editing.abort_second()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_cancel_editing(self):
        """
        Отмена валидных изменений поля "имя отправителя"
        """
        general = self.settings.general()
        editing = self.settings.editing()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        general.edit_second_signature()
        editing.clear_second_sender_name()

        editing.set_second_sender_name(self.NORMAL1_STRING)
        editing.abort_second()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_cancel_editing2(self):
        """
        Отмена валидных изменений поля "имя отправителя"
        """
        general = self.settings.general()
        editing = self.settings.editing()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        general.edit_second_signature()
        editing.clear_second_sender_name()

        editing.set_second_sender_name(self.NORMAL1_STRING)
        editing.close_second()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

    def test_default_editing(self):
        """
        Изменение подписи по умолчанию
        """
        general = self.settings.general()

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.default_signature_id(), 0, "Некорректно выбрана подпись по умолчанию")

        self.settings.edit_second_signature(self.NORMAL0_STRING, True)
        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.default_signature_id(), 1, "Некорректно выбрана подпись по умолчанию")

        self.settings.edit_third_signature(self.NORMAL1_STRING, True)
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.default_signature_id(), 2, "Некорректно выбрана подпись по умолчанию")

    def test_default_editing2(self):
        """
        Изменение подписи по умолчанию в главном окне
        """
        general = self.settings.general()

        self.assertEqual(general.default_signature_id(), 0, "Некорректно выбрана подпись по умолчанию")

        general.set_second_signature_default()
        self.assertEqual(general.default_signature_id(), 1, "Некорректно выбрана подпись по умолчанию")

        general.set_third_signature_default()
        self.assertEqual(general.default_signature_id(), 2, "Некорректно выбрана подпись по умолчанию")
