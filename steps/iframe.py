from pages.iframe import IframePage
from steps.default import Steps


class IframeSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, IframePage(driver))

    def back_to_menu(self):
        self.page.form.return_click()

    def generate(self, proj_id):
        self.page.form.generate_click()
        self.page.accept_alert_input(proj_id)

    def iframe_presents(self):
        return self.page.form.iframe_presents()
