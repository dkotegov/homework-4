from selenium import webdriver

from components.default import Component
from utils import wait_click_for_element_by_selector, wait_for_element_by_selector
from selenium.webdriver.common.keys import Keys


class Player(Component):
    CLOSE = '.js-close-video'
    FULLSCREEN = '.js-fullscreen'
    PARTSCREEN = '.js-partscreen'
    VIDEOPLAYER_FULLSCREEN = '.video-player__fullscreen'

    def click_on_close(self):
        wait_click_for_element_by_selector(self.driver, self.CLOSE)

    def click_on_fullscreen(self):
        wait_click_for_element_by_selector(self.driver, self.FULLSCREEN)

    def wait_for_fullscreen_btn(self):
        wait_for_element_by_selector(self.driver, self.FULLSCREEN)

    def click_on_partscreen(self):
        wait_click_for_element_by_selector(self.driver, self.PARTSCREEN)

    def is_fullscreen(self):
        try:
            wait_for_element_by_selector(self.driver, self.VIDEOPLAYER_FULLSCREEN)
            return True
        except:
            return False

    def esc_to_part_screen(self):
        wait_for_element_by_selector(self.driver, self.VIDEOPLAYER_FULLSCREEN)
        webdriver.ActionChains(self.driver).send_keys(Keys.ESCAPE).perform()


