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

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

    def tearDown(self):
        self.driver.quit()

    def test_valid_creation(self):
        """
        Создание подписей с корректным полем "имя отправителя"
        """
        general = self.settings.general()

        self.settings.create_signature(self.NORMAL0_STRING, False)
        self.settings.create_signature(self.NORMAL1_STRING, False)

        assert general.second_signature_name() == self.NORMAL0_STRING
        assert general.third_signature_name() == self.NORMAL1_STRING

    def test_unicode_creation(self):
        """
        Создание подписей с корректным полем "имя отправителя" (с юникод символами)
        """
        general = self.settings.general()

        self.settings.create_signature(self.UNICODE_STRING, False)

        assert general.second_signature_name() == self.UNICODE_STRING

    def test_empty_creation(self):
        """
        Ошибка при создании пустого поля "имя отправителя"
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.EMPTY_STRING)
        creation.create()
        assert creation.empty_warning_appeared()

        assert creation.is_open()

        creation.abort()

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

    def test_space_creation(self):
        """
        Ошибка при создании поля "имя отправителя", содержащего только пробелы
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.SPACE_STRING)
        creation.create()

        assert creation.empty_warning_appeared()
        assert creation.is_open()

        creation.abort()

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

    def test_forbidden_creation(self):
        """
        Ошибка при создании пустого поля "имя отправителя", содержащего запрещенные символы
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.FORBIDDEN_STRING)
        creation.create()
        assert creation.forbidden_warning_appeared()

        assert creation.is_open()

        creation.abort()

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

    def test_abort_creation(self):
        """
        Отмена создания валидной подписи
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.NORMAL0_STRING)
        creation.abort()

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

    def test_too_long_creation(self):
        """
        Ошибка при создании пустого поля "имя отправителя", содержащего слишком много символов
        """
        general = self.settings.general()
        creation = self.settings.creation()

        general.create_signature()
        creation.set_sender_name(self.TOO_LONG_STRING)
        creation.create()

        assert creation.too_long_warning_appeared()
        assert creation.is_open()

        creation.abort()

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

    def test_default_creation(self):
        """
        Создание подписи по умолчанию
        """
        general = self.settings.general()

        assert general.default_signature_id() == 0

        self.settings.create_signature(self.NORMAL0_STRING, True)

        assert general.default_signature_id() == 1
        assert general.second_signature_name() == self.NORMAL0_STRING

        self.settings.create_signature(self.NORMAL1_STRING, True)

        assert general.default_signature_id() == 2
        assert general.third_signature_name() == self.NORMAL1_STRING

    def test_no_button(self):
        """
        Отсутствие кнопки создания при наличии трех подписей
        """
        general = self.settings.general()

        assert general.can_create_signature()

        self.settings.create_signature(self.NORMAL0_STRING, False)
        assert general.can_create_signature()

        self.settings.create_signature(self.NORMAL1_STRING, False)
        assert not general.can_create_signature()
