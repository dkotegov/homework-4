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
        self.driver.find_element_by_name(self.SAVE_BUTTON).click()
