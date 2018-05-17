from base_page import BasePage
from forms.main_form import MainForm

class MainPage(BasePage):
    def __init__(self, driver):
        super(MainPage, self).__init__(driver)
        self.main_form = MainForm(self.driver)

    def open_messages(self):
        self.main_form.get_message_button().click()
    
    def get_new_message_text(self):
        return self.main_form.get_new_message_text()
    
    def get_existance_of_new_message(self):
        return self.main_form.get_existance_of_new_message()
    