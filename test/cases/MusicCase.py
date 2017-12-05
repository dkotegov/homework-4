from Case import Case

from config import config

from logger import log_d

from test.ok.MusicPage import MusicPage

class MusicTestCase(Case):
    def setUp(self):
        super(MusicTestCase, self).setUp()
        self.music_page = MusicPage(self.driver)
        self.addPage(self.music_page)

    # def testOpenAndClosePanel(self):
    #     self.music_page.set_active_music_panel(True)
    #     self.music_page.set_active_music_panel(False)

    # def testPlayAndStopMusic(self):
    #     self.music_page.set_active_music_panel(True)
    #     self.music_page.set_play_music(True)
    #     self.music_page.set_play_music(False)

    def testHelpForm(self):
        self.music_page.set_active_music_panel(True)
        self.music_page.click_help()
