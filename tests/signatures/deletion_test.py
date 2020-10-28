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

        assert not general.second_signature_exists()
        assert not general.third_signature_exists()

        self.settings.create_signature(self.NORMAL0_STRING, False)
        self.settings.create_signature(self.NORMAL1_STRING, False)

    def tearDown(self):
        self.driver.quit()

    def test_deletion(self):
        """
        Проверка возможности удалить подпись
        """
        general = self.settings.general()

        assert general.second_signature_exists()
        assert general.third_signature_exists()

        assert general.second_signature_name() == self.NORMAL0_STRING
        assert general.third_signature_name() == self.NORMAL1_STRING

        self.settings.delete_second_signature()

        assert general.second_signature_exists()
        assert not general.third_signature_exists()

        assert general.second_signature_name() == self.NORMAL1_STRING

    def test_deletion2(self):
        """
        Проверка возможности удалить подпись
        """
        general = self.settings.general()

        assert general.second_signature_exists()
        assert general.third_signature_exists()

        assert general.second_signature_name() == self.NORMAL0_STRING
        assert general.third_signature_name() == self.NORMAL1_STRING

        self.settings.delete_third_signature()

        assert general.second_signature_name() == self.NORMAL0_STRING
    def test_default_deletion(self):
        """
        Проверка возможности удалить подпись по умолчанию
        """
        general = self.settings.general()

        assert general.default_signature_id() == 0
        assert general.second_signature_exists()
        assert general.third_signature_exists()

        general.set_second_signature_default()
        assert general.default_signature_id() == 1

        self.settings.delete_second_signature()

        assert not general.third_signature_exists()
        assert general.default_signature_id() == 0 or general.default_signature_id() == 1

    def test_default_deletion2(self):
        """
        Проверка возможности удалить подпись по умолчанию
        """
        general = self.settings.general()

        assert general.default_signature_id() == 0
        assert general.second_signature_exists()
        assert general.third_signature_exists()

        general.set_third_signature_default()
        assert general.default_signature_id() == 2

        self.settings.delete_third_signature()

        assert not general.third_signature_exists()
        assert general.default_signature_id() == 0 or general.default_signature_id() == 1

    def test_cancel_deletion(self):
        """
        Проверка возможности отменить удаление подписи
        """
        general = self.settings.general()
        deletion = self.settings.deletion()

        assert general.second_signature_exists()
        assert general.third_signature_exists()

        general.remove_second_signature()
        deletion.decline_removing_second()

        assert general.second_signature_exists()
        assert general.third_signature_exists()

        general.remove_third_signature()
        deletion.decline_removing_third()

        assert general.second_signature_exists()
        assert general.third_signature_exists()

    def test_cancel_deletion_default(self):
        """
        Проверка возможности отменить удаление подписи по умолчанию
        """
        general = self.settings.general()
        deletion = self.settings.deletion()

        assert general.default_signature_id() == 0
        assert general.second_signature_exists()
        assert general.third_signature_exists()

        general.set_second_signature_default()
        assert general.default_signature_id() == 1

        general.remove_second_signature()
        deletion.decline_removing_second()

        assert general.second_signature_exists()
        assert general.third_signature_exists()
        assert general.default_signature_id() == 1

        general.set_third_signature_default()
        general.remove_third_signature()
        deletion.decline_removing_third()

        assert general.second_signature_exists()
        assert general.third_signature_exists()
        assert general.default_signature_id() == 2
