from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.mobile.page import Page, Component
from tests.utils.waits import wait_until_url_changes


class UserAlbumsPage(Page):
    PATH = '/dk?st.cmd=userAlbums'

    @property
    def albums_list(self):
        return AlbumsList(self.driver)

    @property
    def header(self):
        return AlbumsHeader(self.driver)


class AlbumsHeader(Component):
    CREATE_BUTTON = 'addition-button'

    @wait_until_url_changes
    def create_album(self):
        self.driver.find_element_by_class_name(self.CREATE_BUTTON).click()


class AlbumsList(Component):
    ITEM = 'photos_album-grid-w'
    TITLE = 'albm'

    def includes(self, album_name):
        albums = self.driver.find_elements_by_class_name(self.TITLE)
        for album in albums:
            if album.text == album_name:
                return True
        return False

    @property
    def first(self):
        return AlbumItem(self.driver, 2)


class AlbumItem(Component):
    BASE = '//ul[@id="user-albums"]/li[{}]'
    LIKE = '//a[@data-func="performLike"]'
    CANCEL_LIKE = '//a[@data-func="unReact"]'
    LIKES_COUNT = '//span[@class="ecnt"]'

    def __init__(self, driver, id):
        super().__init__(driver)
        self.id = id
        self.base = self.BASE.format(id)

    def like(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.LIKE))
        ).click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.CANCEL_LIKE))
        )

    def cancel_like(self):
        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.CANCEL_LIKE))
        ).click()

        WebDriverWait(self.driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, self.base + self.LIKE))
        )

    @property
    def likes_count(self):
        try:
            likes_count = WebDriverWait(self.driver, 2).until(
                EC.presence_of_element_located((By.XPATH, self.base + self.LIKES_COUNT))
            )
            return int(likes_count.text)
        except TimeoutException:
            return 0
