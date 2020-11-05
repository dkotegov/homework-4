from pages.auth import AuthPage
from steps.default import Steps


class AuthSteps(Steps):
    def __init__(self, driver):
        Steps.__init__(self, AuthPage(driver))

    def open(self):
        self.page.open()

    def login(self, key):
        self.page.form.set_key(key)
        self.page.form.click_submit()
        return self.page.accept_alert_text()
