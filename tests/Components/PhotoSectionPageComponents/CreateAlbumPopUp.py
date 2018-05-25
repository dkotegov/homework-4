from selenium.webdriver.support.wait import WebDriverWait

from tests.Components.AlbumPageComponents.AlbumActionPanel import AlbumActionPanel
from tests.Components.Component import Component


class CreateAlbumPopUp(Component):

    ALBUM_NAME_FORM = '//input[@name="st.layer.photoAlbumName"]'
    CHECKBOX_FOR_EVERYONE = '//input[@id="policy_2"]'
    CHECKBOX_FOR_ALL_FRIENDS = '//input[@id="policy_1"]'
    CREATE_ALBUM_BUTTON = '//input[@name="button_album_create"]'
    CONFIRM_ALBUM_CREATION_FORM = '//div[@id="popLayer_cc"]'
    CLOSE_POPUP_LINK = '//div[@class="layerPanelClose ic ic_close"]'

    def set_album_name(self, name):
        self.driver.find_element_by_xpath(self.ALBUM_NAME_FORM).send_keys(name)

    def set_album_policy(self, policy):
        if policy == 1:
            self.driver.find_element_by_xpath(self.CHECKBOX_FOR_ALL_FRIENDS).click()
        else:
            self.driver.find_element_by_xpath(self.CHECKBOX_FOR_EVERYONE).click()

    def submit_album_creation(self):
        self.driver.find_element_by_xpath(self.CREATE_ALBUM_BUTTON).click()
        WebDriverWait(self.driver, 5, 0.2).until(
            lambda d: d.find_element_by_xpath(AlbumActionPanel.CONFIRM_ALBUM_OPENED)
        )

    def close_create_album_popup(self):
        self.driver.find_element_by_xpath(self.CLOSE_POPUP_LINK).click()
        WebDriverWait(self.driver, 5, 0.2).until_not(
            lambda d: d.find_element_by_xpath(AlbumActionPanel.CONFIRM_ALBUM_OPENED)
        )


