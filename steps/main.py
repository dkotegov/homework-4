from pages.main import MainPage
from steps.default import Steps


class MainSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, MainPage(driver))

    def logout(self):
        self.page.form.logout_click()
