# -*- coding: utf-8 -*-

import unittest

from pages.settings_page import SettingsPage
from setup.default_setup import default_setup


class CreationTest(unittest.TestCase):
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

    def tearDown(self):
        self.driver.quit()


    def test_valid_creation(self):
        """
        Создание подписей с корректным полем "имя отправителя"
        """
        general = self.settings.general()

        self.settings.create_signature(self.NORMAL0_STRING, False)
        self.settings.create_signature(self.NORMAL1_STRING, False)

        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")

    def test_unicode_creation(self):
        """
        Создание подписей с корректным полем "имя отправителя" (с юникод символами)
        """
        general = self.settings.general()

        self.settings.create_signature(self.UNICODE_STRING, False)

        self.assertEqual(general.second_signature_name(), self.UNICODE_STRING, "Имена отправителей не совпадают")

    def test_empty_creation(self):
        """
        Ошибка при создании пустого поля "имя отправителя"
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.EMPTY_STRING)
        creation.create()
        self.assertTrue(creation.empty_warning_appeared(), "Уведомление об ошибке не появилось")

        assert creation.is_open()

        creation.abort()

        self.assertFalse(general.second_signature_exists(), "Существует лишняя подпись")
        self.assertFalse(general.third_signature_exists(), "Существует лишняя подпись")

    def test_space_creation(self):
        """
        Ошибка при создании поля "имя отправителя", содержащего только пробелы
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.SPACE_STRING)
        creation.create()

        self.assertTrue(creation.empty_warning_appeared(), "Уведомление об ошибке не появилось")
        self.assertTrue(creation.is_open(), "Не открыто окно создания")

        creation.abort()

        self.assertFalse(general.second_signature_exists(), "Существует лишняя подпись")
        self.assertFalse(general.third_signature_exists(), "Существует лишняя подпись")

    def test_forbidden_creation(self):
        """
        Ошибка при создании пустого поля "имя отправителя", содержащего запрещенные символы
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.FORBIDDEN_STRING)
        creation.create()
        self.assertTrue(creation.forbidden_warning_appeared(), "Уведомление об ошибке не появилось")
        self.assertTrue(creation.is_open(), "Не открыто окно создания")

        creation.abort()

        self.assertFalse(general.second_signature_exists(), "Существует лишняя подпись")
        self.assertFalse(general.third_signature_exists(), "Существует лишняя подпись")

    def test_abort_creation(self):
        """
        Отмена создания валидной подписи
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.NORMAL0_STRING)
        creation.abort()

        self.assertFalse(general.second_signature_exists(), "Существует лишняя подпись")
        self.assertFalse(general.third_signature_exists(), "Существует лишняя подпись")

    def test_cancel_creation(self):
        """
        Отмена создания валидной подписи
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.NORMAL0_STRING)
        creation.close()

        self.assertFalse(general.second_signature_exists(), "Существует лишняя подпись")
        self.assertFalse(general.third_signature_exists(), "Существует лишняя подпись")

    def test_too_long_creation(self):
        """
        Ошибка при создании пустого поля "имя отправителя", содержащего слишком много символов
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.TOO_LONG_STRING)
        creation.create()

        self.assertTrue(creation.too_long_warning_appeared(), "Уведомление об ошибке не появилось")
        self.assertTrue(creation.is_open(), "Не открыто окно создания")

        creation.abort()

        self.assertFalse(general.second_signature_exists(), "Существует лишняя подпись")
        self.assertFalse(general.third_signature_exists(), "Существует лишняя подпись")

    def test_default_creation(self):
        """
        Создание подписи по умолчанию
        """
        general = self.settings.general()

        self.assertEqual(general.default_signature_id(), 0, "Некорректно выбрана подпись по умолчанию")

        self.settings.create_signature(self.NORMAL0_STRING, True)

        self.assertEqual(general.default_signature_id(), 1, "Некорректно выбрана подпись по умолчанию")
        self.assertEqual(general.second_signature_name(), self.NORMAL0_STRING, "Имена отправителей не совпадают")

        self.settings.create_signature(self.NORMAL1_STRING, True)

        self.assertEqual(general.default_signature_id(), 2, "Некорректно выбрана подпись по умолчанию")
        self.assertEqual(general.third_signature_name(), self.NORMAL1_STRING, "Имена отправителей не совпадают")

    def test_no_button(self):
        """
        Отсутствие кнопки создания при наличии трех подписей
        """
        general = self.settings.general()

        self.assertTrue(general.can_create_signature(), "Невозможно создать подпись")

        self.settings.create_signature(self.NORMAL0_STRING, False)
        self.assertTrue(general.can_create_signature(), "Невозможно создать подпись")

        self.settings.create_signature(self.NORMAL1_STRING, False)
        self.assertFalse(general.can_create_signature(), "Возможно создать подпись")