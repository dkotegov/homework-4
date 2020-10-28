from pages.source import SourcePage
from steps.default import Steps


class SourceSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, SourcePage(driver))

    def back_to_menu(self):
        self.page.form.return_click()

    def upload_file(self, path):
        self.page.form.load_image(path)
        return self.page.form.get_image_src()

    def save_img(self, tag):
        self.page.form.save_click()
        self.page.accept_alert_input(tag)
