from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.page import Page, Component


class UserAlbumEditPage(Page):
    PATH = '/dk?st.cmd=userAlbumEdit'

    @property
    def form(self):
        return EditForm(self.driver)


class EditForm(Component):
    NAME_FIELD = 'field_name'
    SAVE_BUTTON = 'button_save'

    def set_name(self, name):
        name_field = self.driver.find_element_by_id(self.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

    def submit(self):
        current_url = self.driver.current_url
        self.driver.find_element_by_name(self.SAVE_BUTTON).click()
        WebDriverWait(self.driver, 4).until(EC.url_changes(current_url))
