from base_page import BasePage
from forms.dialog_menu_form import DialogMenuForm

class DialogMenuPage(BasePage):

    def __init__(self, driver):
        super(DialogMenuPage, self).__init__(driver)
        self.dialog_menu_form = DialogMenuForm(self.driver)

    def delete_dialog(self):
        self.dialog_menu_form.get_delete_dialog_button().click()

    #112Nick
    def leave_chat(self):
        self.dialog_menu_form.get_leave_chat_button().click()

    def hide_chat(self):
        self.dialog_menu_form.get_hide_chat_button().click()
