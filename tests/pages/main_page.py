import sys

from page import Page
from tests.components.sidebar import Sidebar

class MainPage(Page):
    @property
    def sidebar(self):
        return Sidebar(self.driver)

