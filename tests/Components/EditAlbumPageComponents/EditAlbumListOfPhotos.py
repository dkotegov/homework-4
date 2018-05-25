# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.AlbumPageComponents.ListOfPhotos import ListOfPhotos
from tests.Components.Component import Component


class EditAlbumListOfPhotos(Component):
    DELETE_PHOTO_BUTTON = '//a'
    RESTORE_PHOTO_LINK = '//a[contains(text(), "Восстановить")]'
    CONFIRM_PHOTO_DELETED = '//div[contains(@class, "__deleted")]'
    CONFIRM_LIST_OF_PHOTOS = '//ul[contains(@id, "photo-sc_grid-edit")]'
    BACK_TO_ALBUM_LINK = '//span[contains(text(), "Вернуться назад")]'

    def __find_photo_button_by_id(self, photo_id):
        return self.driver.find_element_by_xpath('//div[@data-id="'+photo_id+'"]/..'+self.DELETE_PHOTO_BUTTON)

    def delete_photo_by_id(self, photo_id):
        self.__find_photo_button_by_id(photo_id).click()

    def wait_until_photo_deleted(self):
        WebDriverWait(self.driver, 4, 0.5).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_PHOTO_DELETED)
        )

    def restore_last_deleted_photo(self):
        self.driver.find_element_by_xpath(self.RESTORE_PHOTO_LINK).click()

    def wait_until_list_of_photos_loaded(self):
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda d: d.find_element_by_xpath(self.CONFIRM_PHOTO_DELETED)
        )

    def redirect_back_to_album_page(self):
        self.driver.find_element_by_xpath(self.BACK_TO_ALBUM_LINK).click()
        WebDriverWait(self.driver, 10, 0.5).until(
            lambda d: d.find_element_by_xpath(ListOfPhotos.PHOTOS_UL)
        )
