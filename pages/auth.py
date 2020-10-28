from pages.default import Page, Component


class AuthPage(Page):
    PATH = ''

    @property
    def form(self):
        return AuthForm(self.driver)


class AuthForm(Component):
    KEY = '//input[@id="inpField"]'
    SUBMIT = '//div[@id="btnSend"]'

    def set_key(self, key):
        self.wait_for_visible(self.KEY)
        input_key = self.driver.find_element_by_xpath(self.KEY)
        input_key.clear()
        input_key.send_keys(key)

    def click_submit(self):
        self.wait_for_visible(self.SUBMIT)
        self.driver.find_element_by_xpath(self.SUBMIT).click()
