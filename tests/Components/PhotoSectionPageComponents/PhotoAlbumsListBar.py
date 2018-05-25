from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.AlbumPageComponents.AlbumActionPanel import AlbumActionPanel
from tests.Components.Component import Component
from tests.Components.PhotoSectionPageComponents.CreateAlbumPopUp import CreateAlbumPopUp


class PhotoAlbumsListBar(Component):
    CREATE_ALBUM_LINK = '//a[@class="portlet_h_ac lp"]'
    DEFAULT_ALBUM = '//li[@class="ugrid_i"]'
    ALBUM_LIST = '//ul[@class="ugrid_cnt"]'
    NUMBER_OF_PHOTOS_IN_DEFAULT_ALBUM = '//div[contains(@class,"col-card_num")]'

    def open_create_album_popup(self):
        self.driver.find_element_by_xpath(self.CREATE_ALBUM_LINK).click()
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(CreateAlbumPopUp.CONFIRM_ALBUM_CREATION_FORM)
        )

    def open_default_album(self):
        self.driver.find_element_by_xpath(self.DEFAULT_ALBUM).click()

    def open_album_with_name(self, name):
        self.driver.find_element_by_xpath(self.ALBUM_LIST).find_element_by_xpath('//a[@title="' + name + '"]').click()
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(AlbumActionPanel.CONFIRM_ALBUM_OPENED)
        )

    def check_album_with_name(self, name):
        try:
            self.driver.find_element_by_xpath(self.ALBUM_LIST).find_element_by_xpath('//a[@title="' + name + '"]')
        except NoSuchElementException:
            return False
        return True

    def get_number_of_photos_in_default_album(self):
        return self.driver.find_element_by_xpath(self.NUMBER_OF_PHOTOS_IN_DEFAULT_ALBUM).text

