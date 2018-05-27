from random import randint

from tests.Lilbs.Lib import Lib
from tests.models.Component import Component
from tests.models.Page import Page


class AlbumPage(Page):
    @property
    def page(self):
        return AlbumPage(driver=self.driver)


class AlbumComponent(Component):

    random_album_name = '%dalbum%d' % (randint(1, 9999), randint(1, 9999))
    create_album_btn_css = 'span[class="tico"]'
    album_name_css = '[class="form__gl-1-2 form photo-album-settings"] [type="text"]'
    save_btn_css = '.formButtonContainer [type]'
    albums_css = 'a[class="o"]'

    def open_photos_page(self):
        url = self.driver.find_element_by_css_selector(
            '[data-l="t\,selectCurrentUser"]').get_attribute('href') + '/photos'
        self.driver.get(url)

    def fill_name(self):
        album_name_el = Lib.simple_wait_element_css(
            self.driver, self.album_name_css)
        album_name_el.send_keys(self.random_album_name)

    def create_album(self):
        create_album_btn = Lib.simple_wait_element_css(
            self.driver, self.create_album_btn_css)
        self.jsClick(create_album_btn)
        self.fill_name()
        save_btn = Lib.simple_wait_element_css(self.driver, self.save_btn_css)
        self.jsClick(save_btn)

    def get_albums(self):
        albums = []
        for album in self.driver.find_elements_by_css_selector(self.albums_css):
            albums.append(album.text)
        return albums
