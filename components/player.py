from components.default import Component
from utils import wait_click_for_element_by_selector


class Player(Component):
    CLOSE = ".js-close-video"
    FULLSCREEN = ".js-fullscreen"

    def click_on_close(self):
        wait_click_for_element_by_selector(self.CLOSE)

    def click_on_fullscreen(self):
        wait_click_for_element_by_selector(self.FULLSCREEN)
