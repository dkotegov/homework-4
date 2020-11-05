from selenium.webdriver.common.keys import Keys

from margarita.pages.default import Page
from margarita.utils import wait_for_element_by_selector, wait_for_pop_up


class ProfilePlaylistsPage(Page):
    PATH = '/profile/playlists'
    EDIT = '.m-right-col.m-playlist-section-edit-button'
    NAME_INPUT = 'div[id="new playlist input"] input'
    CARD = '.l-list-card[data-test-name="{}"]'
    TEXT_INPUT = '.l-list-card[data-test-name="{}"] input[type="text"]'
    IMAGE_INPUT = '.l-list-card[data-test-name="{}"] input[type="file"]'
    DELETE = '.l-list-card[data-test-name="{}"] img[title="delete playlist"]'

    def create_playlist(self, name):
        self.open()
        input = wait_for_element_by_selector(self.driver, self.NAME_INPUT)
        input.clear()
        input.send_keys(name + Keys.ENTER)

    def get_playlist_id(self, name):
        return wait_for_element_by_selector(self.driver, self.CARD.format(name)).get_attribute('a-id')