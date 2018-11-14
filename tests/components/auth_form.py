from component import Component

class AuthForm(Component):
    LOGIN = '//input[@id="mailbox:login"]'
    PASSWORD = '//input[@id="mailbox:password"]'
    SUBMIT = '//input[@class="o-control"]'

    def set_login(self, login):
        self.driver.find_element_by_xpath(self.LOGIN).click()
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        self.driver.find_element_by_xpath(self.SUBMIT).click()