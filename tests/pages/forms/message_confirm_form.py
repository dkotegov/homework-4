from base_element import BaseElement


class MessageConfirmForm(BaseElement):

    CONFIRM_REPORT_BUTTON = '//input[@id="hook_FormButton_button_spam_confirm"]'
    CONFIRM_REMOVE_BUTTON = '//input[@id="hook_FormButton_button_remove_confirm"]'
    REPORT_CANCEL_BUTTON = '//a[@id="button_cancel_confirm"]'
    REPORT_CLOSE_BUTTON = '//a[@id="nohook_modal_close"]'

    def confirm_report(self):
        return self.get_button_by_xpath(self.CONFIRM_REPORT_BUTTON).click()

    def confirm_remove(self):
        return self.get_button_by_xpath(self.CONFIRM_REMOVE_BUTTON).click()

    def cancel_report(self):
        return self.get_button_by_xpath(self.REPORT_CANCEL_BUTTON).click()

    def close_report(self):
        return self.get_button_by_xpath(self.REPORT_CLOSE_BUTTON).click()
