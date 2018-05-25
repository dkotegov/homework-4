from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component
from tests.Components.EditAlbumPageComponents.EditAlbumActionPanel import EditAlbumActionPanel


class AlbumActionPanel(Component):
    EDIT_BUTTON = '//div[contains(@class, "photo-menu_edit")]/a'
    CONFIRM_ALBUM_OPENED = '//div[@id="hook_Block_UserPhotosMRB"]'

    def edit_album(self):
        self.driver.find_element_by_xpath(self.EDIT_BUTTON).click()
        WebDriverWait(self.driver, 30, 2).until(
            lambda d: d.find_element_by_xpath(EditAlbumActionPanel.EDIT_CONFIRM)
        )
