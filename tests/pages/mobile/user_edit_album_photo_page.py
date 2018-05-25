from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.pages.mobile.page import Page, Component


class UserEditAlbumPhotoPage(Page):
    PATH = ''

    @property
    def form(self):
        return EditForm(self.driver)


class EditForm(Component):
    DESCRIPTION_FIELD = 'field_msg'
    SAVE_BUTTON = 'button_save'

    def set_description(self, description):
        WebDriverWait(self.driver, 2, 0.1).until(
            EC.presence_of_element_located((By.ID, self.DESCRIPTION_FIELD))
        ).send_keys(description)

    def save(self):
        current_url = self.driver.current_url
        self.driver.find_element_by_name(self.SAVE_BUTTON).click()
        WebDriverWait(self.driver, 4).until(EC.url_changes(current_url))
