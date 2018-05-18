from base_element import BaseElement


class MessageConfirmForm(BaseElement):

    CONFIRM_REPORT_BUTTON = '//input[@id="hook_FormButton_button_spam_confirm"]'
    CONFIRM_REMOVE_BUTTON = '//input[@id="hook_FormButton_button_remove_confirm"]'

    def confirm_report(self):
        return self.get_button_by_xpath(self.CONFIRM_REPORT_BUTTON).click()

    def confirm_remove(self):
        return self.get_button_by_xpath(self.CONFIRM_REMOVE_BUTTON).click()
