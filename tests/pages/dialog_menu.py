from base_page import BasePage
from forms.dialog_menu_form import DialogMenuForm
from selenium.webdriver.common.keys import Keys
from forms.attach_form import AttachForm


class DialogMenuPage(BasePage):

    def __init__(self, driver):
        super(DialogMenuPage, self).__init__(driver)
        self.dialog_menu_form = DialogMenuForm(self.driver)

    def delete_dialog(self):
        self.dialog_menu_form.get_delete_dialog_button().click()

    # 112Nick
    def leave_chat(self):
        self.dialog_menu_form.get_leave_chat_button().click()

    def hide_chat(self):
        self.dialog_menu_form.get_hide_chat_button().click()

    # Trubnikov
    def change_title(self, title):
        self.dialog_menu_form.get_clickable_chat_title().click()
        self.dialog_menu_form.get_input_title().send_keys(title)
        self.dialog_menu_form.get_input_title().send_keys(Keys.RETURN)

    def get_title(self):
        return self.dialog_menu_form.get_chat_title().get_attribute("innerHTML")

    def change_photo(self, photo_url):
        self.dialog_menu_form.get_change_photo_button().click()
        attach_form = AttachForm(self.driver)
        attach_form.get_dialog_photo().send_keys(photo_url)
        if (attach_form.existence_ready_photo_button()):
            attach_form.get_ready_photo_button().click()
