from page import Page
from tests.components.letters import Letters
from tests.components.sidebar import Sidebar
from tests.components.topbar import Topbar


class DraftsPage(Page):
    PATH = '/drafts/'
    BASE_URL = 'https://octavius.mail.ru/'

    @property
    def sidebar(self):
        return Sidebar(self.driver)

    @property
    def letters(self):
        return Letters(self.driver)

    @property
    def topbar(self):
        return Topbar(self.driver)

    def clear_letters(self):
        if self.letters.has_letters():
            self.letters.select_one()
            self.topbar.select_all()
            self.topbar.delete()
