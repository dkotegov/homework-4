# -*- coding: utf-8 -*-
from page import Page
from tests.components.searchbar import Searchbar


class MainPage(Page):
    BASE_URL = 'https://octavius.mail.ru/'

    @property
    def searchbar(self):
        return Searchbar(self.driver)

    # Ждём загрузки страницы по элементу. В данном случае по серчбару.
    def waitForVisible(self):
        searchbar = self.searchbar
        searchbar.waitForVisible()

