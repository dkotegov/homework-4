from tests.photo_manipulation import PhotoManipulationTest
from tests.pages.primary.components.photos.photo_overlay import PhotoComponent
from tests.pages.primary.photo_page import PhotoPage
from tests.pages.primary.main_page import MainPage

from util import config


class GetLinkTest(PhotoManipulationTest):
    def setUp(self):
        super(GetLinkTest, self).setUp()

    def tearDown(self):
        super(GetLinkTest, self).tearDown()

    def test_get_link(self):
        photos = self.driver.current_url
        photo_page = PhotoPage(self.driver)
        photo_page.goto()
        photo = photo_page.get_photo()

        photo.open_overlay()
        url = photo.get_photo_link()

        self.driver.get(url)
        second_url = photo.get_photo_link()

        self.assertEquals(url, second_url)
        self.driver.get(photos)

    def test_get_avatar_link(self):
        avatar_link = self.get_avatar_link()

        photo_page = PhotoPage(self.driver)
        photo_page.goto()
        photos = self.driver.current_url
        photo = photo_page.get_photo()
        photo.open_overlay()
        photo_link = photo.get_photo_link()
        self.driver.get(photos)
        self.driver.implicitly_wait(config.WAITING_TIME)

        self.assertNotEqual(avatar_link, photo_link)

        self.set_avatar(photo_link)
        MainPage(self.driver).goto()
        new_avatar_link = self.get_avatar_link()
        self.assertEquals(photo_link, new_avatar_link)

        self.set_avatar(avatar_link)
        new_avatar_link = self.get_avatar_link()
        self.assertEquals(avatar_link, new_avatar_link)
        self.driver.get(photos)
        self.driver.implicitly_wait(config.WAITING_TIME)

    def set_avatar(self, url):
        old_url = self.driver.current_url
        self.driver.get(url)
        self.driver.implicitly_wait(config.WAITING_TIME)
        photo = PhotoComponent(self.driver)
        photo.set_as_avatar()
        self.driver.implicitly_wait(config.WAITING_TIME)
        self.driver.get(old_url)
        self.driver.implicitly_wait(config.WAITING_TIME)

    def get_avatar_link(self):
        old_url = self.driver.current_url
        main_page = MainPage(self.driver)
        main_page.get_avatar()
        avatar_photo = PhotoComponent(self.driver)
        avatar_link = avatar_photo.get_photo_link()
        self.driver.get(old_url)
        self.driver.implicitly_wait(config.WAITING_TIME)
        return avatar_link
