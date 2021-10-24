import os

from pages.default import Page

class DefaultSteps(object):
    def __init__(self, driver):
        self.driver = driver

    def authorize(self):
        self.page.openAuthorize()
        self.page.set_login(os.environ.get('TEST_LOGIN'))
        self.page.continue_authorize()
        self.page.set_password(os.environ.get('TEST_PASSWORD'))
        self.page.submit()
        self.page.waitForAuthorize()