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
        self.driver.find_element_by_id(self.NAME_FIELD).send_keys(name)

    def submit(self):
        self.driver.find_element_by_name(self.SAVE_BUTTON).click()
