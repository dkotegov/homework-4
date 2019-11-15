from page import Page
from component import Component


class AuthPage(Page):
    @property
    def get_form(self):
        return AuthComponent(self.driver, 'div #mailbox-container')


class AuthComponent(Component):
    def input_login(self, email):
        elem = self.container.find_element_by_id('mailbox:login')
        elem.click()
        elem.clear()
        elem.send_keys(email)

    def input_password(self, password):
        elem = self.container.find_element_by_id('mailbox:password')
        elem.click()
        elem.clear()
        elem.send_keys(password)

    def submit(self):
        self.container.find_element_by_xpath('//input[@class="o-control"][@type="submit"][1]').click()

    def authenticate(self, email, password):
        self.input_login(email)
        self.submit()
        self.input_password(password)
        self.submit()
