from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.Component import Component


class DeleteAlbumPopUp(Component):

    CONFIRM_POPUP_APPEARS = '//div[@id="cfrmPopLayerRemoveUserAlbums"]'
    DELETE_ALBUM_BUTTON = '//input[@id="hook_FormButton_button_delete_confirm"]'

    def press_delete_button_in_popup(self):
        self.driver.find_element_by_xpath(self.DELETE_ALBUM_BUTTON).click()
        WebDriverWait(self.driver, 30, 2).until_not(
            lambda d: d.find_element_by_xpath(self.CONFIRM_POPUP_APPEARS)
        )


