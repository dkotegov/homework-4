from os import environ

from utils.helpers import wait_for_visible
from pages.default import DefaultPage, Component


class ProfilePage(DefaultPage):
    FOLLOWERS = '#followers-number'
    FOLLOW_BUTTON = '#follow-button'
    AVATAR_IMG = '.avatar-container__avatar'

    def __init__(self, driver, username=environ['LOGIN']):
        super().__init__(driver, f'/user/{username}')
        self.create_playlist_component = CreatePlaylist(self.driver)
        self.playlists_list_component = PlaylistsList(self.driver)

    @property
    def followers(self):
        wait_for_visible(self.driver, self.FOLLOWERS)
        return int(self.driver.find_element_by_css_selector(self.FOLLOWERS).text)

    @property
    def follow_button(self):
        wait_for_visible(self.driver, self.FOLLOW_BUTTON)
        return self.driver.find_element_by_css_selector(self.FOLLOW_BUTTON)

    @property
    def playlists(self):
        return self.playlists_list_component.get_playlists()

    @property
    def create_playlist_form(self):
        return self.create_playlist_component.CREATE_PLAYLIST_INPUT

    @property
    def avatar_img_src(self):
        wait_for_visible(self.driver, self.AVATAR_IMG)
        return self.driver.find_elements_by_css_selector(self.AVATAR_IMG)[0].get_attribute('src')

    def create_playlist(self, playlist_name):
        self.create_playlist_component.start_create_playlist()
        self.create_playlist_component.fill_create_playlist_input(playlist_name)
        self.create_playlist_component.submit_create_playlist()

    def cancel_create_playlist(self, playlist_name):
        self.create_playlist_component.start_create_playlist()
        self.create_playlist_component.fill_create_playlist_input(playlist_name)
        self.create_playlist_component.cancel_create_playlist()

    def toggle_follow(self):
        self.follow_button.click()


class CreatePlaylist(Component):
    CREATE_PLAYLIST_BUTTON = '#create-playlist-button'
    CREATE_PLAYLIST_INPUT = '#input-create-playlist'
    CREATE_PLAYLIST_SUBMIT = '#submit-create-playlist'
    CREATE_PLAYLIST_CANCEL = '#cancel-create-playlist'

    def start_create_playlist(self):
        wait_for_visible(self.driver, self.CREATE_PLAYLIST_BUTTON)
        self.driver.find_element_by_css_selector(self.CREATE_PLAYLIST_BUTTON).click()

    def fill_create_playlist_input(self, playlist_name):
        wait_for_visible(self.driver, self.CREATE_PLAYLIST_INPUT)
        self.driver.find_element_by_css_selector(self.CREATE_PLAYLIST_INPUT).click()
        self.driver.find_element_by_css_selector(self.CREATE_PLAYLIST_INPUT).send_keys(playlist_name)

    def submit_create_playlist(self):
        wait_for_visible(self.driver, self.CREATE_PLAYLIST_SUBMIT)
        self.driver.find_element_by_css_selector(self.CREATE_PLAYLIST_SUBMIT).click()

    def cancel_create_playlist(self):
        wait_for_visible(self.driver, self.CREATE_PLAYLIST_CANCEL)
        self.driver.find_element_by_css_selector(self.CREATE_PLAYLIST_CANCEL).click()


class PlaylistsList(Component):
    PLAYLISTS_CONTAINER = '#tabs'
    PLAYLISTS_ITEMS = '.tab__title'

    def get_playlists(self):
        wait_for_visible(self.driver, self.PLAYLISTS_CONTAINER)
        playlists = self.driver.find_elements_by_css_selector(self.PLAYLISTS_ITEMS)
        return [playlist.text for playlist in playlists]
