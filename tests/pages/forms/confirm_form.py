from base_element import BaseElement


class ConfirmForm(BaseElement):
    CONFIRM_BUTTON = '//input[contains(@id, "hook_FormButton")]'

    def get_confirm_button(self):
        return self.get_button_by_xpath(self.CONFIRM_BUTTON)
