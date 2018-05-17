from base_page import BasePage
from forms.confirm_form import ConfirmForm



class ConfirmPage(BasePage):

    def confirm(self):
        delete_dialog_confirm_form = ConfirmForm(self.driver)
        delete_dialog_confirm_form.get_confirm_button().click()