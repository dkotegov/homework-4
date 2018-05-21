import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.mobile.page import Page, Component


class UserAlbumEditPage(Page):
    PATH = '/dk?st.cmd=userAlbumEdit'

    @property
    def form(self):
        return EditForm(self.driver)

    def create_album(self, album_name='Test album #{}'.format(time.time())):
        self.open()
        create_form = self.form
        create_form.set_name(album_name)
        create_form.submit()


class EditForm(Component):
    NAME_FIELD = 'field_name'
    NAME_ERROR = 'field_name_label'
    SAVE_BUTTON = 'button_save'

    def set_name(self, name):
        name_field = self.driver.find_element_by_id(self.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)

    def submit(self):
        self.driver.find_element_by_name(self.SAVE_BUTTON).click()

    def is_name_error(self):
        try:
            self.driver.find_element_by_id(self.NAME_ERROR)
            return True
        except NoSuchElementException:
            return False
