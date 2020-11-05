from pages.new_proj import NewProjPage
from steps.default import Steps


class NewProjSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, NewProjPage(driver))

    def back_to_menu(self):
        self.page.form.return_click()

    def fill_form(self, name, desc):
        self.page.form.set_name(name)
        self.page.form.set_description(desc)
        self.page.form.submit()
        return self.page.accept_alert_text()
