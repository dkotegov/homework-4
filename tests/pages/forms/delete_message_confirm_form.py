from base_element import BaseElement

class DeleteMessageConfirmForm(BaseElement):
    CONFIRM_BUTTON = '//input[@id="hook_FormButton_button_remove_confirm"]'
    
    def get_confirm_button(self):
        return self.get_button_by_xpath(self.CONFIRM_BUTTON)