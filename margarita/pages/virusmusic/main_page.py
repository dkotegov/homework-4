from selenium.webdriver import ActionChains

import margarita.utils as utils
from margarita.pages.virusmusic.default import Page
from margarita.components.virsumusic.search_form import SearchForm


class MainPage(Page):
    PATH = '/'
    TRACK_ID = 't-id'
    FIRST_TRACK_IN_LIST = '//*[@class="l-track-big"]'
    LIKE_BUTTON_BY_ID = '//*[@t-id={}]//*[@class="l-big-track-button favorite-button"]/*'
    TRACK_BY_ID = '//*[@t-id={}]'
    NOT_LIKED_CLASS = 'm-big-like-button is-not-liked'
    LIKED_CLASS = 'm-big-like-button is-liked'
    CLASS = 'class'
    ADD_BUTTON_BY_ID = '//*[@t-id={}]//*[@class="l-big-track-button add-button"]/*'
    PLAY_BUTTON_BY_ID = '//*[@t-id={}]/*[@class="m-track-image"]'
    TRIGGER_BUTTON = '//div[contains(@class, "l-player")]'
    TRACK_IN_QUEUE = '//div[contains(@class, "l-player-track")][@id={}]'
    REMOVE_FROM_QUEUE_BUTTON = '//div[contains(@class, "l-player-track")][@id={}]/*//div[contains(@class, "delete-button")]/*'
    PLAYLIST_BY_NAME = '//span[contains(text(), {})]'
    PLAYLIST_PROP_BY_NAME = '//span[contains(text(), {})]/parent::*'
    CLOSE_WINDOW = '//*[@class="m-close-choose-menu-button"]'
    PLAYLIST_BY_ID = '//*[@p-id={}]'
    PLAY_TRACK_BY_NUM = '//div[contains(@class,"l-player-track")][{}]'
    PLAY_TRACK_BY_NUM_BUTTON = '//*[@class="l-player-track row border-bottom"][{}]/*[@class="m-track-photo"]'
    CURRENT_MAKER = '//*[@class="current-marker"]'
    PLAYER_NEXT = '//*[@class="player-control-button next"]'
    PLAYER_PREV = '//*[@class="player-control-button prev"]'
    PLAYER_ARROW = '//img[contains(@class, "player-trigger-arrow")]'

    SHUFFLE_SELECTOR = 'img.playlist-control-button.shuffle'
    CYCLE_SELECTOR = 'img.playlist-control-button.repeat'

    CLASS_NOT_FOUND = '//div[@class="no-found"]'

    def get_first_track_id(self):
        return utils.wait_for_element_by_xpath(self.driver, self.FIRST_TRACK_IN_LIST).get_attribute(self.TRACK_ID)

    def press_track_like_button(self, track_id):
        track = utils.wait_for_element_by_xpath(self.driver, self.TRACK_BY_ID.format(track_id))
        ActionChains(self.driver).move_to_element(track).click(
            self.driver.find_element_by_xpath(self.LIKE_BUTTON_BY_ID.format(track_id))).perform()

    def is_liked(self, track_id):
        track = utils.wait_for_element_by_xpath(self.driver, self.TRACK_BY_ID.format(track_id))
        ActionChains(self.driver).move_to_element(track).perform()
        like_class = self.driver.find_element_by_xpath(self.LIKE_BUTTON_BY_ID.format(track_id)).get_attribute(
            self.CLASS)
        if like_class == self.NOT_LIKED_CLASS:
            return False
        else:
            return True

    def is_like_visible(self, track_id):
        track = utils.wait_for_element_by_xpath(self.driver, self.TRACK_BY_ID.format(track_id))
        ActionChains(self.driver).move_to_element(track).perform()
        try:
            utils.wait_for_element_by_xpath(self.driver, self.LIKE_BUTTON_BY_ID.format(track_id))
            return True
        except:
            return False

    def is_add_visible(self, track_id):
        track = utils.wait_for_element_by_xpath(self.driver, self.TRACK_BY_ID.format(track_id))
        ActionChains(self.driver).move_to_element(track).perform()
        try:
            utils.wait_for_element_by_xpath(self.driver, self.ADD_BUTTON_BY_ID.format(track_id))
            return True
        except:
            return False

    def press_add_to_playlist(self, track_id, playlist_name, playlist_id):
        utils.wait_for_element_by_xpath(self.driver, self.TRACK_BY_ID.format(track_id))
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_xpath(self.TRACK_BY_ID.format(track_id))) \
            .perform()
        utils.wait_for_element_by_xpath(self.driver, self.ADD_BUTTON_BY_ID.format(track_id)).click()
        playlist = utils.wait_for_element_by_xpath(self.driver, self.PLAYLIST_BY_ID.format(playlist_id))
        ActionChains(self.driver).move_to_element(playlist).click(playlist).perform()
        is_included = playlist.get_attribute("is-include")
        utils.wait_for_element_by_xpath(self.driver, self.CLOSE_WINDOW).click()
        return is_included

    def play(self, track_id):
        utils.wait_for_element_by_xpath(self.driver, self.PLAY_BUTTON_BY_ID.format(track_id)).click()

    def get_player_pos(self):
        pos = utils.wait_for_element_by_xpath(self.driver, self.TRIGGER_BUTTON).get_attribute("style")
        return pos

    def wrap_player(self):
        ActionChains(self.driver).move_to_element(utils.wait_for_element_by_xpath(self.driver, self.TRIGGER_BUTTON)) \
            .click(self.driver.find_element_by_xpath(self.PLAYER_ARROW)).perform()

    def remove_from_queue(self, track_id):
        track = utils.wait_for_element_by_xpath(self.driver, self.TRACK_IN_QUEUE.format(track_id))
        ActionChains(self.driver).move_to_element(track).perform()
        utils.wait_for_element_by_xpath(self.driver, self.REMOVE_FROM_QUEUE_BUTTON.format(track_id)).click()

    def queue_contains(self, track_id):
        try:
            utils.wait_for_element_by_xpath(self.driver, self.TRACK_IN_QUEUE.format(track_id))
            return True
        except:
            return False

    def get_current_id(self):
        return utils.wait_for_element_by_xpath(self.driver, self.CURRENT_MAKER).get_attribute("current-id")

    def play_track_in_queue(self, track_num):
        utils.wait_for_element_by_xpath(self.driver, self.PLAY_TRACK_BY_NUM_BUTTON.format(track_num)).click()

    def play_next(self):
        utils.wait_for_element_to_be_clickable_by_xpath(self.driver, self.PLAYER_NEXT).click()

    def play_prev(self):
        utils.wait_for_element_by_xpath(self.driver, self.PLAYER_PREV).click()

    def shuffle(self):
        utils.wait_for_element_by_selector(self.driver, self.SHUFFLE_SELECTOR).click()

    def cycle(self):
        utils.wait_for_element_by_selector(self.driver, self.CYCLE_SELECTOR).click()

    def enter_search(self, string):
        search_form = SearchForm(self.driver)
        search_form.enter_string(string)

    def search_result(self, type, artist_name):
        search_form = SearchForm(self.driver)
        search_form.search_result(type, artist_name)

    def press_search_button(self):
        search_form = SearchForm(self.driver)
        search_form.search()

    def wait_for_not_found_search(self):
        utils.wait_for_element_by_xpath(self.driver, self.CLASS_NOT_FOUND)
