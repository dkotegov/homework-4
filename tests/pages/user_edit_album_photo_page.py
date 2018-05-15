from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page, Component
from selenium.webdriver.support import expected_conditions as EC


class UserEditAlbumPhotoPage(Page):
    PATH = ''

    @property
    def form(self):
        return EditForm(self.driver)


class EditForm(Component):
    SAVE_BUTTON = 'button_save'

    def submit(self):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable((By.NAME, self.SAVE_BUTTON))).click()
