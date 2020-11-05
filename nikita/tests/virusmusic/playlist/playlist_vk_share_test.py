from nikita.tests.virusmusic.playlist.default import PlaylistTest
from nikita.pages.virusmusic.playlist import PlaylistPage
from nikita.utils import wait_for_new_window, wait_for_url_to_match

class PlaylistVkShareTest(PlaylistTest):
    def test(self):
        page = PlaylistPage(self.driver, self.playlistId)
        handles = self.driver.window_handles
        main_window = self.driver.window_handles[0]
        page.vk_share()
        wait_for_new_window(self.driver, handles)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to_window(new_window)
        wait_for_url_to_match(self.driver, '.*vk\.com.*share.*')
        self.driver.switch_to_window(main_window)
