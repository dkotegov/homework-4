from urllib.parse import urlparse, parse_qs

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.mobile.page import Page, Component
from tests.utils.waits import wait_until_url_changes


class UserAlbumPage(Page):
    PATH = '/dk?st.cmd=userAlbum&st.albId={}'
    ALBUM_ID = 'st.albId'

    def __init__(self, driver, album_id=None):
        super().__init__(driver)
        self.album_id = album_id

    @property
    def empty_album(self):
        return EmptyAlbum(self.driver)

    @property
    def album_header(self):
        return AlbumHeader(self.driver)

    @property
    def photos_list(self):
        return PhotosList(self.driver)

    @property
    def toolbar(self):
        return Toolbar(self.driver)

    @property
    def confirmation_modal(self):
        return ConfirmationModal(self.driver)

    def open(self, path=None):
        if path is None:
            path = self.PATH.format(self.album_id)
        super().open(path)

    def parse_album_id(self):
        qs = urlparse(self.driver.current_url).query
        self.album_id = parse_qs(qs)[self.ALBUM_ID][0]
        return self.album_id


class EmptyAlbum(Component):
    TITLE = 'ep-ttl-txt'

    @property
    def title(self):
        return self.driver.find_element_by_class_name(self.TITLE).text


class AlbumHeader(Component):
    COVER = '//div[@class="user-album"]//div[contains(@class, "icvr")]'
    COVER_ID = 'id'

    @property
    def cover_id(self):
        url = self.driver.find_element_by_xpath(self.COVER).get_attribute('style')
        qs = urlparse(url).query
        return parse_qs(qs)[self.COVER_ID][0]


class PhotosList(Component):
    ITEM = 'sil'

    @property
    def count(self):
        return len(self.driver.find_elements_by_class_name(self.ITEM))

    @property
    def first(self):
        return self.get(0)

    def get(self, index):
        return PhotoItem(self.driver, self.driver.find_elements_by_class_name(self.ITEM)[index])


class PhotoItem(Component):
    ITEM = 'sil'
    PHOTO_ID = 'st.phoId'
    IMAGE_ID = 'id'

    @property
    def id(self):
        href = self.element.get_attribute('href')
        qs = urlparse(href).query
        return parse_qs(qs)[self.PHOTO_ID][0]

    @property
    def image_id(self):
        url = self.element.get_attribute('style')
        qs = urlparse(url).query
        return parse_qs(qs)[self.IMAGE_ID][0]

    @wait_until_url_changes
    def open(self):
        self.element.click()


class Toolbar(Component):
    TOOLBAR_BUTTON = 'js-t-widget'
    EDIT_BUTTON = 'ic-edit'
    DELETE_BUTTON = 'ic-del'

    def open(self):
        WebDriverWait(self.driver, 2, 0.1).until(EC.element_to_be_clickable((By.ID, self.TOOLBAR_BUTTON))).click()

    @wait_until_url_changes
    def edit(self):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, self.EDIT_BUTTON))).click()

    def delete(self):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, self.DELETE_BUTTON))).click()


class ConfirmationModal(Component):
    DELETE_BUTTON = 'button_delete'

    @wait_until_url_changes
    def delete(self):
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.NAME, self.DELETE_BUTTON))).click()
