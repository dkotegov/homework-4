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

    DIV_CLASS_POPULARS = "mus_card_i"
    SPAN_CLASS_POPULARS_ADD = "mus_card_ac_i__add"
    SPAN_CLASS_POPULARS_SUCCESS = "mus_card_ac_i__success"

    #############
    # left list #
    DIV_UPLOAD = "lmSecm_sec_upload"
    DIV_MY_MUSIC = "lmSecm_sec_klass"
    #############

    DIV_CLASS_CREATE_COLLECT_BUTTON = "m_ic_create-collection"
    DIV_CLASS_CREATE_COLLECT = "mus_playlist-add"

    BUTTON_CLASS_CREATE_COLLECT = "gwt-uid-720" # it's ID

    UL_COLLECTIONS = "lmPPLlst"

    ########
    # find #
    FIND_IN_COLLECTIONS = "//div[contains(text(), '{}')]"
    ########

    SPAN_CLASS_CLOSE_BUTTON = "mml_ic_close"

    DIV_CLASS_UPLOAD_FORM_XPATH = "//div[contains(@class, 'mus_upload')]"
    INPUT_UPLOAD_XPATH = "//input[@accept='audio/mpeg' and contains(@class, 'vl_btn_it')]"

    DIV_CLASS_MY_ALBUM = "mus_album"

    DIV_CLASS_VOLUME = "mus_player-volume"
    DIV_CLASS_VOLUME_ICON = "mus_player-volume_ic"
    DIV_CLASS_VOLUME_MUTE = "__mute"

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

    def _assert_volume(self, icon_element, mute):
        waitMute = lambda s: icon_element.get_attribute("class").find(self.DIV_CLASS_VOLUME_MUTE) > 0
        if mute:
            self.wait.until(waitMute)
        else:
            self.wait.until_not(waitMute)

    def _wait_load_artist(self):
        def checkArtists(s):
            elements = s.find_elements_by_class_name(self.TITLE_CLASS_ARTIST)
            if len(elements) == 0:
                return False

            return len(elements[0].text) > 0

        self.wait.until(lambda s: checkArtists(s))

    def __init__(self, driver):
        super(MusicPage, self).__init__(driver, "music_page")

    def choose_my_music(self):
        self._assert_active_music_panel(True)

        self.driver.find_element_by_id(self.DIV_MY_MUSIC).click()
        self.wait.until(lambda s: self.driver.find_element_by_id(self.UL_COLLECTIONS).is_displayed())

    def choose_upload_music(self):
        self._assert_active_music_panel(True)

        self.driver.find_element_by_id(self.DIV_UPLOAD).click()

        get_upload_form = lambda : self.driver.find_element_by_xpath(self.DIV_CLASS_UPLOAD_FORM_XPATH)
        self.wait.until(lambda s: get_upload_form().is_displayed())

        # try find
        get_upload_form().find_element_by_xpath(self.INPUT_UPLOAD_XPATH)

    def set_active_music_panel(self, active_flag, waitLoad=False):
        self._assert_active_music_panel(not active_flag)
        self.driver.find_element_by_id(self.TOOLBAR_MUSIC).click()
        self._assert_active_music_panel(active_flag)

        if waitLoad:
            self._wait_load_artist()

    # return on_flag
    def get_volume_mute(self):
        self._assert_active_music_panel(True)
        controlls = self.getElementByClass(self.driver, self.DIV_CLASS_VOLUME)
        icon_volume = self.getElementByClass(controlls, self.DIV_CLASS_VOLUME_ICON)

        return icon_volume.get_attribute("class").find(self.DIV_CLASS_VOLUME_MUTE) > 0

    def set_volume(self, mute):
        self._assert_active_music_panel(True)
        controlls = self.getElementByClass(self.driver, self.DIV_CLASS_VOLUME)
        icon_volume = self.getElementByClass(controlls, self.DIV_CLASS_VOLUME_ICON)

        icon_volume.click()
        self._assert_volume(icon_volume, mute)

    def set_play_music(self, active_flag):
        self._assert_active_music_panel(True)
        self._assert_play_music(not active_flag)

        self.driver.find_element_by_xpath(self.BUTTON_CLASS_XPATH).click()
        self._assert_play_music(active_flag)

    def click_help(self):
        self._assert_active_music_panel(True)

        self.getElementByClass(self.driver, self.BUTTON_CLASS_HELP, tag="play").click()
        self._assert_help_form()

    def getFirstPopularElement(self):
        self._assert_active_music_panel(True)

        populars = self.driver.find_elements_by_class_name(self.DIV_CLASS_POPULARS)
        assert_that(len(populars), greater_than_or_equal_to(1), "cannot find popular collect")
        return populars[0]

    def addToPopular(self, popularElement):
        self._assert_active_music_panel(True)

        buttonAdd = self.getElementByClass(popularElement, self.SPAN_CLASS_POPULARS_ADD, tag="popular add")
        spanSuccess = self.getElementByClass(popularElement, self.SPAN_CLASS_POPULARS_SUCCESS, tag="popular success")

        self.actions.move_to_element(popularElement).pause(3).click(buttonAdd).perform()
        self.wait.until(lambda s: spanSuccess.is_displayed())

    def click_collect(self):
        self._assert_active_music_panel(True)

        base = self.driver.find_element_by_id(self.UL_COLLECTIONS)
        el = self.getElementByClass(base, self.DIV_CLASS_CREATE_COLLECT_BUTTON, tag="create collect")
        button_create = self.getParent(el)

        button_create.click()

        self.wait.until(lambda s: s.find_elements_by_class_name(self.DIV_CLASS_CREATE_COLLECT))

    def click_and_create_collect(self, name_collect):
        self._assert_active_music_panel(True)

        self.click_collect()

        base = self.getElementByClass(self.driver, self.DIV_CLASS_CREATE_COLLECT, "collect input")

        collect_field = self.driver.find_element_by_xpath("//input[@type='text' and contains(@class, 'vl_it')]")
        collect_field.send_keys(name_collect)

        scope_buttons = self.getElementByClass(base, "form-actions", tag="collect click")
        self.getElementByClass(scope_buttons, "vl_btn", tag="click button").click()

        all_collections = self.driver.find_element_by_id(self.UL_COLLECTIONS)
        self.wait.until(lambda s: all_collections.find_element_by_xpath(self.FIND_IN_COLLECTIONS.format(name_collect)))

    def click_close(self):
        self._assert_active_music_panel(True)

        self.getElementByClass(self.driver, self.SPAN_CLASS_CLOSE_BUTTON, tag="find button").click()
        self._assert_active_music_panel(False)

    # check only edit button
    def check_music_album_in_my_music(self):
        album = self.getFirstElementByClass(self.driver, self.DIV_CLASS_MY_ALBUM)
        album.find_element_by_xpath("//a[contains(@class, 'js-pl-edit')]")
