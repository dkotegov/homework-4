import sys

from page import Page
from tests.components.sidebar import Sidebar
from tests.components.letters import Letters

class MainPage(Page):
    @property
    def sidebar(self):
        return Sidebar(self.driver)

    @property
    def letters(self):
        return Letters(self.driver)

