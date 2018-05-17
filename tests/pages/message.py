from base_page import BasePage
from forms.message_form import MessageForm
from forms.companion_form import CompanionForm
from time import sleep

class MessagePage(BasePage):

    def __init__(self, driver):
        super(MessagePage, self).__init__(driver)
        self.message_form = MessageForm(self.driver)
        self.companion_form = CompanionForm(self.driver)

    def create_dialog(self):
       self.message_form.get_create_dialog_button().click()
    
    def choose_companion(self):
        self.companion_form.get_companion_button().click()
        self.companion_form.get_create_dialog_button().click()

    def choose_companion_forward_message(self):
        self.companion_form.get_forward_companion_button().click()
        self.companion_form.get_create_dialog_button().click()

    def get_existance_of_search_result(self):
        return self.message_form.get_search_result()
    
    #112Nick
    def get_found_message_text(self):
        return self.message_form.get_found_message_text()

    def get_existance_of_dialogs_empty(self):
        return self.message_form.get_dialogs_empty()