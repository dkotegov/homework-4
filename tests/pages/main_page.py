# -*- coding: utf-8 -*-

import sys
import urlparse

from page import Page
from tests.components.sidebar import Sidebar
from tests.components.topbar import Topbar
from tests.components.folder_create import FolderCreate
from tests.components.folder_edit import FolderEdit
from tests.components.letters import Letters
from tests.components.folder_unlock import FolderUnlock
from tests.components.logout import Logout
from tests.components.write_letter import WriteLetter

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage(Page):
    BASE_URL = 'https://octavius.mail.ru/'

    def __init__(self, driver):
        Page.__init__(self, driver)
        self.sidebar.waitForVisible()
        self._redirect_to_qa()
        self.sidebar.click_to_inbox()

    @property
    def sidebar(self):
        return Sidebar(self.driver)

    @property
    def topbar(self):
        return Topbar(self.driver)

    @property
    def folder_create(self):
        return FolderCreate(self.driver)

    @property
    def letters(self):
        return Letters(self.driver)

    @property
    def folder_unlock(self):
        return FolderUnlock(self.driver)

    @property
    def logout(self):
        return Logout(self.driver)

    @property
    def folder_edit(self):
        return FolderEdit(self.driver)

    @property
    def write_letter(self):
        return WriteLetter(self.driver)

    def _redirect_to_qa(self):
        url = urlparse.urljoin(self.BASE_URL, '/bundles/page.qa.html')
        self.driver.get(url)
