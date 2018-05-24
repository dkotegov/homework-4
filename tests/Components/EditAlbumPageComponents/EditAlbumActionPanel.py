# coding=utf-8
from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component
from tests.Components.EditAlbumPageComponents.DeleteAlbumPopUp import DeleteAlbumPopUp


class EditAlbumActionPanel(Component):
    EDIT_CONFIRM = '//div[@data-module = "PhotoEdit"]'
    ACTIONS_PANEL = '//div[@class="photo-panel_info js-photo-album-panel"]'
    DELETE_ALBUM_LINK = '//a[contains(text(), "Удалить альбом")]'

    def open_delete_album_popup(self):
        self.driver.find_element_by_xpath(self.DELETE_ALBUM_LINK).click()
        WebDriverWait(self.driver, 4, 0.5).until(
            lambda d: d.find_element_by_xpath(DeleteAlbumPopUp.CONFIRM_POPUP_APPEARS)
        )
