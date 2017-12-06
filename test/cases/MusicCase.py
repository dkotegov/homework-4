from Case import Case

import random
from hamcrest import *
import time

from config import config

from logger import log_d

from test.ok.MusicPage import MusicPage



class MusicTestCase(Case):
    def setUp(self):
        super(MusicTestCase, self).setUp()
        self.music_page = MusicPage(self.driver)
        self.addPage(self.music_page)

    def testOpenAndClosePanel(self):
        self.music_page.set_active_music_panel(True)
        self.music_page.set_active_music_panel(False)

    def testPlayAndStopMusic(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        self.music_page.set_play_music(True)

        # listen music 3 seconds
        time.sleep(3)

        self.music_page.set_play_music(False)

    def testHelpForm(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        self.music_page.click_help()

    def testAddToPopular(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        element = self.music_page.getFirstPopularElement()
        self.music_page.addToPopular(element)

    def testCheckCollect(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        self.music_page.choose_my_music()
        self.music_page.click_collect()


    def testCreateCollect(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        self.music_page.choose_my_music()
        self.music_page.click_and_create_collect("test" + str(random.randint(0, 100000))) # some increment

    def testClosePanel(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        self.music_page.click_close()

    def testUploadMusic(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)
        self.music_page.choose_upload_music()

    def testEditButton(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)

        self.music_page.choose_my_music()
        self.music_page.check_music_album_in_my_music()

    def testCheckVolume(self):
        self.music_page.set_active_music_panel(True, waitLoad=True)

        assert_that(self.music_page.get_volume_mute(), is_(False), "must have sound in first")
        self.music_page.set_volume(mute=True)
        self.music_page.set_volume(mute=False)
