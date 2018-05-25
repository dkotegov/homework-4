from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from tests.basics import BasicTest
from tests.pages.primary.photo_page import PhotoPage
from tests.pages.primary.main_page import MainPage


from util import config


class PhotoManipulationTest(BasicTest):
    PHOTOS_AFTER_LOAD_A_XPATH = '//a[contains(@hrefattrs, "st.cmd=userPhotos&st._aid=NavMenu_User_Photos")]'

    def setUp(self):
        super(PhotoManipulationTest, self).setUp()
        self.load()

    def tearDown(self):
        self.remove()
        super(PhotoManipulationTest, self).tearDown()

    def load(self):
        old_url = self.driver.current_url
        page = PhotoPage(self.driver)
        page.goto()
        page.load()
        WebDriverWait(self.driver, config.WAITING_TIME_LONG, 0.1).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.PHOTOS_AFTER_LOAD_A_XPATH)))
        self.driver.find_element_by_xpath(self.PHOTOS_AFTER_LOAD_A_XPATH).click()
        self.driver.get(old_url)

    def remove(self):
        MainPage(self.driver).goto_photo()
        page = PhotoPage(self.driver)
        last_loaded = page.get_photo()
        last_loaded.open_overlay()
        toolbar = last_loaded.toolbar()
        toolbar.get_right_toolbar().delete_photo()

    def to_profile(self):
        MainPage(self.driver).goto()

    def to_photos(self):
        MainPage(self.driver).goto_photo()

    def to_photos_from_profile(self):
        PhotoPage(self.driver).goto()

    def open_overlay(self):
        photo_page = PhotoPage(self.driver)
        photo = photo_page.get_photo()
        photo.open_overlay()
