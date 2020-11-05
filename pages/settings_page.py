# -*- coding: utf-8 -*-
from selenium.common.exceptions import TimeoutException

from base import Page
from components.settings_general import SettingsGeneralForm
from components.signature_creation import SignatureCreationForm
from components.signature_deletion import SignatureDeletionForm
from components.signature_editing import SignatureEditingForm
from components.signature_deep_editing import SignatureDeepEditingForm


class SettingsPage(Page):
    BASE_URL = 'https://e.mail.ru/'
    PATH = 'settings/general'

    def general(self):
        return SettingsGeneralForm(self.driver)

    def deletion(self):
        return SignatureDeletionForm(self.driver)

    def creation(self):
        return SignatureCreationForm(self.driver)

    def editing(self):
        return SignatureEditingForm(self.driver)

    def deep_editing(self):
        return SignatureDeepEditingForm(self.driver)


    def delete_first_signature(self):
        """
        Шорткат для удаления первой подписи
        :return: None
        """
        general = self.general()
        deletion = self.deletion()

        general.remove_first_signature()
        deletion.approve_removing_first()

    def delete_second_signature(self):
        """
        Шорткат для удаления второй подписи
        :return: None
        """
        general = self.general()
        deletion = self.deletion()

        general.remove_second_signature()
        deletion.approve_removing_second()

    def delete_third_signature(self):
        """
        Шорткат для удаления третьей подписи
        :return: None
        """
        general = self.general()
        deletion = self.deletion()

        general.remove_third_signature()
        deletion.approve_removing_third()

    def clear_signatures(self):
        """
        Шорткат для удаления второй и третьей подписий, если имеются
        :return: None
        """
        general = self.general()
        try:
            self.delete_second_signature()
            self.delete_second_signature()
        except TimeoutException:
            pass

    def create_signature(self, sender_name, mark_as_default):
        """
        Шорткат для создания подписи
        :return: None
        """
        general = self.general()
        creation = self.creation()

        general.create_signature()
        creation.set_sender_name(sender_name)

        if mark_as_default:
            creation.mark_as_default()

        creation.create()

    def edit_first_signature(self, sender_name, mark_as_default):
        """
        Шорткат для изменения первой подписи
        :return: None
        """
        general = self.general()
        editing = self.editing()

        general.edit_first_signature()

        editing.clear_first_sender_name()
        editing.set_first_sender_name(sender_name)

        if mark_as_default:
            editing.mark_first_as_default()

        editing.save_first()

    def edit_second_signature(self, sender_name, mark_as_default):
        """
        Шорткат для изменения второй подписи
        :return: None
        """
        general = self.general()
        editing = self.editing()

        general.edit_second_signature()

        editing.clear_second_sender_name()
        editing.set_second_sender_name(sender_name)

        if mark_as_default:
            editing.mark_second_as_default()

        editing.save_second()

    def edit_third_signature(self, sender_name, mark_as_default):
        """
        Шорткат для изменения третьей подписи
        :return: None
        """
        general = self.general()
        editing = self.editing()

        general.edit_third_signature()

        editing.clear_third_sender_name()
        editing.set_third_sender_name(sender_name)

        if mark_as_default:
            editing.mark_third_as_default()

        editing.save_third()

    def edit_first_signature_deep(self):
        """
        Шорткат для изменения первой подписи Серега
        :return: None
        """
        general = self.general()
        editing = self.editing()

        general.edit_first_signature()


        editing.save_first()