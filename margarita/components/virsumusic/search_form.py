from margarita import utils
from margarita.components.virsumusic.default import Component


class SearchForm(Component):
    SEARCH_FIELD = '//*[@class="m-search-input m-desktop-tablet-only"]'
    SEARCH_BUTTON = '//*[@class="m-lupa-button m-search-icon m-desktop-tablet-only"]'

    SEARCH_ARTIST_RESULT = '//div[contains(text(), "{}")][@class="m-small-text m-small-artist"]'
    SEARCH_ALBUM_OR_TRACK_RESULT = '//div[contains(text(), "{0}")]/parent::div[contains(@class, "m-small-{1}")]'

    def enter_string(self, string):
        utils.wait_for_element_by_xpath(self.driver, self.SEARCH_FIELD).send_keys(string)

    def search(self):
        utils.wait_for_element_by_xpath(self.driver, self.SEARCH_BUTTON).click()

    def search_result(self, type, name):
        if type == "artist":
            utils.wait_for_element_by_xpath(self.driver, self.SEARCH_ARTIST_RESULT.format(name)).click()
        else:
            utils.wait_for_element_by_xpath(self.driver, self.SEARCH_ALBUM_OR_TRACK_RESULT.format(name, type)).click()
