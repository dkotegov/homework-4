from Base import Page
from Banners import Banners

from .Directories import Directories
from .TabsAtHome import TabsAtHome
from .Buttons import Buttons
from .Documents import Documents

import urllib.parse


class HomePage(Page):
    BASE_URL = 'https://cloud.mail.ru/'
    PATH = 'home/'

    @property
    def folders(self):
        return Directories(self.driver)

    @property
    def tabs_at_home_p(self):
        return TabsAtHome(self.driver)

    @property
    def banners(self):
        return Banners(self.driver)

    @property
    def buttons(self):
        return Buttons(self.driver)

    @property
    def creating_documents(self):
        return Documents(self.driver)

    def open(self):
        url = urllib.parse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()



