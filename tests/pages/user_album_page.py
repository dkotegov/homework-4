from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page, Component


class UserAlbumPage(Page):
    PATH = '/dk?st.cmd=userAlbumEdit'

    @property
    def empty_album_content(self):
        return EmptyAlbumContent(self.driver)

    @property
    def toolbar(self):
        return Toolbar(self.driver)

    @property
    def confirmation_modal(self):
        return ConfirmationModal(self.driver)


class EmptyAlbumContent(Component):
    TITLE = 'ep-ttl-txt'

    @property
    def title(self):
        return self.driver.find_element_by_class_name(self.TITLE).text


class Toolbar(Component):
    TOOLBAR_BUTTON = 'js-t-widget'
    EDIT_BUTTON = 'ic-edit'
    DELETE_BUTTON = 'ic-del'

    def open(self):
        WebDriverWait(self.driver, 2, 0.1).until(EC.element_to_be_clickable((By.ID, self.TOOLBAR_BUTTON))).click()

    def edit(self):
        self.driver.find_element_by_class_name(self.EDIT_BUTTON).click()

    def delete(self):
        self.driver.find_element_by_class_name(self.DELETE_BUTTON).click()


class ConfirmationModal(Component):
    DELETE_BUTTON = 'button_delete'

    def delete(self):
        self.driver.find_element_by_name(self.DELETE_BUTTON).click()
