from selenium.webdriver.common.by import By

from tests.pages.page import Page, Component


class UserAlbumsPage(Page):
    PATH = '/dk?st.cmd=userAlbums'

    @property
    def albums_list(self):
        return AlbumsList(self.driver)


class AlbumsList(Component):
    TITLE = 'albm'

    def includes(self, album_name):
        albums = self.driver.find_elements(By.CLASS_NAME, self.TITLE)
        for album in albums:
            if album.text == album_name:
                return True
        return False
