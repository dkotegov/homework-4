from selenium.webdriver.common.keys import Keys

from nikita.pages.virusmusic.default import Page
from nikita.utils import wait_for_element_by_selector, wait_for_pop_up

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

    def wait_for_playlist(self, name):
        wait_for_element_by_selector(self.driver, self.CARD.format(name))

    def change_name(self, name, newName):
        self.edit()
        input = self.driver.find_element_by_css_selector(self.TEXT_INPUT.format(name))
        input.clear()
        input.send_keys(newName)
        self.edit()

    def load_image(self, name, path):
        self.edit()
        self.driver.find_element_by_css_selector(self.IMAGE_INPUT.format(name)).send_keys(path)
        self.edit()

    def delete_playlist(self, name):
        self.edit()
        delete = wait_for_element_by_selector(self.driver, self.DELETE.format(name))
        delete.click()

    def edit(self):
        edit = wait_for_element_by_selector(self.driver, self.EDIT)
        edit.click()
