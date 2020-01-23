from tests.pages.BasicPage import BasicPage


class RemoveConfirmationer(BasicPage):
    confirm_remove_button = '.layer__submit-button'

    def confirm(self):
        elem = self.wait_render(self.confirm_remove_button)
        elem.click()
