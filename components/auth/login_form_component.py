from components.base_component import Component


class LoginForm(Component):

    LOCATORS = {'LOGIN': 'input[name="Login"]',
                'PASSWORD': 'input[name="Password"]',
                'NEXT_BUTTON': '[data-test-id="next-button"]',
                'SUBMIT_BUTTON': '[data-test-id="submit-button"]',
                }

    def set_login(self, login):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['LOGIN'])
        login_input = self.page.driver.find_element_by_css_selector(self.LOCATORS['LOGIN'])
        login_input.click()
        login_input.send_keys(login)

    def set_password(self, password):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['PASSWORD'])
        password_input = self.page.driver.find_element_by_css_selector(self.LOCATORS['PASSWORD'])
        password_input.click()
        password_input.send_keys(password)

    def next(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['NEXT_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['NEXT_BUTTON']).click()

    def submit(self):
        self.page.waiting_for_visible_by_selector(self.LOCATORS['SUBMIT_BUTTON'])
        self.page.driver.find_element_by_css_selector(self.LOCATORS['SUBMIT_BUTTON']).click()
