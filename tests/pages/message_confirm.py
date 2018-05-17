from base_page import BasePage
from forms.message_confirm_form import MessageConfirmForm


class MessageConfirmPage(BasePage):
    def __init__(self, driver):
        super(MessageConfirmPage, self).__init__(driver)
        self.confirm_form = MessageConfirmForm(self.driver)

    def confirm_report(self):
        self.confirm_form.confirm_report()