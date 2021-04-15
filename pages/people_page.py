from pages.base_page import Page
from pages.navbar import NavBar
from pages.base_component import Component


class PeoplePage(Page, Component):
    PATH = '/people'

    DISGUISHT_PEOPLE = '//button[contains(text(),"Избранные люди")]'

    CARD_LIKE_ICON = '//img[@class="user-card__like"]'
    DOWNLOAD_MORE = '//button[@class="card-wrapper__button"]'

    @property
    def navbar(self):
        return NavBar(self.driver)

    def click_disguisht(self):
        self._wait_until_clickable(self.DISGUISHT_PEOPLE).click()

    def click_like_icon(self):
        self._wait_until_clickable(self.CARD_LIKE_ICON).click()

    def click_download_more(self):
        self._wait_until_clickable(self.DOWNLOAD_MORE).click()

    def handle_like(self):
        self._wait_until_preset(self.LIKE_UPDATE_CONFIRMATION)

    

    # TODO: add missing components
