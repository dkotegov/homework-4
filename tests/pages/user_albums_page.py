from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.page import Page, Component


class UserAlbumsPage(Page):
    PATH = '/dk?st.cmd=userAlbums'

    @property
    def albums_list(self):
        return AlbumsList(self.driver)


class AlbumsList(Component):
    ITEM = 'photos_album-grid-w'
    TITLE = 'albm'

    def includes(self, album_name):
        albums = self.driver.find_elements_by_class_name(self.TITLE)
        for album in albums:
            if album.text == album_name:
                return True
        return False

    def find(self, album_name):
        albums = self.driver.find_elements_by_class_name(self.ITEM)
        for album in albums:
            if album.find_element_by_class_name(self.TITLE).text == album_name:
                return AlbumItem(album)
        raise KeyError


class AlbumItem(Component):
    LIKE = 'widget_like'
    LIKES_COUNT = 'ecnt'
    TITLE = 'albm'

    def like(self):
        self.driver.find_element_by_class_name(self.LIKE).click()

    @property
    def likes_count(self):
        likes_count = WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, self.LIKES_COUNT))
        )
        return int(likes_count.text)
