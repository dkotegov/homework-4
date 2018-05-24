from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.mobile.like_component import LikeComponent
from tests.pages.mobile.page import Page, Component


class PhotoPage(Page):
    PATH = ''

    @property
    def photo(self):
        return Photo(self.driver)

    @property
    def toolbar(self):
        return Toolbar(self.driver)

    @property
    def confirmation(self):
        return ConfirmationModal(self.driver)

    def make_photo_cover(self):
        toolbar = self.toolbar
        toolbar.open()
        toolbar.make_cover()
        self.confirmation.yes()


class Photo(Component):
    DESCRIPTION = 'photo-description'
    BASE = '//div[contains(@class, "np_photoBox")]'

    @property
    def description(self):
        return self.driver.find_element_by_class_name(self.DESCRIPTION).text

    @property
    def like(self):
        return LikeComponent(self.driver, self.BASE)


class Toolbar(Component):
    TOOLBAR_BUTTON = 'layer-menu'
    COVER_BUTTON = 'ic-acvr'

    def open(self):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, self.TOOLBAR_BUTTON))).click()

    def make_cover(self):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.CLASS_NAME, self.COVER_BUTTON))).click()


class ConfirmationModal(Component):
    YES_BUTTON = '//a[contains(@class, "dialog_action_button") and @data-func="go"]'

    def yes(self):
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable((By.XPATH, self.YES_BUTTON))).click()

        WebDriverWait(self.driver, 2).until_not(EC.presence_of_element_located((By.XPATH, self.YES_BUTTON)))
