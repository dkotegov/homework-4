from tests.pages.mobile.like_component import LikeComponent
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

    @property
    def like(self):
        return LikeComponent(self.driver, self.base)
