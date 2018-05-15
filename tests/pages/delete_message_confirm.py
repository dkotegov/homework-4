from base_page import BasePage
from forms.delete_message_confirm_form import DeleteMessageConfirmForm

class DeleteMessageConfirmPage(BasePage):

    def delete_message(self):
        delete_message_confirm_form = DeleteMessageConfirmForm(self.driver)
        delete_message_confirm_form.get_confirm_button().click()