# -*- coding: utf-8 -*-

import sys
import urlparse

from page import Page
from tests.components.old_folder_settings_form import FoldersSettingsOld

class SettingsFolders(Page):
    BASE_URL = 'https://e.mail.ru/'
    PATH = '/settings/folders'

    @property
    def settings_form(self):
        return FoldersSettingsOld(self.driver)