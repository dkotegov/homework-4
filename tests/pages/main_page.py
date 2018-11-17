# -*- coding: utf-8 -*-

import sys
import urlparse

from page import Page
from tests.components.sidebar import Sidebar
from tests.components.topbar import Topbar
from tests.components.folder_create import FolderCreate
from tests.components.letters import Letters
from tests.components.folder_unlock import FolderUnlock
from tests.components.logout import Logout


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(Page):
    BASE_URL = 'https://octavius.mail.ru/'

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
    
    def redirectToQa(self):
        url = urlparse.urljoin(self.BASE_URL, '/bundles/page.qa.html')
        self.driver.get(url)

    # Ждём загрузки страницы по элементу. В данном случае по сайдбару.
    def waitForVisible(self):
        sidebar = self.sidebar
        sidebar.waitForVisible()

    # Вход в папку "Входящие"
    def go_to_inbox(self):
        sidebar = self.sidebar
        sidebar.click_to_inbox()


