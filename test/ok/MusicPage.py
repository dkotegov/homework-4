from Page import Page
from hamcrest import *

class MusicPage(Page):
    TOOLBAR_MUSIC = "hook_ToolbarIconMusic_ToolbarIconMusic"

    TOOLBAR_CLASS_MUSIC = "toolbar_nav_a__audio"
    TOOLBAR_CLASS_MUSIC_ACTIVE = "toolbar_nav_a__audio__active"

    BUTTON_CLASS_PLAY = "__pause"
    BUTTON_CLASS_PLAY2 = "mus_player-controls_i"
    BUTTON_CLASS_XPATH = "//div[contains(@class, 'mus_player-controls_i') and contains(@class, '__pause')]"

    BUTTON_CLASS_PLAY_START_XPATH = "//div[contains(@class, 'mus_player-controls_i') and contains(@class, '__pause') and not(contains(@class, '__play'))]"

    TITLE_CLASS_ARTIST = "mus_player_artist"

    BUTTON_CLASS_HELP = "mml_ic_help"

    POPLAYER_HELP = "hook_Block_PopLayer"
    POPLAYER_HELP_FORM = "hook_Block_HelpFeedbackForm"

    def _assert_active_music_panel(self, isActive):
        self.driver.find_elements_by_class_name(self.TOOLBAR_CLASS_MUSIC)

        waitShowPanel = lambda s: s.find_elements_by_class_name(self.TOOLBAR_CLASS_MUSIC_ACTIVE)
        if isActive:
            self.wait.until(waitShowPanel)
        else:
            self.wait.until_not(waitShowPanel)

    def _assert_play_music(self, isActive):
        self.driver.find_element_by_xpath(self.BUTTON_CLASS_XPATH)

        waitStopStatus = lambda s: s.find_element_by_xpath(self.BUTTON_CLASS_PLAY_START_XPATH)
        if isActive:
            self.wait.until(waitStopStatus)
        else:
            self.wait.until_not(waitStopStatus)

    def _assert_help_form(self):
        waitForm = lambda s: s.find_element_by_id(self.POPLAYER_HELP_FORM)
        self.wait.until(waitForm)

    def _wait_load_artist(self):
        wait_artist = lambda s: len(s.find_elements_by_class_name(self.TITLE_CLASS_ARTIST)[0].text) > 0
        self.wait.until(wait_artist)

    def __init__(self, driver):
        super(MusicPage, self).__init__(driver, "music_page")

    def set_active_music_panel(self, active_flag):
        self._assert_active_music_panel(not active_flag)
        self.driver.find_element_by_id(self.TOOLBAR_MUSIC).click()
        self._assert_active_music_panel(active_flag)

    def set_play_music(self, active_flag):
        self._assert_active_music_panel(True)
        self._assert_play_music(not active_flag)

        self._wait_load_artist()

        self.driver.find_element_by_xpath(self.BUTTON_CLASS_XPATH).click()
        self._assert_play_music(active_flag)

    def click_help(self):
        self._assert_active_music_panel(True)
        self._wait_load_artist()

        objs = self.driver.find_elements_by_class_name(self.BUTTON_CLASS_HELP)
        assert_that(objs, has_length(1), "bad button class play")
        objs[0].click()

        self._assert_help_form()