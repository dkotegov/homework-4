from margarita.tests.virusmusic.default_auth import TestAuth
from margarita.tests.virusmusic.default_no_auth import TestNoAuth
from margarita.pages.virusmusic.main_page import MainPage
from margarita.utils import wait_for_pop_up, wait_for_url
from margarita.constants import BASE_URL, PLAYLIST_NAME


class TrackTestAuth(TestAuth):
    def setUp(self):
        super().setUp()
        page = MainPage(self.driver)


class TrackTestNoAuth(TestNoAuth):
    def setUp(self):
        super().setUp()
        page = MainPage(self.driver)