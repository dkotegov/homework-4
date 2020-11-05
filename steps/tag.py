from pages.tag import TagPage
from steps.default import Steps


class TagSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, TagPage(driver))

    def back_to_menu(self):
        self.page.form.return_click()

    def delete_source(self):
        self.page.form.delete_click()
        self.page.accept_alert_text()
        return self.page.accept_alert_text()

    def image_presents(self, value):
        return self.page.form.image_presents(value)
